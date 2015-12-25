from bike_container import BikeContainer

class Garage(BikeContainer):
    """A garage for storing bikes at, Child of BikeContainer class.

    Bikes are repaired here."""

    def repair_bike(self, bike):
        """Calls fix on the specified bike"""
        bike.fix()
