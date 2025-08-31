import unittest
from src.navigation.navigator import Navigator

class TestNavigator(unittest.TestCase):

    def setUp(self):
        self.navigator = Navigator()

    def test_plan_route(self):
        start = (0, 0)
        end = (10, 10)
        route = self.navigator.plan_route(start, end)
        self.assertIsNotNone(route)
        self.assertEqual(route[0], start)
        self.assertEqual(route[-1], end)

    def test_execute_navigation(self):
        route = [(0, 0), (1, 1), (2, 2)]
        result = self.navigator.execute_navigation(route)
        self.assertTrue(result)

    def test_invalid_route(self):
        with self.assertRaises(ValueError):
            self.navigator.execute_navigation([])

if __name__ == '__main__':
    unittest.main()