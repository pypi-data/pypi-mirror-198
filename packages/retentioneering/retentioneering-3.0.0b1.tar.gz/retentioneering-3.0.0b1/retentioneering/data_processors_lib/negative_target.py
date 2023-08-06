from __future__ import annotations

from typing import Any, Callable, List

import pandas as pd

from retentioneering.data_processor import DataProcessor
from retentioneering.eventstream.schema import EventstreamSchema
from retentioneering.eventstream.types import EventstreamType
from retentioneering.params_model import ParamsModel
from retentioneering.widget.widgets import ListOfString, ReteFunction

EventstreamFilter = Callable[[pd.DataFrame, EventstreamSchema], Any]


def _default_func(eventstream: EventstreamType, negative_target_events: List[str]) -> pd.DataFrame:
    """
    Filters rows with target events from the input eventstream.

    Parameters
    ----------
    eventstream : Eventstream
        Source eventstream or output from previous nodes.

    negative_target_events : list of str
        Each event from that list is associated with the bad result (scenario)
        of user's behaviour (experience) in the product.
        If there are several target events in user path - the event with minimum timestamp is taken.

    Returns
    -------
    pd.DataFrame
        Filtered DataFrame with negative_target_events and its timestamps.
    """
    user_col = eventstream.schema.user_id
    time_col = eventstream.schema.event_timestamp
    event_col = eventstream.schema.event_name
    df = eventstream.to_dataframe()

    negative_events_index = (
        df[df[event_col].isin(negative_target_events)].groupby(user_col)[time_col].idxmin()  # type: ignore
    )

    return df.loc[negative_events_index]  # type: ignore


class NegativeTargetParams(ParamsModel):
    """
    A class with parameters for :py:class:`.NegativeTarget` class.
    """

    negative_target_events: List[str]
    func: Callable = _default_func

    _widgets = {"func": ReteFunction(), "negative_target_events": ListOfString()}


class NegativeTarget(DataProcessor):
    """
    Create new synthetic events in paths of all users having the specified event(s):
    ``negative_target_RAW_EVENT_NAME``.

    Parameters
    ----------
    negative_target_events : list of str
        Define the list of events that we consider negative.
        If there are several target events in the user path, the event with the minimum timestamp is taken.

    func : Callable, default _default_func_negative
        Filter rows with target events from the input eventstream.

    Returns
    -------
    Eventstream
        ``Eventstream`` with new synthetic events only added to the users who fit the conditions.

        +--------------------------------+-----------------+-----------------------------+
        | **event_name**                 | **event_type**  | **timestamp**               |
        +--------------------------------+-----------------+-----------------------------+
        | negative_target_RAW_EVENT_NAME | negative_target | min(negative_target_events) |
        +--------------------------------+-----------------+-----------------------------+

    Notes
    -----
    See :doc:`Data processors user guide</user_guides/dataprocessors>` for the details.


    """

    params: NegativeTargetParams

    def __init__(self, params: NegativeTargetParams):
        super().__init__(params=params)

    def apply(self, eventstream: EventstreamType) -> EventstreamType:
        from retentioneering.eventstream.eventstream import Eventstream

        type_col = eventstream.schema.event_type
        event_col = eventstream.schema.event_name

        func = self.params.func
        negative_target_events = self.params.negative_target_events

        negative_targets = func(eventstream, negative_target_events)
        negative_targets[type_col] = "negative_target"
        negative_targets[event_col] = "negative_target_" + negative_targets[event_col]
        negative_targets["ref"] = None

        eventstream = Eventstream(
            raw_data_schema=eventstream.schema.to_raw_data_schema(),
            raw_data=negative_targets,
            relations=[{"raw_col": "ref", "eventstream": eventstream}],
        )
        return eventstream
