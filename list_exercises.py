list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)
#list1[::-1]

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []
print(list3)
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])
print(list3)
list3 = [i+j for i,j in zip(list1,list2)]
print(list3)

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# x = list(zip(list1,list2))
# print(x)

numbers = [1, 2, 3, 4, 5, 6, 7]
list = []
list = [i**2 for i in numbers]
for i in numbers:
    list.append(i**2)
print(list)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []
for i in list1:
    for j in list2:
        list3.append(i+j)
[i+j for i in list1 for j in list2 ]

print(list3)

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i,j in zip(list1, list2[::-1]):
    print(i,j)

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list2 = list(filter(None,list1))
# print(list1)

#
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(["h", "i", "j"])
print(list1)

#
list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] = 200
print(list1)

list1 = [5, 20, 15, 20, 25, 50, 20]
while 20 in list1:
    list1.remove(20)
    
print(list1)
