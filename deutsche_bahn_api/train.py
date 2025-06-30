from __future__ import annotations

from deutsche_bahn_api.train_changes import TrainChanges


class Train:
    stop_id: str
    trip_type: str | None
    train_type: str
    train_number: str
    train_line: str | None
    platform: str | None
    passed_stations: str | None
    stations: str | None
    arrival: str | None
    departure: str | None
    train_changes: TrainChanges | None

    def __init__(self):
        self.trip_type = None
        self.train_line = None
        self.platform = None
        self.passed_stations = None
        self.stations = None
        self.arrival = None
        self.departure = None
        self.train_changes = None


