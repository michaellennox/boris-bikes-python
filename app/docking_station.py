class DockingStation(object):
    """A docking station for storing bikes at

    Attributes:
        bikes: a container for Bike objects
        capacity: the number of bikes able to be held by the station
    """

    DEFAULT_CAPACITY = 20 # A docking station's default capacity is 20 bikes

    def __init__(self, capacity=DEFAULT_CAPACITY):
        """Initializes with no bikes in station, capacity is equal to DEFAULT_CAPACITY"""
        self.bikes = []
        self.capacity = capacity

    def release_bike(self):
        """Returns a Bike, fails if station empty or if no working bikes"""
        if len(self.bikes) <= 0:
            raise Exception('No bikes available')
        working_bike = next((x for x in self.bikes if x.isworking), None)
        if not working_bike:
            raise Exception('No working bikes available')
        return self.bikes.pop(self.bikes.index(working_bike))

    def dock(self, bike):
        """Docks a bike at the station, fails if station full"""
        if len(self.bikes) >= self.capacity:
            raise Exception('Docking station full')
        self.bikes.append(bike)
