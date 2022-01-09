import datetime
import json
import requests
from os.path import exists

from typing import List
from weather_codes import *


API_KEY = '6a7c7dd6d920ce4649101c099f27cbb5'
DAILY_API_ENDPOINT = f'http://api.openweathermap.org/data/2.5/forecast/daily?appid={API_KEY}'
TOP_CITIES = "./city_data/top_1000_us_cities_sorted.json"
TOP_CITIES_FORECAST = "./weather_data/top_1000_us_cities_16_day_forecast.json"

def getCities() -> List:
  with open(TOP_CITIES, "r") as read_file:
    data = json.load(read_file)
  return data

def getWeatherForecast() -> dict:
  if exists(TOP_CITIES_FORECAST):
    with open(TOP_CITIES_FORECAST, "r") as read_file:
      data = json.load(read_file)
      return data

  cities = getCities()
  forecasts = {}

  for city in cities:
    city_id = city['id']
    response = requests.get(f'{DAILY_API_ENDPOINT}&id={city_id}&units=imperial')
    forecasts[city_id] = response.json()['list']

  with open("top_1000_us_cities_16_day_forecast.json", "w") as write_file:
    json.dump(forecasts, write_file)
  
  return forecasts


def rankTemperature(forecast, score) -> int:
  day_temp = forecast['temp']['day']

  if day_temp > 65 and day_temp <= 75:
    score = 10
  elif (day_temp > 75 and day_temp <= 85) or (day_temp > 60 and day_temp <= 65):
    score = 9.5
  elif (day_temp > 85 and day_temp <= 90):
    score = 8.0
  elif day_temp > 90:
    score = 7.0
  elif (day_temp > 50 and day_temp <= 60):
    score = 6.0
  elif (day_temp > 40 and day_temp <= 50):
    score = 5.0
  elif day_temp <= 40:
    score = 4.0
  
  return score
  

def rankWeather(forecast, score) -> int:
  for weather in forecast['weather']:
    score *= US_SUMMER_SCORES[weather['id']]
  
  return score

def rankWindSpeed(forecast, score) -> int:
  return score

def rankFeelsLike(forecast, score) -> int:
  return score

def generateWeatherScores() -> None:
  cities = getCities()
  forecasts = getWeatherForecast()

  city_scores = {}
  for city in cities:
    city_id = city['id']
    scores_per_day = {}
    for forecast in forecasts[str(city_id)]:
      score = 10
      score = rankTemperature(forecast, score)
      score = rankWeather(forecast, score)
      score = rankWindSpeed(forecast, score)
      score = rankFeelsLike(forecast, score)

      date = datetime.datetime.fromtimestamp(forecast['dt']).strftime('%Y-%m-%d')
      scores_per_day[date] = {
        'date': date,
        'score': score,
        'day_temp': forecast['temp']['day'],
        'weather': [weather['id'] for weather in forecast['weather']],
      }
    
    city_scores[city_id] = scores_per_day
  
  with open("./weather_data/top_1000_us_cities_weather_scores.json", "w") as write_file:
    json.dump(city_scores, write_file)
