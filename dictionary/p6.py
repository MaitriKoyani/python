# Exercise 6: Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for key in keys:
    if key in sample_dict.keys():
        del sample_dict[key]
print(sample_dict)