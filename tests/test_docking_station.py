import unittest
from app.docking_station import DockingStation
from mock import Mock
from app.bike import Bike

class TestDockingStation(unittest.TestCase):
    def setUp(self):
        self.station = DockingStation()
        self.bike = Mock()

    def test_release_bike_releases_a_bike(self):
        bike = self.station.release_bike()
        self.assertIsInstance(bike, Bike)
        
    def test_station_docks_and_stores_a_bike(self):
        self.station.dock(self.bike)
        self.assertEqual(self.station.bikes, self.bike)
