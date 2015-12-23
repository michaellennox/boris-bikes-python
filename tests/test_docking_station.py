import unittest
from app.docking_station import DockingStation
from mock import Mock
from app.bike import Bike

class TestDockingStation(unittest.TestCase):
    def setUp(self):
        self.station = DockingStation()
        self.bike = Mock()

    def test_release_bike_releases_a_bike(self):
        self.station.dock(self.bike)
        bike = self.station.release_bike()
        self.assertIsInstance(bike, Bike)
        
    def test_station_docks_and_stores_a_bike(self):
        self.station.dock(self.bike)
        self.assertIn(self.bike, self.station.bikes)
        
    def test_station_raises_exception_when_trying_to_release_while_empty(self):
        with self.assertRaisesRegexp(Exception, 'No bikes'):
            self.station.release_bike()

    def test_station_raises_exception_when_trying_to_dock_more_bikes_than_capacity(self):
        for _ in range(self.station.DEFAULT_CAPACITY):
            self.station.dock(self.bike)
        with self.assertRaisesRegexp(Exception, 'station full'):
            self.station.dock(self.bike)

    def test_bikes_array_initializes_empty(self):
        self.assertEqual(self.station.bikes, [])

    def test_capacity_defaults_to_default_capacity(self):
        self.assertEqual(self.station.capacity, self.station.DEFAULT_CAPACITY)
        
    def test_default_capacity_is_20(self):
        self.assertEqual(self.station.DEFAULT_CAPACITY, 20)
