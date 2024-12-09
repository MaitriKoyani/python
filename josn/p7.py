# Exercise 7: Convert the following JSON into Vehicle Object
import json
from collections import namedtuple
sample='{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }'
def customVehicleDecoder(dict):
    return namedtuple('X', dict.keys())(*dict.values())
vehicleobj = json.loads(sample, object_hook=customVehicleDecoder)
print(type(vehicleobj))
print(vehicleobj.name,vehicleobj.engine,vehicleobj.price)