import unittest
import app.docking_station
import app.bike

class TestUserStories(unittest.TestCase):
    def setUp(self):
        self.station = DockingStation()

    def tearDown(self):
        self.station.dispose()
        self.widget = None

    def test_docking_station_releases_a_bike(self):
        # As a person,
        # So that I can use a bike,
        # I'd like a docking station to release a bike.
        bike = self.station.release_bike()
        assertIsInstance(bike, Bike())

