import ast
import json
import unicodedata


###
# Filter out list to only US cities
###

result = []

with open("city.list.json", "r") as read_file:
    data = json.load(read_file)
    for item in data:
        if item['country'] == 'US':
            result.append(item)

with open("us_cities.list.json", "w") as write_file:
    json.dump(result, write_file)


###
# Convert population list to dict
###

pop_dict = {}
with open("city_population.txt", "r") as read_file:
    data = read_file.read().replace('\n', '')
    pop_list = ast.literal_eval(data)
    for item in pop_list[1:]:
        pop_dict[item[1].lower()] = int(item[0])


###
# Append population info to cities list
###

result = []
with open("us_cities.list.json", "r") as read_file:
    data = json.load(read_file)
    for item in data:
        search_key = unicodedata.normalize('NFKD', item['name']).encode('ascii', 'ignore').lower()
        res = [val for k, val in pop_dict.items() if search_key in k]
        item['population'] = next(iter(res), -1)
        result.append(item)


with open("us_cities_population.json", "w") as write_file:
    json.dump(result, write_file)


###
# Sort US cities by population
###

result = []
with open("us_cities_population.json", "r") as read_file:
    data = json.load(read_file)
    data.sort(key=lambda x: x['population'], reverse=True)
    result = data


with open("us_cities_population_sorted.json", "w") as write_file:
    json.dump(result, write_file)


###
# Sort US cities by population
###

result = []
with open("us_cities_population_sorted.json", "r") as read_file:
    data = json.load(read_file)
    result = data[:1000]

with open("top_1000_us_cities_sorted.json", "w") as write_file:
    json.dump(result, write_file)
