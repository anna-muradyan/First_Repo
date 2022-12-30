myDict = {"aram":51, "b":15, "c":20,"d":5,"e":5}
# dict_1 = {}  # dict()

# values = list(myDict.values())
# for key, values in myDict.items():
#     if str(values)[0] != "5":
#         dict_1[key] = values

# print(myDict)
# print(dict_1)


# for key in myDict.copy():
#     values = str(myDict[key])
#     print(values)
#     if values[0] == "5":
#         myDict.pop(key)

# print(myDict)



#Տրված է բառարան։ Ստանալ ցուցակ բառարանի այն բանալիներից, որոնց արժեքները եռանիշ թվեր են։
# myDict = {"aram":513, "b":151, "c":201,"d":51,"e":5125}
# list1 = []
# for key in myDict.copy():
#  values = str(myDict[key])
#  if len(values) == 3:
#   list1.append(values)
# print(list1)

#Ստանալ ցուցակ, որը կազված կլինի list1-ի կենտ ինդեքսով էլեմենտներից և list2-ի զույգ ինդեքսով էլեմենտներից։
list1 = [0, 21, 15, 5, 8, 35, 48, 18, 58, 25]
list2 = [0, 1, 8, 15, 25, 68, 48, 77, 88, 15, 38]
new_list = []
# for i in list2:
#     index = list2.index(i)
#     if index % 2 == 0:
#         new_list.append(i)
# for i in list1:
#     index = list1.index(i)
#     if index % 2 != 0:
#         new_list.append(i)
# print(new_list)

#another method 
# list1 = [0, 21, 15, 5, 8, 35, 48, 18, 58, 25]
# list2 = [0, 1, 8, 15, 25, 68, 48, 77, 88, 15, 38]
# list2_even = list2[::2]
# list1_odd = list1[1::2]
# print(list2_even + list1_odd)

#4) Տրված է բառարան, որի բանալիները մարդկանց անուններն են, իսկ արժեքները՝ նրանց ծննդյան տարեթվերը։ Ստանալ ցուցակ այն մարդկանց անուններից կազմված, որոնց տարիքը մեծ է 18-ից

myDict = {"aram":2015, "babken":2001, "anna":2000,"david":2020,"ervand":1978}
from datetime import date
today = date.today()
year = today.year
for key in myDict.copy():
    age = year - myDict[key]
    if age < 18:
        myDict.pop(key)
print(myDict)



#5)Տրված է բառարան։ Բառարանից  հեռացնել այն զույգը, որոնց արժեքների մեջ կա 0։
# myDict = {"aram":2015, "babken":2001, "anna":1995,"david":2020,"ervand":1978}
# for key in myDict.copy():
#     values = str(myDict[key])  
#     if "0" in values:
#         myDict.pop(key)
# print(myDict)
        
#6) Տրված է dict1 և dict2 բառարանները։ Ստանալ dict3 բառարանը որը կազմված է dict1-ի և dict2-ի զույգերից (մեկումեջ դասավորված)
myDict1 = {"karen":2000, "vartan":2001, "anna":1995,"david":2020,"ervand":1978}
myDict2 = {"aram":2015, "babken":2001, "hanna":2000,"astxik":1973,"hambo":1968}
myDict3 = {}
for i in (myDict1, myDict2):
    myDict3.update(i)
print(myDict3)
for i, j in myDict1.items():
    print(i,j)
print(myDict3)