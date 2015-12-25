import unittest
from mock import Mock
from app.garage import Garage

class TestGarage(unittest.TestCase):
    def setUp(self):
        self.garage = Garage()
        self.bike = Mock()

    def test_repair_bike_fixes_broken_bikes(self):
        self.garage.repair_bike(self.bike)
        self.bike.fix.assert_called_with()
