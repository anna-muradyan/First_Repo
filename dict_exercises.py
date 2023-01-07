#1 two lists turn to a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10,20,30]
dict = {}
for i in range(len(keys)):
    dict.update({keys[i]: values[i]})
print(dict)

#2 merge two dictionaries

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {**dict1, **dict2}

#3 remove certain keys
dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

#4 Keys to remove
keys = ["name", "salary"]
for i in keys:
    dict.pop(i)
print(dict)

#5 print certain value

dict = {
    "class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}
print(dict["class"]["student"]["marks"]["history"])

#6 Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
res = dict.fromkeys(employees,defaults)
print(res)


#6  Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
dict = {}
keys = ["name", "salary"]
for i in keys:  
    dict.update({i:sample_dict[i]})
print(dict)

 #7Check if a value exists in a dictionary

sample_dict = {'a': 100, 'b': 200, 'c': 300}
values = sample_dict.values()
if 200 in values:
    print("200 present in a dict")


dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}


dict["location"] = dict.pop("city")
print(dict)
