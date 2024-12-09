# Exercise 2: Access the value of key2 from the following JSON
import json
sampleJson = """{"key1": "value1", "key2": "value2"}"""
l1=json.loads(sampleJson)
print(l1['key2'])