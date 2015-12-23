from bike import Bike

class DockingStation(object):
    """A docking station for storing bikes at
    
    Attributes:
        bikes: a container for Bike objects
    """

    def __init__(self):
        """Initializes with no bikes in station"""
        self.bikes = None

    def release_bike(self):
        """Returns a Bike, fails if station empty"""
        if self.bikes == None:
            raise Exception('No bikes available')
        return Bike()

    def dock(self, bike):
        """Docks a bike at the station, fails if station full"""
        if self.bikes:
            raise Exception('Docking station full')
        self.bikes = bike

