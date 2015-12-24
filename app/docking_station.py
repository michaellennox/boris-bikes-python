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

    def release_bike(self, status='working'):
        """If called with no additional argument, releases a working bike and fails if none available.

        If called with an additional argument, releases a broken bike and fails if none available.
        """
        if len(self.bikes) <= 0:
            raise Exception('No bikes available')
        if status == 'working':
            return_bike = next((x for x in self.bikes if x.isworking), None)
            if not return_bike:
                raise Exception('No working bikes available')
        else:
            return_bike = next((x for x in self.bikes if not x.isworking), None)
            if not return_bike:
                raise Exception('No broken bikes available')
        return self.bikes.pop(self.bikes.index(return_bike))

    def dock(self, bike):
        """Docks a bike at the station, fails if station full"""
        if len(self.bikes) >= self.capacity:
            raise Exception('Docking station full')
        self.bikes.append(bike)

    def remove_working_bike(self, van):
        """Asks the van passed as argument for a working bike"""
        self.bikes.append(van.release_bike('working'))
