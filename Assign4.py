"""
******************************
CS 1026 - Assignment 4 - Main Program
Code by: Muniver Kharod
Student ID: mkharod2
File created: December 3, 2024
******************************
Loads airport and flight data, supports flight analysis, and handles queries.
"""
from Flight import *
from Airport import *

# variables for storing data
all_airports = {}  # Maps airport codes to Airport objects
all_flights = {}   # Maps origin airport codes to lists of Flight objects


def load_data(airport_file, flight_file):
    """
    Loads airport and flight data from text files.
    Populates all_airports and all_flights dictionaries.
    """
    try:
        # Load airport data
        with open(airport_file, 'r') as af:
            for line in af:
                line = line.strip()
                if line:  # Skip empty lines
                    code, country, city = [part.strip()
                                           for part in line.split('-', maxsplit=2)]
                    all_airports[code.upper()] = Airport(
                        code.upper(), city, country)

        # Load flight data
        with open(flight_file, 'r') as ff:
            for line in ff:
                line = line.strip()
                if line:  # Skip empty lines
                    parts = [part.strip() for part in line.split('-')]
                    flight_no = f"{parts[0]}-{parts[1]}"
                    origin_code = parts[2].upper()
                    dest_code = parts[3].upper()
                    try:
                        duration = float(parts[4])
                    except ValueError:
                        continue  # Skip invalid duration values

                    # Add flights to the dictionary if airports exist
                    if origin_code in all_airports and dest_code in all_airports:
                        flight = Flight(
                            flight_no,
                            all_airports[origin_code],
                            all_airports[dest_code],
                            duration,
                        )
                        all_flights.setdefault(origin_code, []).append(flight)

        return True
    except Exception as e:
        print(f"Error loading data: {e}")
        return False


def get_airport_by_code(code):
    """Fetches an Airport object by its code."""
    code = code.strip().upper()
    if code in all_airports:
        return all_airports[code]
    else:
        raise ValueError(f"No airport with the given code: {code}")


def find_all_city_flights(city):
    """Finds all flights to or from a given city."""
    city = city.strip().lower()
    result = []

    # Parse flights to identify city-specific matches
    for flights in all_flights.values():
        for flight in flights:
            if flight.get_origin().get_city().lower() == city or flight.get_destination().get_city().lower() == city:
                result.append(flight)

    return result


def find_all_country_flights(country):
    """Finds all flights to or from a given country."""
    country = country.strip().lower()
    result = []

    # Parse flights to find matches for the country
    for flights in all_flights.values():
        for flight in flights:
            if flight.get_origin().get_country().lower() == country or flight.get_destination().get_country().lower() == country:
                result.append(flight)

    return result


def find_flight_between(orig_airport, dest_airport):
    """
    Locates a flight that connects two airports directly or with a single hop.
    Returns: - If flight information is located, provide it directly.
        A collection of linking airport codes for connections with only one hop.
    If there are no flights, raises: ValueError.
    """
    orig_code = orig_airport.get_code().upper()
    dest_code = dest_airport.get_code().upper()

    # Check for direct flight
    if orig_code in all_flights:
        for flight in all_flights[orig_code]:
            if flight.get_destination().get_code().upper() == dest_code:
                return f"Direct Flight: {orig_code} to {dest_code}"

    # Check for single-hop connections
    connecting_airports = set()
    if orig_code in all_flights:
        for flight1 in all_flights[orig_code]:
            mid_airport = flight1.get_destination()
            mid_code = mid_airport.get_code().upper()
            if mid_code in all_flights:
                for flight2 in all_flights[mid_code]:
                    if flight2.get_destination().get_code().upper() == dest_code:
                        connecting_airports.add(mid_code)

    if connecting_airports:
        return connecting_airports

    raise ValueError(f"No flights found from {orig_code} to {dest_code}")


def find_return_flight(first_flight):
    """Determines a flight's return for a specified Flight object.."""
    orig_airport = first_flight.get_origin()
    dest_airport = first_flight.get_destination()
    orig_code = orig_airport.get_code().upper()
    dest_code = dest_airport.get_code().upper()

    # Check for a return flight
    if dest_code in all_flights:
        for flight in all_flights[dest_code]:
            if flight.get_destination().get_code().upper() == orig_code:
                return flight

    raise ValueError(f"No return flight found from {dest_code} to {orig_code}")


def shortest_flight_from(orig_airport):
    """Determines which airport has the shortest flight leaving from it.."""
    orig_code = orig_airport.get_code().upper()

    # Check if the origin has flights
    if orig_code not in all_flights:
        return None

    flights_from_origin = all_flights[orig_code]

    # Find and return the flight with the shortest time duration
    min_duration = min(flight.get_duration() for flight in flights_from_origin)
    for flight in flights_from_origin:
        if flight.get_duration() == min_duration:
            return flight

    return None


if __name__ == "__main__":
      pass