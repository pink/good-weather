THUNDERSTORM_CODES = {
  200: {
    "condition": "Thunderstorm",
    "detail": "thunderstorm with light rain",
  },
  201: {
    "condition": "Thunderstorm",
    "detail": "thunderstorm with rain",
  },
  202: {
    "condition": "Thunderstorm",
    "detail": "thunderstorm with heavy rain",
  },
  210: {
    "condition": "Thunderstorm",
    "detail": "light thunderstorm",
  },
  211: {
    "condition": "Thunderstorm",
    "detail": "thunderstorm",
  },
  212: {
    "condition": "Thunderstorm",
    "detail": "heavy thunderstorm",
  },
  221: {
    "condition": "Thunderstorm",
    "detail": "ragged thunderstorm",
  },
  230: {
    "condition": "Thunderstorm",
    "detail": "thunderstorm with light drizzle",
  },
  231: {
    "condition": "Thunderstorm",
    "detail": "thunderstorm with drizzle",
  },
  232: {
    "condition": "Thunderstorm",
    "detail": "thunderstorm with heavy drizzle",
  },
}

DRIZZLE_CODES = {
  300: {
    "condition": "Drizzle",
    "detail": "light intensity drizzle",
  },
  301: {
    "condition": "Drizzle",
    "detail": "drizzle",
  },
  302: {
    "condition": "Drizzle",
    "detail": "heavy intensity drizzle",
  },
  310: {
    "condition": "Drizzle",
    "detail": "light intensity drizzle rain",
  },
  311: {
    "condition": "Drizzle",
    "detail": "drizzle rain",
  },
  312: {
    "condition": "Drizzle",
    "detail": "heavy intensity drizzle rain",
  },
  313: {
    "condition": "Drizzle",
    "detail": "shower rain and drizzle",
  },
  314: {
    "condition": "Drizzle",
    "detail": "heavy shower rain and drizzle",
  },
  321: {
    "condition": "Drizzle",
    "detail": "shower drizzle",
  },
}

RAIN_CODES = {
  500: {
    "condition": "Rain",
    "detail": "light rain",
  },
  501: {
    "condition": "Rain",
    "detail": "moderate rain",
  },
  502: {
    "condition": "Rain",
    "detail": "heavy intensity rain",
  },
  503: {
    "condition": "Rain",
    "detail": "very heavy rain",
  },
  504: {
    "condition": "Rain",
    "detail": "extreme rain",
  },
  511: {
    "condition": "Rain",
    "detail": "freezing rain",
  },
  520: {
    "condition": "Rain",
    "detail": "light intensity shower rain",
  },
  521: {
    "condition": "Rain",
    "detail": "shower rain",
  },
  522: {
    "condition": "Rain",
    "detail": "heavy intensity shower rain",
  },
  531: {
    "condition": "Rain",
    "detail": "ragged shower rain",
  },
}

SNOW_CODES = {
  600: {
    "condition": "Snow",
    "detail": "light snow",
  },
  601: {
    "condition": "Snow",
    "detail": "snow",
  },
  602: {
    "condition": "Snow",
    "detail": "Heavy snow",
  },
  611: {
    "condition": "Snow",
    "detail": "Sleet",
  },
  612: {
    "condition": "Snow",
    "detail": "Light shower sleet",
  },
  613: {
    "condition": "Snow",
    "detail": "Shower sleet",
  },
  615: {
    "condition": "Snow",
    "detail": "Light rain and snow",
  },
  616: {
    "condition": "Snow",
    "detail": "Rain and snow",
  },
  620: {
    "condition": "Snow",
    "detail": "Light shower snow",
  },
  621: {
    "condition": "Snow",
    "detail": "Shower snow",
  },
  622: {
    "condition": "Snow",
    "detail": "Heavy shower snow",
  },
}

ATMOSPHERE_CODES = {
  701: {
    "condition": "Mist",
    "detail": "mist",
  },
  711: {
    "condition": "Smoke",
    "detail": "smoke",
  },
  721: {
    "condition": "Haze",
    "detail": "haze",
  },
  731: {
    "condition": "Dust",
    "detail": "sand/dust whirls",
  },
  741: {
    "condition": "Fog",
    "detail": "fog",
  },
  751: {
    "condition": "Sand",
    "detail": "sand",
  },
  761: {
    "condition": "Dust",
    "detail": "dust",
  },
  762: {
    "condition": "Ash",
    "detail": "volcanic ash",
  },
  771: {
    "condition": "Squall",
    "detail": "squalls",
  },
  781: {
    "condition": "Tornado",
    "detail": "tornado",
  },
}

CLEAR_CODES = {
  800: {
    "condition": "Clear",
    "detail": "clear sky",
  },
}

CLOUD_CODES = {
  801: {
    "condition": "Clouds",
    "detail": "few clouds: 11-25%",
  },
  802: {
    "condition": "Clouds",
    "detail": "scattered clouds: 25-50%",
  },
  803: {
    "condition": "Clouds",
    "detail": "broken clouds: 51-84%",
  },
  804: {
    "condition": "Clouds",
    "detail": "overcast clouds: 85-100%",
  },
}

US_SUMMER_SCORES = {
  200: 0.75,
  201: 0.2,
  202: 0.2,
  210: 0.75,
  211: 0.75,
  212: 0.4,
  221: 0.4,
  230: 0.75,
  231: 0.75,
  232: 0.2,
  300: 0.75,
  301: 0.75,
  302: 0.75,
  310: 0.75,
  311: 0.75,
  312: 0.6,
  313: 0.6,
  314: 0.6,
  321: 0.6,
  500: 0.65,
  501: 0.2,
  502: 0.2,
  503: 0.2,
  504: 0.2,
  511: 0.2,
  520: 0.2,
  521: 0.2,
  522: 0.2,
  531: 0.2,
  600: 0.2,
  601: 0.2,
  602: 0.2,
  611: 0.2,
  612: 0.2,
  613: 0.2,
  615: 0.2,
  616: 0.2,
  620: 0.2,
  621: 0.2,
  622: 0.2,
  701: 0.65,
  711: 0.5,
  721: 0.5,
  731: 0.5,
  741: 0.65,
  751: 0.25,
  761: 0.25,
  762: 0,
  771: 0,
  781: 0,
  800: 1,
  801: 1,
  802: 1,
  803: 0.95,
  804: 0.85
}