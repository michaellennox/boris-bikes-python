import unittest
from mock import Mock
from app.garage import Garage

class TestGarage(unittest.TestCase):
    def setUp(self):
        self.garage = Garage()
        self.van = Mock()
        self.bike = Mock(isworking = True)

    def test_garage_initializes_with_an_bikes_array(self):
        self.assertEqual(self.garage.bikes, [])

    def test_garage_remove_broken_bikes_calls_on_van(self):
        self.garage.remove_broken_bike(self.van)
        self.van.release_bike.assert_called_with('broken')

    def test_garage_returns_contained_bike_when_told_to(self):
        self.garage.bikes.append(self.bike)
        bike = self.garage.release_bike('working')
        self.assertEqual(bike, self.bike)
