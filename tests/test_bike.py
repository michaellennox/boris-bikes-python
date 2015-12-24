import unittest
from app.bike import Bike

class TestBike(unittest.TestCase):
    def setUp(self):
        self.bike = Bike()

    def test_is_expected_to_be_working_on_initialization(self):
        self.assertTrue(self.bike.isworking)

    def test_is_expected_to_not_be_working_after_reporting_broken(self):
        self.bike.report_broken()
        self.assertFalse(self.bike.isworking)
