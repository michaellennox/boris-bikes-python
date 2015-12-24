import unittest
from mock import Mock
from app.docking_station import DockingStation

class TestDockingStation(unittest.TestCase):
    def setUp(self):
        self.station = DockingStation()
        self.bike = Mock()

    def test_dock_stores_bike_passed_as_argument(self):
        self.station.dock(self.bike)
        self.assertIn(self.bike, self.station.bikes)

    def test_raises_exception_when_trying_to_dock_more_bikes_than_capacity(self):
        for _ in range(self.station.DEFAULT_CAPACITY):
            self.station.dock(self.bike)
        with self.assertRaisesRegexp(Exception, 'station full'):
            self.station.dock(self.bike)
