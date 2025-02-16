"""
******************************
Code by: Muniver Kharod
******************************
Defines the Flight class for managing flight details between airports.
"""
from Airport import *

class Flight:
    def __init__(self, flight_no, origin, dest, dur):
        # Ensure origin and destination are Airport objects
        if not isinstance(origin, Airport) or not isinstance(dest, Airport):
            raise TypeError("The origin and destination must be Airport objects")
        # Initialize instance attributes
        self._flight_no = flight_no
        self._origin = origin
        self._destination = dest
        self._duration = dur

    def __str__(self):
        # Determine if the flight is domestic or international
        flight_type = "domestic" if self.is_domestic() else "international"
        duration_hours = round(self._duration)
        return f"{self._origin.get_city()} to {self._destination.get_city()} ({duration_hours}h) [{flight_type}]"

    def __eq__(self, other):
        # Check if 'other' is a Flight instance and compare attributes
        if not isinstance(other, Flight):
            return False
        return self._origin == other._origin and self._destination == other._destination

    def __add__(self, conn_flight):
        # Ensure conn_flight is a Flight object
        if not isinstance(conn_flight, Flight):
            raise TypeError("The connecting_flight must be a Flight object")
        # Ensure the flights are combinable
        if self._destination != conn_flight._origin:
            raise ValueError("These flights cannot be combined")
        # Create a new Flight object representing the combined flight
        new_flight_no = self._flight_no
        new_origin = self._origin
        new_destination = conn_flight._destination
        new_duration = self._duration + conn_flight._duration
        return Flight(new_flight_no, new_origin, new_destination, new_duration)

    def get_flight_no(self):
        # Getter for flight number
        return self._flight_no

    def get_origin(self):
        # Getter for origin
        return self._origin

    def get_destination(self):
        # Getter for destination
        return self._destination

    def get_duration(self):
        # Getter for duration
        return self._duration

    def is_domestic(self):
        # Check if flight is domestic
        return self._origin.get_country().strip().lower() == self._destination.get_country().strip().lower()

    def set_origin(self, origin):
        # Setter for origin
        if not isinstance(origin, Airport):
            raise TypeError("Origin must be an Airport object")
        self._origin = origin

    def set_destination(self, destination):
        # Setter for destination
        if not isinstance(destination, Airport):
            raise TypeError("Destination must be an Airport object")
        self._destination = destination
