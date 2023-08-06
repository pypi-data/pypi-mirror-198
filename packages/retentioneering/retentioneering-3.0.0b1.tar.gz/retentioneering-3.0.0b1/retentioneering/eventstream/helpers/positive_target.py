from __future__ import annotations

from typing import Callable, List, Optional

from ..types import EventstreamType


class PositiveTargetHelperMixin:
    def positive_target(self, positive_target_events: List[str], func: Optional[Callable] = None) -> EventstreamType:
        """
        A method of ``Eventstream`` class that creates new synthetic
        events in paths of all users having the specified events - ``positive_target_RAW_EVENT_NAME``.

        Parameters
        ----------
        See parameters description
            :py:class:`.PositiveTarget`

        Returns
        -------
        Eventstream
            Input ``eventstream`` with new synthetic events.



        """
        # avoid circular import
        from retentioneering.data_processors_lib import (
            PositiveTarget,
            PositiveTargetParams,
        )
        from retentioneering.graph.nodes import EventsNode
        from retentioneering.graph.p_graph import PGraph

        p = PGraph(source_stream=self)  # type: ignore

        params: dict[str, list[str] | Callable] = {"positive_target_events": positive_target_events}
        if func:
            params["func"] = func

        node = EventsNode(processor=PositiveTarget(params=PositiveTargetParams(**params)))  # type: ignore
        p.add_node(node=node, parents=[p.root])
        result = p.combine(node)
        del p
        return result
