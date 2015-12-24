import unittest
from app.docking_station import DockingStation
from app.bike import Bike

class TestUserStories(unittest.TestCase):
    def setUp(self):
        self.station = DockingStation()
        self.bike = Bike()
        self.broken_bike = Bike()
        self.broken_bike.report_broken()

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
        self.assertTrue(bike.isworking)

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

    def test_docking_station_should_have_a_modifiable_capacity(self):
        # As a system maintainer,
        # So that busy areas can be served more effectively,
        # I want to be able to specify a larger capacity when necessary.
        larger_station = DockingStation(50)
        self.assertEqual(larger_station.capacity, 50)

    def test_reporting_bike_broken_registers_as_not_working(self):
        # As a member of the public,
        # So that I reduce the chance of getting a broken bike in future,
        # I'd like to report a bike as broken when I return it.
        self.bike.report_broken()
        self.assertFalse(self.bike.isworking)

    def test_docking_station_does_not_release_broken_bike(self):
        # As a maintainer of the system,
        # So that I can manage broken bikes and not disappoint users,
        # I'd like docking stations not to release broken bikes.
        self.station.dock(self.broken_bike)
        with self.assertRaisesRegexp(Exception, 'No working bikes available'):
            self.station.release_bike()
