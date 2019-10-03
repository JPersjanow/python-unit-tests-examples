import json
import requests
from requests.adapters import HTTPAdapter


class WeatherChecker(object):
    def __init__(self, latitude: float = 54.5188898, longitude: float = 18.5305409) -> None:
        """
        Weather checker constructor.
        latitude: float number, latitude of the location, defaulted to Gdynia
        longitude: float number, longitude of the location, defaulted to Gdynia
        """
        self.longitude = longitude
        self.latitude = latitude

        self.location = ""
        self.condition = ""
        self.temperature = 0.0  # type: float
        self.pressure = 0  # type: int
        self.update()

    def update(self) -> None:
        session = requests.Session()
        adapter = HTTPAdapter()
        session.mount('https://', adapter)
        response = session.get(f"https://fcc-weather-api.glitch.me/api/current?lat={self.latitude}&lon={self.longitude}")
        weather_json = json.loads(response.content.decode())
        self.location = weather_json["name"]
        self.condition = weather_json["weather"][0]["description"]
        self.temperature = weather_json["main"]["temp"]
        self.pressure = weather_json["main"]["pressure"]

    def present(self) -> None:
        print(f"Location:   \t{self.location}")
        print(f"Condition:  \t{self.condition}")
        print(f"Temperature:\t{self.temperature}")
        print(f"Pressure:   \t{self.pressure}")


if __name__ == '__main__':
    weather_obj = WeatherChecker()
    weather_obj.present()
