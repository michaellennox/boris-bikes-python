import unittest
from mock import Mock
from app.van import Van

class TestVan(unittest.TestCase):
    def setUp(self):
        self.van = Van()
        self.station = Mock()
        self.broken_bike = Mock(isworking = False)

    def test_van_initializes_with_an_bikes_array(self):
        self.assertEqual(self.van.bikes, [])

    def test_van_remove_broken_bikes_calls_on_docking_station(self):
        self.van.remove_broken_bike(self.station)
        self.station.release_bike.assert_called_with('broken')

    def test_van_returns_contained_bike_when_told_to(self):
        self.van.bikes.append(self.broken_bike)
        bike = self.van.release_bike('broken')
        self.assertEqual(bike, self.broken_bike)
