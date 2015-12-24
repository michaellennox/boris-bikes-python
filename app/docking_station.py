from bike_container import BikeContainer

class DockingStation(BikeContainer):
    """A docking station for storing bikes at, Child of BikeContainer class

    Attributes:
        bikes: a container for Bike objects
        capacity: the number of bikes able to be held by the station
    """

    def dock(self, bike):
        """User docks a bike at the station, fails if station full"""
        if len(self.bikes) >= self.capacity:
            raise Exception('Docking station full')
        self.bikes.append(bike)
