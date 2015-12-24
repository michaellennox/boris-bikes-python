class Garage(object):

    def __init__(self):
        self.bikes = []

    def remove_broken_bike(self, van):
        """Asks the van passed as argument for a broken bike"""
        self.bikes.append(van.release_bike('broken'))

    def release_bike(self, status='working'):
        """Returns a working bike"""
        return self.bikes.pop()
