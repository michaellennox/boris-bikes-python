class Van(object):
    """A van for transporting bikes between docking station and garage

    Attributes:
        bikes: container for bikes
    """

    def __init__(self):
        """Initializes with an empty bikes container"""
        self.bikes = []

    def remove_broken_bike(self, station):
        """Asks the station passed as argument for a broken bike"""
        self.bikes.append(station.release_bike('broken'))

    def release_bike(self, status='broken'):
        """Returns a broken bike"""
        return self.bikes.pop()
