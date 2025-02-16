"""
******************************
CS 1026 - Assignment 4
Code by: Muniver Kharod
Student ID: mkharod2
File created: December 3, 2024
******************************
Defines the Airport class for managing airport information.
"""
class Airport:
    def __init__(self, code, city, country):
        # Initialize the instance's _code, _city, and _country attributes
        self._code = code.strip().upper()
        self._city = city.strip()
        self._country = country.strip()

    def __str__(self):
        # Return the string representation in the format: code (city, country)
        return f"{self._code} ({self._city}, {self._country})"

    def __eq__(self, other):
        # Check if 'other' is an Airport instance and compare codes
        if isinstance(other, Airport):
            return self._code == other._code
        return False

    def get_code(self):
        # Getter returning the Airport code
        return self._code

    def get_city(self):
        # Getter returning the Airport city
        return self._city

    def get_country(self):
        # Getter returning the Airport country
        return self._country

    def set_city(self, city):
        # Setter that updating the Airport city
        self._city = city.strip()

    def set_country(self, country):
        # Setter updating the Airport country
        self._country = country.strip()
