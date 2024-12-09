# Exercise 4: Sort JSON keys in and write them into a file
import json
sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
with open('json.txt','w') as fo:
    json.dump(sampleJson, fo,indent=3, separators=(', ',' = '), sort_keys=True)
    print("done writing.")