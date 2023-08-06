from __future__ import annotations

from typing import Optional, Tuple

import numpy as np

from retentioneering.constants import DATETIME_UNITS
from retentioneering.data_processor import DataProcessor
from retentioneering.eventstream.types import EventstreamType
from retentioneering.params_model import ParamsModel
from retentioneering.widget.widgets import ReteTimeWidget


class DeleteUsersByPathLengthParams(ParamsModel):
    """
    A class with parameters for :py:class:`.DeleteUsersByPathLength` class.
    """

    events_num: Optional[int]
    cutoff: Optional[Tuple[float, DATETIME_UNITS]]

    _widgets = {
        "cutoff": ReteTimeWidget(),
    }


class DeleteUsersByPathLength(DataProcessor):
    """
    Filter user paths based on the path length, removing the paths that are shorter than the
    specified number of events or cut_off.

    Parameters
    ----------
    events_num : int, optional
        Minimum user path length

    cutoff : Tuple(float, :numpy_link:`DATETIME_UNITS<>`), optional
        Minimum user path length and its unit of measure.

    Returns
    -------
    Eventstream
        ``Eventstream`` with events that should be deleted from input ``eventstream`` marked ``_deleted=True``.

    Raises
    ------
    ValueError
        If both of ``events_num`` and ``cutoff`` are empty or both are given.

    See Also
    --------
    .TimedeltaHist : Plot the distribution of the time deltas between two events.
    .UserLifetimeHist : Plot the distribution of user lifetimes.

    Notes
    -----
    See :doc:`Data processors user guide</user_guides/dataprocessors>` for the details.
    """

    params: DeleteUsersByPathLengthParams

    def __init__(self, params: DeleteUsersByPathLengthParams):
        super().__init__(params=params)

    def apply(self, eventstream: EventstreamType) -> EventstreamType:
        from retentioneering.eventstream.eventstream import Eventstream

        user_col = eventstream.schema.user_id
        time_col = eventstream.schema.event_timestamp

        cutoff, cutoff_unit = None, None
        events_num = self.params.events_num

        if self.params.cutoff:
            cutoff, cutoff_unit = self.params.cutoff

        if events_num and cutoff:
            raise ValueError("Events_num and cutoff parameters cannot be used simultaneously!")

        if not events_num and not cutoff:
            raise ValueError("Either events_num or cutoff must be specified!")

        events = eventstream.to_dataframe(copy=True)

        if cutoff and cutoff_unit:
            userpath = (
                events.groupby(user_col)[time_col]
                .agg([np.min, np.max])
                .rename(columns={"amin": "start", "amax": "end"})
            )
            mask_ = (userpath["end"] - userpath["start"]) / np.timedelta64(1, cutoff_unit) < cutoff  # type: ignore

        else:
            userpath = events.groupby([user_col])[[time_col]].nunique().rename(columns={time_col: "length"})
            mask_ = userpath["length"] < events_num

        users_to_delete = userpath[mask_].index
        events = events[events[user_col].isin(users_to_delete)]
        events["ref"] = events.loc[:, eventstream.schema.event_id]

        eventstream = Eventstream(
            raw_data_schema=eventstream.schema.to_raw_data_schema(),
            raw_data=events,
            relations=[{"raw_col": "ref", "eventstream": eventstream}],
        )

        if not events.empty:
            eventstream._soft_delete(eventstream.to_dataframe())

        return eventstream
