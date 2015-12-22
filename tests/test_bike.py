import unittest
from app.bike import Bike

class TestBike(unittest.TestCase):
    def setUp(self):
        self.bike = Bike()

    def test_is_expected_to_be_working(self):
        self.assertTrue(self.bike.isworking())
