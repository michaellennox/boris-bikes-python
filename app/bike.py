class Bike(object):
    """A boris bike for use by the public

    Attributes:
        isworking: True while working, False when broken
    """

    def __init__(self):
        """Initializes working True"""
        self.isworking = True

    def report_broken(self):
        """Changes value of isworking to False"""
        self.isworking = False

    def fix(self):
        """Changes value of isworking to True"""
        self.isworking = True
