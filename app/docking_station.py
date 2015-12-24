from bike_container import BikeContainer

class DockingStation(BikeContainer):
    """A docking station for storing bikes at, Child of BikeContainer class"""

    def dock(self, bike):
        """User docks a bike at the station, fails if station full"""
        if len(self.bikes) >= self.capacity:
            raise Exception('Docking station full')
        self.bikes.append(bike)
