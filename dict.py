#1) Բառարանից հեռացնել բոլոր այն զույգերը, որոնց արժեքների առաջին թվանշանը 5 է։
myDict = {"a":51, "b":15, "c":20,"d":5,"e":5}
dict_1 = {}  # dict()

for key, values in myDict.items():
    if str(values)[0] != "5":
        dict_1[key] = values

print(dict_1)

for key in myDict.copy():
    values = str(myDict[key])
    if values[0] == "5":
        myDict.pop(key)

print(myDict)


#2)Տրված է բառարան։ Ստանալ ցուցակ բառարանի այն բանալիներից, որոնց արժեքները եռանիշ թվեր են։
myDict = {"aram":513, "b":151, "c":201,"d":51,"e":5125}
myList = []
for key in myDict.copy():
 values = str(myDict[key])
 if len(values) == 3:
  myList.append(values)
print(myList)

#3)Ստանալ ցուցակ, որը կազված կլինի list1-ի կենտ ինդեքսով էլեմենտներից և list2-ի զույգ ինդեքսով էլեմենտներից։
list1 = [0, 21, 15, 5, 8, 35, 48, 18, 58, 25]
list2 = [0, 1, 8, 15, 25, 68, 48, 77, 88, 15, 38]
new_list = []
for i in list1:
    index = list1.index(i)
    if index % 2 != 0:
        new_list.append(i)
for i in list2:
    index = list2.index(i)
    if index % 2 == 0:
        new_list.append(i)
print(new_list)

#another method for 3)
list1 = [0, 21, 15, 5, 8, 35, 48, 18, 58, 25]
list2 = [0, 1, 8, 15, 25, 68, 48, 77, 88, 15, 38]
list2_even = list2[::2]
list1_odd = list1[1::2]
print(list2_even + list1_odd)

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
myDict = {"aram":2015, "babken":2001, "anna":1995,"david":2020,"ervand":1978}
for key in myDict.copy():
    values = str(myDict[key])  
    if "0" in values:
        myDict.pop(key)
print(myDict)
        
#6) Տրված է dict1 և dict2 բառարանները։ Ստանալ dict3 բառարանը որը կազմված է dict1-ի և dict2-ի զույգերից (մեկումեջ դասավորված)
dict1 = {"zero":0,"two":2, "four":4, "six": 6, "eight":8,"ten":10}
dict2 = {"one":1,"three":3,"five":5,"seven":7, "nine":9}
dict3 = {**dict1, **dict2}
dict3 = dict(sorted(dict3.items(), key=lambda x:x[1]))
print(dict3)


dict1 = {"one": 1, "three":3, "five":5}
dict2 = {"two":2, "fore":4, "six":6}
dict3 = dict()

list1 = list(dict1)
list2 = list(dict2)
for i in range(len(list1)):
    dict3[list1[i]] = dict1[list1[i]]
    dict3[list2[i]] = dict2[list2[i]]

print(dict3)