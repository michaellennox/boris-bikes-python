import unittest
from app.docking_station import DockingStation
from app.bike import Bike

class TestUserStories(unittest.TestCase):
    def setUp(self):
        self.station = DockingStation()

    def test_docking_station_releases_a_bike(self):
        # As a person,
        # So that I can use a bike,
        # I'd like a docking station to release a bike.
        bike = self.station.release_bike()
        self.assertIsInstance(bike, Bike)

    def test_docking_station_releases_working_bike(self):
        # As a person,
        # So that I can use a good bike,
        # I'd like to see if a bike is working
        bike = self.station.release_bike()
        self.assertTrue(bike.isworking())
