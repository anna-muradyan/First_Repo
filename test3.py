dict1 = {"zero":0,"two":2, "four":4, "six": 6, "eight":8,"ten":10}
dict2 = {"one":1,"three":3,"five":5,"seven":7, "nine":9}
dict3 = {}
dict1_keys = dict1.keys()
dict2_keys = dict2.keys()
smallest_size = min(len(dict1_keys), len(dict2_keys))
for index in range(smallest_size):
   key1 = dict1_keys[index]
   key2 = dict2_keys[index]
   dict3[key1] = dict1[key1]
   dict3[key2] = dict2[key2]
print(dict3)



dict1_keys = list(dict1.keys())
dict2_keys = list(dict2.keys())

s1 = len(dict1_keys)
s2 = len(dict2_keys)

max_size = max(s1, s2)

dict3 = {}
for index in range(max_size):
    
    if(index < s1):
        key1 = dict1_keys[index]
        dict3[key1] = dict1[key1]
    if(index < s2):
        key2 = dict2_keys[index]
        dict3[key2] = dict2[key2]

print(dict3)