"""A module for working with Vizzu charts."""

import pkgutil
import uuid
from typing import List, Optional, Union

from IPython.display import display_javascript  # type: ignore
from IPython import get_ipython  # type: ignore

from ipyvizzu.animation import AbstractAnimation, Snapshot, AnimationMerger
from ipyvizzu.animationcontrol import AnimationControl
from ipyvizzu.method import Animate, Feature, Store, EventOn, EventOff, Log
from ipyvizzu.template import ChartProperty, DisplayTarget, DisplayTemplate
from ipyvizzu.event import EventHandler


class Chart:
    """A class for representing a wrapper over Vizzu chart."""

    # pylint: disable=too-many-instance-attributes

    VIZZU: str = "https://cdn.jsdelivr.net/npm/vizzu@0.7/dist/vizzu.min.js"
    """A variable for storing the default url of vizzu package."""

    def __init__(
        self,
        vizzu: str = VIZZU,
        width: str = "800px",
        height: str = "480px",
        display: Union[DisplayTarget, str] = DisplayTarget.ACTUAL,
    ):
        """
        Chart constructor.

        Args:
            vizzu: The url of Vizzu JavaScript package.
            width: The width of the chart.
            height: The height of the chart.
            display: The display behaviour of the chart.
        """

        self._chart_id: str = uuid.uuid4().hex[:7]

        self._vizzu: str = vizzu
        self._width: str = width
        self._height: str = height

        self._display_target: DisplayTarget = DisplayTarget(display)
        self._calls: List[str] = []
        self._last_anim: Optional[str] = None
        self._showed: bool = False

        self._initialized: bool = False
        self._scroll_into_view: bool = False

    @staticmethod
    def _register_events() -> None:
        ipy = get_ipython()
        if ipy is not None:
            ipy.events.register("pre_run_cell", Chart._register_pre_run_cell)

    @staticmethod
    def _register_pre_run_cell() -> None:
        display_javascript(DisplayTemplate.CLEAR_INHIBITSCROLL, raw=True)

    @property
    def scroll_into_view(self) -> bool:
        """
        A property for turning on/off the scroll into view feature.

        Returns:
            The value of the property (default `False`).
        """

        return self._scroll_into_view

    @scroll_into_view.setter
    def scroll_into_view(self, scroll_into_view: Optional[bool]):
        self._scroll_into_view = bool(scroll_into_view)

    @property
    def control(self) -> AnimationControl:
        """
        A property for returning a control object of the last animation.

        Raises:
            AssertionError: If called before any animation plays.

        Returns:
            The control object of the last animation.
        """
        assert self._last_anim, "must be used after an animation."
        return AnimationControl(self._chart_id, self._last_anim, self._display)

    def initializing(self) -> None:
        """A method for initializing the chart."""

        if not self._initialized:
            self._initialized = True
            ipyvizzurawjs = pkgutil.get_data(__name__, "templates/ipyvizzu.js")
            ipyvizzujs = ipyvizzurawjs.decode("utf-8")  # type: ignore
            self._display(DisplayTemplate.IPYVIZZUJS.format(ipyvizzujs=ipyvizzujs))

            if self._display_target != DisplayTarget.MANUAL:
                Chart._register_events()

            self._display(
                DisplayTemplate.INIT.format(
                    chart_id=self._chart_id,
                    vizzu=self._vizzu,
                    div_width=self._width,
                    div_height=self._height,
                )
            )

    def animate(
        self,
        *animations: AbstractAnimation,
        **options: Optional[Union[str, int, float, dict]],
    ) -> None:
        """
        A method for changing the state of the chart.

        Args:
            *animations:
                List of AbstractAnimation inherited objects such as [Data][ipyvizzu.animation.Data],
                [Config][ipyvizzu.animation.Config] and [Style][ipyvizzu.animation.Style].
            **options: Dictionary of animation options for example `duration=1`.
                For information on all available animation options see the
                [Vizzu Code reference](https://lib.vizzuhq.com/0.7/reference/interfaces/vizzu.Anim.Options/#properties).

        Raises:
            ValueError: If `animations` is not set.

        Example:
            Reset the chart styles:

                chart.animate(Style(None))
        """  # pylint: disable=line-too-long

        if not animations:
            raise ValueError("No animation was set.")

        animation = AnimationMerger.merge_animations(animations)
        animate = Animate(animation, options)

        self._last_anim = uuid.uuid4().hex[:7]
        self._display(
            DisplayTemplate.ANIMATE.format(
                display_target=self._display_target.value,
                chart_id=self._chart_id,
                anim_id=self._last_anim,
                scroll=str(self._scroll_into_view).lower(),
                **animate.dump(),
            )
        )

    def feature(self, name: str, enabled: bool) -> None:
        """
        A method for turning on/off features of the chart.

        Args:
            name:
                The name of the chart feature.
                For information on all available features see the
                [Vizzu Code reference](https://lib.vizzuhq.com/0.7/reference/modules/vizzu/#feature).
            enabled: The new state of the chart feature.

        Example:
            Turn on `tooltip` of the chart:

                chart.feature("tooltip", True)
        """  # pylint: disable=line-too-long

        self._display(
            DisplayTemplate.FEATURE.format(
                chart_id=self._chart_id,
                **Feature(name, enabled).dump(),
            )
        )

    def store(self) -> Snapshot:
        """
        A method for saving and storing the actual state of the chart.

        Returns:
            A Snapshot object wich stores the actual state of the chart.

        Example:
            Save and restore the actual state of the chart:

                snapshot = chart.store()
                ...
                chart.animate(snapshot)
        """

        snapshot_id = uuid.uuid4().hex[:7]
        self._display(
            DisplayTemplate.STORE.format(
                chart_id=self._chart_id, **Store(snapshot_id).dump()
            )
        )
        return Snapshot(snapshot_id)

    def on(  # pylint: disable=invalid-name
        self, event: str, handler: str
    ) -> EventHandler:
        """
        A method for creating and turning on an event handler.

        Args:
            event:
                The type of the event.
                For information on all available events see the
                [Vizzu Code reference](https://lib.vizzuhq.com/0.7/reference/modules/vizzu.Event/#type).
            handler: The JavaScript method of the event.

        Returns:
            The turned on event handler object.

        Example:
            Turn on an event handler which prints an alert message
            when someone clicks on the chart:

                handler = chart.on("click", "alert(JSON.stringify(event.data));")
        """  # pylint: disable=line-too-long

        event_handler = EventHandler(event, handler)
        self._display(
            DisplayTemplate.SET_EVENT.format(
                chart_id=self._chart_id,
                **EventOn(event_handler).dump(),
            )
        )
        return event_handler

    def off(self, event_handler: EventHandler) -> None:
        """
        A method for turning off an event handler.

        Args:
            event_handler: A previously created event handler object.

        Example:
            Turn off a previously created event handler:

                chart.off(handler)
        """

        self._display(
            DisplayTemplate.CLEAR_EVENT.format(
                chart_id=self._chart_id,
                **EventOff(event_handler).dump(),
            )
        )

    def log(self, chart_property: ChartProperty) -> None:
        """
        A method for printing chart properties to the browser console.

        Args:
            chart_property:
                A chart property such as
                [CONFIG][ipyvizzu.template.ChartProperty] and
                [STYLE][ipyvizzu.template.ChartProperty].

        Example:
            Log the actual style of the chart to the browser console:

                chart.log(ChartProperty.STYLE)
        """

        self._display(
            DisplayTemplate.LOG.format(
                chart_id=self._chart_id, **Log(chart_property).dump()
            )
        )

    def _repr_html_(self) -> str:
        assert (
            self._display_target == DisplayTarget.MANUAL
        ), "chart._repr_html_() can be used with display=DisplayTarget.MANUAL only"
        assert not self._showed, "cannot be used after chart displayed."
        self._showed = True
        if not self._initialized:
            return ""
        html_id = uuid.uuid4().hex[:7]
        script = (
            self._calls[0]
            + "\n"
            + "\n".join(self._calls[1:]).replace(
                "element", f'document.getElementById("{html_id}")'
            )
        )
        return f'<div id="{html_id}"><script>{script}</script></div>'

    def show(self) -> None:
        """
        A method for displaying the assembled JavaScript code.

        Raises:
            AssertionError: If [display][ipyvizzu.Chart.__init__]
                is not [DisplayTarget.MANUAL][ipyvizzu.template.DisplayTarget].
            AssertionError: If chart already has been displayed.
        """

        assert (
            self._display_target == DisplayTarget.MANUAL
        ), "chart.show() can be used with display=DisplayTarget.MANUAL only"
        assert not self._showed, "cannot be used after chart displayed"
        display_javascript(
            "\n".join(self._calls),
            raw=True,
        )
        self._showed = True

    def _display(self, javascript: str) -> None:
        if not self._initialized:
            self.initializing()
        if self._display_target != DisplayTarget.MANUAL:
            display_javascript(
                javascript,
                raw=True,
            )
        else:
            assert not self._showed, "cannot be used after chart displayed"
            self._calls.append(javascript)
