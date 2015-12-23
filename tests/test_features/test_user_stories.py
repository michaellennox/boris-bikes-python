import unittest
from app.docking_station import DockingStation
from app.bike import Bike

class TestUserStories(unittest.TestCase):
    def setUp(self):
        self.station = DockingStation()
        self.bike = Bike()

    def test_docking_station_releases_a_bike(self):
        # As a person,
        # So that I can use a bike,
        # I'd like a docking station to release a bike.
        self.station.dock(self.bike)
        bike = self.station.release_bike()
        self.assertIsInstance(bike, Bike)

    def test_docking_station_releases_working_bike(self):
        # As a person,
        # So that I can use a good bike,
        # I'd like to see if a bike is working
        self.station.dock(self.bike)
        bike = self.station.release_bike()
        self.assertTrue(bike.isworking())

    def test_docking_station_accepts_bike(self):
        # As a member of the public
        # So I can return bikes I've hired
        # I want to dock my bike at the docking station
        self.station.dock(self.bike)

    def test_docking_station_stores_a_docked_bike(self):
        # As a member of the public
        # So I can decide whether to use the docking station
        # I want to see a bike that has been docked
        self.station.dock(self.bike)
        self.assertIn(self.bike, self.station.bikes)

    def test_docking_station_does_not_release_bike_when_empty(self):
        # As a member of the public,
        # So that I am not confused and charged unnecessarily,
        # I'd like docking stations not to release bikes when there are none available.
        with self.assertRaisesRegexp(Exception, 'No bikes'):
            self.station.release_bike()

    def test_docking_station_does_not_accept_more_bikes_than_capacity(self):
        # As a maintainer of the system,
        # So that I can control the distribution of bikes,
        # I'd like docking stations not to accept more bikes than their capacity.
        for _ in range(self.station.DEFAULT_CAPACITY):
            self.station.dock(Bike())
        with self.assertRaisesRegexp(Exception, 'Docking station full'):
            self.station.dock(self.bike)

    def test_docking_station_has_default_capacity_20(self):
        # As a system maintainer,
        # So that I can plan the distribution of bikes,
        # I want a docking station to have a default capacity of 20 bikes.
        self.assertEqual(self.station.DEFAULT_CAPACITY, 20)
