import unittest
from mock import Mock
from app.bike_container import BikeContainer

class TestBikeContainer(unittest.TestCase):
    def setUp(self):
        self.bike_container = BikeContainer()
        self.filled_container = BikeContainer()
        self.bike = Mock(isworking = True)
        self.broken_bike = Mock(isworking = False)
        self.filled_container.bikes.extend((self.bike, self.broken_bike))

    def test_bikes_array_initializes_empty(self):
        self.assertEqual(self.bike_container.bikes, [])

    def test_capacity_defaults_to_default_capacity(self):
        self.assertEqual(self.bike_container.capacity, self.bike_container.DEFAULT_CAPACITY)

    def test_default_capacity_is_20(self):
        self.assertEqual(self.bike_container.DEFAULT_CAPACITY, 20)

    def test_capacity_is_modifiable(self):
        larger_container = BikeContainer(50)
        self.assertEqual(larger_container.capacity, 50)

    def test_release_bike_with_working_releases_a_working_bike(self):
        bike = self.filled_container.release_bike('working')
        self.assertEqual(bike, self.bike)

    def test_release_bike_with_broken_releases_a_broken_bike(self):
        bike = self.filled_container.release_bike('broken')
        self.assertEqual(bike, self.broken_bike)

    def test_release_bike_removes_it_from_bikes(self):
        self.filled_container.release_bike('working')
        self.assertNotIn(self.bike, self.filled_container.bikes)

    def test_raises_exception_when_trying_to_release_bike_while_empty(self):
        with self.assertRaisesRegexp(Exception, 'No bikes'):
            self.bike_container.release_bike('working')

    def test_raises_exception_when_trying_to_release_broken_while_none(self):
        self.filled_container.release_bike('broken')
        with self.assertRaisesRegexp(Exception, 'No broken bikes'):
            self.filled_container.release_bike('broken')

    def test_raises_exception_when_trying_to_release_broken_while_none(self):
        self.filled_container.release_bike('working')
        with self.assertRaisesRegexp(Exception, 'No working bikes'):
            self.filled_container.release_bike('working')

    def test_remove_bike_working_removes_bike_from_another_container(self):
        self.bike_container.remove_bike(self.filled_container, 'working')
        self.assertIn(self.bike, self.bike_container.bikes)

    def test_remove_bike_broken_removes_bike_from_another_container(self):
        self.bike_container.remove_bike(self.filled_container, 'broken')
        self.assertIn(self.broken_bike, self.bike_container.bikes)

    def test_remove_bike_raises_exception_when_container_is_full(self):
        for _ in range(self.bike_container.DEFAULT_CAPACITY):
            self.bike_container.bikes.append(Mock())
        with self.assertRaisesRegexp(Exception, 'Cannot take any more bikes'):
            self.bike_container.remove_bike(self.filled_container, 'working')
