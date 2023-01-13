class Transmitter:
    def __init__(self, waste_type, location, active, status, identyficator):
        self.waste_type = waste_type
        self.location = location
        self.active = active
        self.status = status
        self.identificator = identyficator

    def __init__(self, active, status, identyficator):
        self.active = active
        self.status = status
        self.identificator = identyficator
