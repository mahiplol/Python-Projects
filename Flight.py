from Airport import *


class Flight:
    def __init__(self, flightNo, origin, destination):
        self._flightNo = flightNo
        if isinstance(origin, Airport) and isinstance(destination,
                                                      Airport):  # Checking that both origin and destination are Airport objects
            self._origin = origin
            self._destination = destination
        else:
            raise TypeError(
                "the origin and destination must be airport objects")  # If either or both are not Airport objects, then raising a TypeError

    def __repr__(self):
        # Return the representation of this Flight containing the flightNo, origin city, and destination city, and an indication of whether the Flight is domestic or international
        flight = ""
        if not self.isDomesticFlight():
            flight += "international"
        else:
            flight += "domestic"

        return "Flight: " + str(self._flightNo) + \
               " from " + self._origin.getCity() + \
               " to " + self._destination.getCity() + \
               " {" + flight + "}"

    def __eq__(self, other):
        # Method that returns True if self and other are considered the same Flight
        if self._origin.getCity() is other._origin.getCity() and self._destination.getCity() is other._destination.getCity():
            return True
        else:
            return False

    def getFlightNumber(self):
        # Getter that returns the Flight number code
        return self._flightNo

    def getOrigin(self):
        # Getter that returns the Flight origin
        return self._origin

    def getDestination(self):
        # Getter that returns the Flight destination
        return self._destination

    def isDomesticFlight(self):
        # Method that returns True if the flight is domestic; returns False if the flight is international
        if self._origin.getCountry() is self._destination.getCountry():
            return True
        else:
            return False

    def setOrigin(self, origin):
        # Setter that sets (updates) the Flight origin
        self._origin = origin

    def setDestination(self, destination):
        # Setter that sets (updates) the Flight destination
        self._destination = destination
