import unittest
from app.docking_station import DockingStation
from app.bike import Bike

class TestDockingStation(unittest.TestCase):
    def setUp(self):
        self.station = DockingStation()

    def test_release_bike_releases_a_bike(self):
        bike = self.station.release_bike()
        self.assertIsInstance(bike, Bike)
        
    def test_station_accepts_a_bike(self):
        self.station.dock(Bike())
