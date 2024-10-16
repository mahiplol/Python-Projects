class Airport:
    def __init__(self, code, city, country):
        # initializing the instance variables _code, _city, and _country based on the corresponding parameters in the constructor
        self._code = code
        self._city = city
        self._country = country

    def __repr__(self):
        # returns the representation of this Airport in the following format: code (city, country)
        return str(self._code) + "(" + self._city + "," + self._country + ")"

    def getCode(self):
        # Getter that returns the Airport code
        return self._code

    def getCity(self):
        # Getter that returns the Airport city
        return self._city

    def getCountry(self):
        # Getter that returns the Airport country
        return self._country

    def setCity(self, city):
        # Setter that sets (updates) the Airport city
        self._city = city

    def setCountry(self, country):
        # Setter that sets (updates) the Airport country
        self._country = country
