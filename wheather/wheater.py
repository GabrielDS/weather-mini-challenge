from datetime import datetime
import logging

from open_weather import GetCityForecast, Invoker

KEY = '439d4b804bc8187953eb36d2a8c26a02'
CITY_ID = 3451328
MIN_HUMIDITY = 70

def list_to_string(words_list):

    if len(words_list) > 1:

        last_word = words_list[-1]

        words = ', '.join(words_list[:-1])

        string_words = f"{words} and {last_word}."

        return string_words

    elif len(words_list) == 1:

        return words_list[0]

    return ''

def get_days_greater_humidity(response, min_humidity):
    days_forecast = response['list'][1:6]
    list_of_days = []

    for day in days_forecast:

        if day['humidity'] > min_humidity:

            timestamp = day['dt']

            day_name = datetime.utcfromtimestamp(timestamp).strftime('%A')

            list_of_days.append(day_name)

    return list_of_days

def main():
    request = GetCityForecast(
        api_key=KEY,
        city_id=CITY_ID,
    )

    response_weather = Invoker.execute(request)

    days = get_days_greater_humidity(
        response=response_weather,
        min_humidity=MIN_HUMIDITY
    )

    days_string = list_to_string(days)

    print(f'You should take an umbrella in these days: {days_string}')

if __name__ == '__main__':
    main()