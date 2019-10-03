import unittest
from unittest.mock import patch, MagicMock

import weather_checker_2


class WeatherCheckerUnitTests(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.requests_patcher = patch("weather_checker_2.requests")
        self.mock_requests = self.requests_patcher.start()

    def tearDown(self) -> None:
        super().tearDown()
        patch.stopall()

    @patch("weather_checker_2.WeatherChecker.update")
    def test_initialized_properly_with_defaults(self, update_mock: MagicMock):
        checker = weather_checker_2.WeatherChecker()
        self.assertEqual(checker.temperature, 0.0, msg="Wrong temp when initialized")

    @patch("weather_checker_2.WeatherChecker.update")
    def test_initialized_properly_with_non_defaults(self, update_mock: MagicMock):
        checker = weather_checker_2.WeatherChecker(latitude=123, longitude=321)
        self.assertEqual(123, checker.latitude)
        self.assertEqual(321, checker.longitude)

    @patch("weather_checker_2.json.loads")
    def test_update(self, json_loader_mock: MagicMock):
        expected_dict = {"weather":
                             [{"description": 'test_description'}],
                         "main":
                             {"temp": 420,
                              "pressure": 123},
                         "name": "test_city"}

        json_loader_mock.return_value = expected_dict
        checker = weather_checker_2.WeatherChecker()
        self.assertEqual("test_city", checker.location, msg="Wrong test location")
        self.assertEqual(420, checker.temperature)
        self.assertEqual("test_description", checker.condition, msg="Wrong description")
