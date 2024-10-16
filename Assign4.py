# This file is meant to be the core of the program from which the Airport and Flight objects should be created

from Flight import *
from Airport import *
import csv

allAirports = []
allFlights = dict()


def loadData(airportFile, flightFile):
    try:
        airport_data = open(airportFile, "r", encoding='utf-8')
        airport_read = csv.reader(airport_data,
                                  delimiter=",")  # Read in all the data from the airport file of the given name
        flight_data = open(flightFile, "r", encoding='utf-8')
        flight_read = csv.reader(flight_data,
                                 delimiter=",")  # Read in all the data from the flight file of the given name

        for line in airport_read:
            # Extracting the information from each line and creating an Airport object for each. Removing any whitespace from the outside of each portion of the line
            airport_data = Airport(line[0].strip(), line[2].strip(), line[1].strip())
            allAirports.append(airport_data)

        for line in flight_read:
            # Extracting the information from each line and creating a Flight object for each. Removing any whitespace from the outside of each portion of the line
            flight = str(line[0].strip())
            origin = str(line[1].strip())
            destination = str(line[2].strip())
            origin_code = getAirportByCode(origin)
            destination_code = getAirportByCode(destination)
            temp = Flight(flight, origin_code, destination_code)

            # adding the object to the allFlights dictionary
            if origin in allFlights:
                allFlights[origin].append(temp)
            else:
                allFlights[origin] = [temp]

    except:
        return False
    return True


def getAirportByCode(code):
    # Return the Airport object that has the parameter code
    for airport in allAirports:
        if str(code) == airport.getCode():
            return airport
    return -1   # if there is no Airport found for the given code, then return -1.


def findAllCityFlights(city):
    # Return a list that contains all Flight objects that involve the given city either as the origin or the destination
    list_of_flights = []
    for code in allFlights:
        airport = getAirportByCode(code)
        airport_city = airport.getCity()
        if city == airport_city:
            list_of_flights.extend(allFlights[code])
        else:
            flight = allFlights[code]
            for i in flight:
                destination = i.getDestination().getCity()
                if city == destination:
                    list_of_flights.append(i)
    return list_of_flights


def findAllCountryFlights(country):
    # Return a list that contains all Flight objects that involve the given country either as the origin or the destination (or both)
    list_of_flights = []
    for i in allFlights:
        airport = getAirportByCode(i)
        airport = airport.getCountry()
        if country == airport:
            list_of_flights.extend(allFlights[i])
        else:
            flight = allFlights[i]
            for j in flight:
                destination = j.getDestination().getCountry()
                if country == destination:
                    list_of_flights.append(j)
    return list_of_flights


def findFlightBetween(origAirport, destAirport):
    # Check if there is a direct flight from origAirport to destAirport. If so, return a string of the given format
    origAirportCode = origAirport.getCode()
    destAirportCode = destAirport.getCode()
    for i in allFlights[origAirportCode]:
        if i.getDestination().getCode() is destAirportCode:
            return f"Direct Flight: {origAirportCode} to {destAirportCode}"
    origin_x = set()
    destination_x = set()
    for flight in allFlights:
        for i in allFlights[flight]:
            if flight == origAirportCode:
                origin_x.add(i.getDestination().getCode())
            else:
                if i.getDestination().getCode() == destAirportCode:
                    destination_x.add(i.getOrigin().getCode())
    connect = origin_x & destination_x
    if len(connect) != 0:
        return connect
    return -1   # If there is no direct flight AND no single-hop connecting flights from origAirport to destAirport, then just return -1.


def findReturnFlight(firstFlight):
    # Take the given Flight object and look for the Flight object representing the return flight from that given flight
    flightA_origin = firstFlight.getOrigin().getCode()
    flightA_destination = firstFlight.getDestination().getCode()
    list_of_flights = allFlights[flightA_destination]

    for i in list_of_flights:
        flightB_destination = i.getDestination().getCode()
        if flightB_destination == flightA_origin:
            return i    # return flight object that departs from origin B and arrives in destination A
    return -1   # If there is no such Flight object that goes in the opposite direction as firstFlight, just return -1.
