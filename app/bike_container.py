class BikeContainer(object):
    """A class designed to handle bike objects. Should be used as baseclass for DockingStation, Garage and Van.

    Attributes:
        bikes = A list of bikes
        capacity = Number of bikes container can hold
    """

    DEFAULT_CAPACITY = 20

    def __init__(self, capacity=DEFAULT_CAPACITY):
        """Initializes with an empty list to hold bikes and a capacity which defaults to DEFAULT_CAPACITY"""
        self.bikes = []
        self.capacity = capacity

    def release_bike(self, status):
        """If called with argument of 'working', releases a working bike and fails if none available.

        If called with argument of 'broken', releases a broken bike and fails if none available.
        """
        if len(self.bikes) <= 0:
            raise Exception('No bikes available')
        if status == 'working':
            return_bike = next((x for x in self.bikes if x.isworking), None)
            if not return_bike:
                raise Exception('No working bikes available')
        elif status == 'broken':
            return_bike = next((x for x in self.bikes if not x.isworking), None)
            if not return_bike:
                raise Exception('No broken bikes available')
        return self.bikes.pop(self.bikes.index(return_bike))

    def remove_bike(self, target, status):
        """If called with status argument of 'working', asks for a working bike from target.

        If called with status argument of 'broken', asks for a broken bike from target.

        Fails if the container is full.
        """
        if len(self.bikes) >= self.capacity:
            raise Exception('Cannot take any more bikes')
        self.bikes.append(target.release_bike(status))
