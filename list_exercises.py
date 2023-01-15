#Reverse a list

list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)
print(list1[::-1])


#2 Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])
print(list3)

list3  = [i+j for i, j in zip(list1,list2)]
print(list3)

#3 Turn every item of a list into its square
numbers = [1, 2, 3, 4, 5, 6, 7]
list1 = []
for i in numbers:
    list1.append(i**2)
print(list1)

#4 Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 =[i+j for i in list1 for j in list2]
print(list3)

#5 Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i, j in zip(list1, list2[::-1]):
    print(i, j)

#6 Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
a = list(filter(None,list1))
print(a)

#7 Add new item to list after a specified item
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#8 Extend nested list by adding the sublist

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(["h", "i", "j"])
print(list1)

#9 You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item
list1 = [5, 10, 15, 20, 25, 50, 20]
a = list1.index(20)
list1[a] = 200
print(list1)

#10 Given a Python list, write a program to remove all occurrences of item 20.
list1 = [5, 10, 15, 20, 25, 50, 20]
while 20 in list1:
    list1.remove(20)
print(list1)

