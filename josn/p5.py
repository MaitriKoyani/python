# Exercise 5: Access the nested key ‘salary’ from the following JSON
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
l1=json.loads(sampleJson)
print(l1['company']['employee']['payble']['salary'])