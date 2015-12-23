from bike import Bike

class DockingStation(object):
    """A docking station for storing bikes at"""

    def release_bike(self):
        """Returns a Bike"""
        return Bike()

    def dock(self, bike):
        """Docks a bike at the station"""
        pass
