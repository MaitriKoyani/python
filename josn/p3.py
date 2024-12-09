# Exercise 3: PrettyPrint following JSON data
# PrettyPrint following JSON data with indent level 2 and key-value separators should be (",", " = ").
import json
sampleJson = {"key1": "value1", "key2": "value2","key3":{"key1": "value1", "key2": "value2"}},{"key1": "value1", "key2": "value2","key3":{"key1": "value1", "key2": "value2"}}
print(json.dumps(sampleJson, indent=2, separators=(" . ", " = ")))
