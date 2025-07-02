from deutsche_bahn_api.message import Message


class TrainChanges:
    """ This class represents changed train attributes. """
    departure: str | None
    arrival: str | None
    passed_stations: str | None
    stations: str | None
    platform: str | None
    departure_status: str | None
    arrival_status: str | None
    departure_cancellation_time: str | None
    arrival_cancellation_time: str | None
    messages: list[Message]

    def __init__(self):
        self.departure = None
        self.arrival = None
        self.passed_stations = None
        self.stations = None
        self.platform = None
        self.departure_status = None
        self.arrival_status = None
        self.departure_cancellation_time = None
        self.arrival_cancellation_time = None
        self.messages = []
