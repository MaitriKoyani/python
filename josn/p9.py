# Exercise 9: Parse the following JSON to get all the values of a key ‘name’ within an array
import json
sample="""[ { "id":1,  "name":"name1", "color":["red","green"]},{ "id":2,"name":"name2","color":[ "pink","yellow"]}]"""
l1=json.loads(sample)
l2=[]
for i in l1:
    for j,k in i.items():
        if j=='name':
            l2.append(k)
print(l2)
# dataList = [item.get('name') for item in l1]
# print(dataList)