import json

data = '''{
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}'''

# Convert Python object to JSON string
json_string = json.dumps(data)

# Convert JSON string back to Python object
parsed_data = json.loads(json_string)

print(parsed_data)

nested_json = {
  "person": {
    "name": "Alice",
    "age": 25,
    "address": {
      "city": "San Francisco",
      "zipcode": "94105"
    }
  },
  "languages": ["English", "Spanish"]
}

city = nested_json["person"]["address"]["city"]
print(city)

