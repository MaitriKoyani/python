# Exercise 8: Check whether following json is valid or invalid. If Invalid correct it
import json

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True
invaliddata='{ "company":{ "employee":{ "name":"emma","payble":{ "salary":7000"bonus":800}}}}'
isvalid=validateJSON(invaliddata)
print('given data is valid?',isvalid)
validdata='{ "company":{ "employee":{ "name":"emma","payble":{ "salary":7000,"bonus":800}}}}'
isvalid=validateJSON(validdata)
print('given data is valid?',isvalid)
