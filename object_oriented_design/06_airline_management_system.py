"""
Requirements collection
The requirements for the airline management system are defined below:
R1: A customer should be able to search for flights by the date, departure, and destination airport.
R2: A customer should be able to reserve tickets for available flights. Customers should also be able to book multiple flights at once.
R3: The customer should be allowed to book multiple seats for a single flight.
R4: The system should allow the customer to check flight details, such as available seats, flight schedules, and departure/arrival times.
R5: The admin should be able to add new flights. The admin should be able to update or cancel scheduled flights.
R6: An airline should be able to own multiple aircrafts. The admin should be able to add these aircrafts to the system.
R7: An airline should be able to operate its flights from different airports.
R8: The admin should be able to assign pilots and crew members to flights effectively.
R9: The customer should be able to make payments against their flight reservations.
R10: The customer should be able to cancel their previous reservations.
R11: The front desk officer should be able to reserve tickets, create itineraries,and make flight payments for the customer.
R12: The flight crew should be able to view the schedule for their assigned flights.
R13: The system should send the customer a notification whenever a reservation has been made or canceled or when there is an update for their flight.
"""
from __future__ import annotations
from abc import ABC
from datetime import datetime


class AirlineManagementSystem:
    def __init__(self):
        self.airports = []
        self.flights = []
        self.aircrafts = []
        self.customers = []
        self.admins = []
        self.front_desk_officers = []
        self.crews = []
        self.pilots = []

    def search_flights(self,
                       date,
                       departure_airport,
                       destination_airport):
        matching_flights = []
        for flight in self.flights:
            if flight.departure_time.date() == date and flight.departure_airport == departure_airport and flight.arrival_airport == destination_airport:
                matching_flights.append(flight)
        return matching_flights

    def add_flight(self, flight):
        self.flights.append(flight)

    def update_flight(self, flight):
        # Update flight details
        pass

    def cancel_flight(self, flight):
        # Cancel flight
        pass

    def add_aircraft(self, aircraft):
        self.aircrafts.append(aircraft)

    def assign_pilot(self, flight, pilot):
        # Assign pilot to flight
        pass

    def assign_crew(self, flight, crew):
        # Assign crew to flight
        pass

    def make_payment(self, customer, amount):
        # Make payment for flight reservation
        pass

    def cancel_reservation(self, customer, flight, seat_number):
        # Cancel reservation for a customer
        pass

    def reserve_ticket(self, customer, flight, seat_number):
        # Reserve ticket for a customer
        pass

    def create_itinerary(self, customer):
        # Create itinerary for a customer
        pass

    def view_schedule(self, crew, flight):
        # View schedule for a crew member
        pass

    def send_notification(self, customer, message):
        # Send notification to a customer
        pass
    

# Actors: Customer, Admin, FrontDeskOfficer, Crew, Pilot
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class Passenger(Person):
    def __init__(self, name, email, phone):
        super().__init__(name, email, phone)
        self.reservations = []
        self.account = None

    def make_reservation(self, flight, seat_number):
        if flight.reserve_seat(seat_number):
            self.reservations.append((flight, seat_number))
            return True
        return False

    def cancel_reservation(self, flight, seat_number):
        if flight.cancel_seat(seat_number):
            self.reservations.remove((flight, seat_number))
            return True
        return False

    def get_reservation_details(self):
        return [(flight.get_flight_details(), seat_number) for flight, seat_number in self.reservations]
    

class Admin(Person):
    def __init__(self, name, email, phone):
        super().__init__(name, email, phone)

    def add_flight(self, flight):
        pass

    def update_flight(self, flight):
        pass

    def cancel_flight(self, flight):
        pass

    def add_aircraft(self, aircraft):
        pass

    def assign_pilot(self, flight, pilot):
        pass

    def assign_crew(self, flight, crew):
        pass
    
class FrontDeskOfficer(Person):
    def __init__(self, name, email, phone):
        super().__init__(name, email, phone)

    def reserve_ticket(self, customer, flight, seat_number):
        return customer.make_reservation(flight, seat_number)

    def create_itinerary(self, customer):
        return customer.get_reservation_details()

    def make_payment(self, customer, amount):
        pass
    
class Crew(Person):
    def __init__(self, name, email, phone):
        super().__init__(name, email, phone)

    def view_schedule(self, flight):
        pass

class Pilot(Crew):
    def __init__(self, name, email, phone):
        super().__init__(name, email, phone)

    def view_schedule(self, flight):
        pass


# Components: Flight, Airplane, Airport
class Flight:
    def __init__(self,
                 flight_number: str,
                 departure_airport: Airport,
                 arrival_airport: Airport,
                 departure_time: datetime,
                 arrival_time: datetime,
                 aircraft: Aircraft
                 ) -> None:
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.aircraft = aircraft
        self.seats = aircraft.seats
        self.available_seats = aircraft.seats

    def get_flight_details(self):
        return {
            "flight_number": self.flight_number,
            "departure_airport": self.departure_airport,
            "arrival_airport": self.arrival_airport,
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time,
            "aircraft": self.aircraft,
            "seats": self.seats,
            "available_seats": self.available_seats
        }

    def reserve_seat(self, seat_number):
        if self.available_seats > 0:
            self.available_seats -= 1
            return True
        return False

    def cancel_seat(self, seat_number):
        if self.available_seats < self.seats:
            self.available_seats += 1
            return True
        return False
    

class Airport:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_airport_details(self):
        return {
            "name": self.name,
            "code": self.code
        }  

    
class Aircraft:
    def __init__(self, aircraft_number, model, seats):
        self.aircraft_number = aircraft_number
        self.model = model
        self.seats = seats

    def get_aircraft_details(self):
        return {
            "aircraft_number": self.aircraft_number,
            "model": self.model,
            "seats": self.seats
        }
        


class Payment:
    def __init__(self, amount, date, status):
        self.amount = amount
        self.date = date
        self.status = status

    def make_payment(self):
        pass

    def get_payment_status(self):
        return self.status
    
class CashPayment(Payment):
    def __init__(self, amount, date, status):
        super().__init__(amount, date, status)

    def make_payment(self):
        pass


class Notification:
    def __init__(self, message):
        self.message = message

    def send_notification(self):
        pass
    

class Notification(ABC):
    def __init__(self, notification_id, created_on, content) -> None:
        self.notification_id = notification_id
        self.created_on = created_on
        self.content = content
    
    @abstractmethod
    def send_notification(self, account):
        pass
    
    
class SMSNotification(Notification):
    def __init__(self, notification_id, created_on, content) -> None:
        super().__init__(notification_id, created_on, content)
        
    def send_notification(self, account):
        pass
    
    
class EmailNotification(Notification):
    def __init__(self, notification_id, created_on, content, email) -> None:
        self.email = email
        super().__init__(notification_id, created_on, content)
        
    def send_notification(self, account):
        pass
    
class Airline:
    __instance = None
    def __new__(cls, name):
        if cls.__instance is None:
            cls.__instance = super(Airline, cls).__new__(cls)
            cls.__instance.name = name
        return cls.__instance 
    
if __name__ == '__main__':
    airline1 = Airline("Lufthansa")
    print(id(airline1))
    print(airline1.name)
    
    airline2 = Airline("EgyptAir")
    print(id(airline2))
    print(airline2.name)
    
    # print(airline1.name)
    