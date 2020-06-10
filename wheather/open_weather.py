from urllib import request, parse
import json


class OpenWeatherRequest:
    def __init__(self, api_key, version=2.5):
        self.api_key = api_key
        self.version = version

    @property
    def url_base(self):
        return f'https://openweathermap.org/data/{self.version}/'

    def request(self):
        raise NotImplementedError()


class GetCityForecast(OpenWeatherRequest):
    def __init__(self, city_id, *args, **kwargs):
        super(GetCityForecast, self).__init__(*args, **kwargs)

        self.city_id = city_id

    def request(self):
        url = parse.urljoin(
            self.url_base,
            f'forecast/daily?id={self.city_id}&units=metric&appid={self.api_key}'
        )

        response = request.urlopen(url)

        return response


class Invoker:
    @classmethod
    def execute(self, request_object):
        if not isinstance(request_object, OpenWeatherRequest):
            raise TypeError('Request should be a OpenWeatherRequests type.')

        value = request_object.request()

        json_reponse = json.loads(
            value.read().decode(
                value.info().get_param('charset') or 'utf-8'
            )
        )

        return json_reponse

