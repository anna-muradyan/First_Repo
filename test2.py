#! /usr/local/bin/python
# text = input("enter a text: ")
# if "hel" in text and "hey" not in text:
#     print("text is good")
# elif "hey" in text and "hel" not in text:
#     print("not bad")
# else:
#     print("good text")

# number = int(input("please enter a number:"))
# while number > 0:
#         print("you entered positiv enumber, keep on doing it")
#         number = int(input("please enter a number:"))
# print("you entered a negative number")


# total = 0
# price = float(input("please enter a price:"))
# while price > 0:    
#     total += price 
#     price = float(input("please enter a price:"))
# print("whatever", total)

# number = float(input("please enter a number:"))
# count = 0
# while number != 0:
#     if number%10 == 2 and number%4 == 0:
#         print("good number")
#         count += 1
#     else:
#         print("not good nuber")
#     number = float(input("please enter a number:"))   
# print("number", count)

# print("wow")
# print("hel","llo",sep="-", end="\n")
# print("lo")



# number = input("enter a number: ")
# sum = 0
# for i in str(number):
#         sum = sum + int(i)
# print(sum)



# number = input("enter a 4digit number: ")
# print(number[-1])



# number = input("enter a 4digit number: ")
# print(number[0:2]+number[3:4])

# number = input("enter a number: ")
# summ = 0
# for i in str(number):
#     summ += int(i)
# print(summ)

# print("\u2603")

# number = input("enter a number: ")
# odd = even = 0
# for i in range(0,len(number),2):
#     odd = odd + int(number[i])

# text = input("please enter a text:")
# text_reversed = text[::-1]
# print(text_reversed)

#Նախադասության մեջ գտնել այն բառերը, որոնք սկսվում և ավարտվում են նույն սիմվոլով:
# sentence = input("enter a sentence: ")
# new_sentence = sentence.split()
# for i in new_sentence:
#     if i[0] == i[-1]:
#         print(i,sep="-",end="")


#Նախադասության մեջ գտնել այն բառերը, որոնք պարունակում են 1-ից ավել “a” սիմվոլ:
# sentence = input("enter a sentence: ")
# new_sentence = sentence.split()
# count = 0
# for i in new_sentence:
#     if i.count("a") > 1:
#         print(i)




#Հաշվել թե քանի անգամ տառը հանդիպում բառի մեջ
# word = input("enter a word: ")
# letter = input("enter a letter: ")
# print(word.count(letter))

    

#Թիվը դրական է թե բացասական
# number = int(input("enter a number: "))
# if number > 0:
#     print("positive")
# elif number < 0:
#     print("negative")
# else:
#     print("poka")



#Գտնել եռանիշ թվի թվանշանների գումարը
# number = input("enter a number: ")
# sum = 0
# for i in number:
#     sum += int(i)
# print(sum)



#Եթե մուտքագրված թիվը եռանիշ է և բազմապատիկ է 3-ի ապա տպել “YES”, հակառակ դեպքում “NO”
# number = int(input("enter a number: "))
# while number < 1000 and number > 99:
#     if number%3 == 0:
#         print("number is good")
#     else:
#         print("not good")
#     number = int(input("enter a number: "))
    


# number = 1001
# for i in range(0,1001,10):
#     print(i,",", end ="")

# max_t = 102.5
# temper = float(input("please enter a number:"))
# while temper > max_t:
#     print("not good")
#     temper = float(input("please enter a number:"))
# print("good")

# count = 10
# while count == 10:
#     print("hello")

# for i in range(5):
#     print("hello")

#usage \t 

# end = int(input("input a number: "))
# print("i\tsquare")
# print("--------------")
# for i in range(1, end + 1):
#     square = i**2
   
#     print(f"{i}\t{square}")



# total = 0
# for i in range(1,6):
#     total += i
# print(f"amount is {total}")

# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, minutes, seconds)
# for j in range(8):
#     for i in range(6):
#         print("*", end ="")
#     print()

#print stars
# r = 8
# for i in range(r):
#     for j in range(i+1):
#         print("*", end ="")
#     print()

# r = 6
# for i in range(r):
#     for j in range(i):
#         print(" ", end ="")
#     print("#")

#factorial

# number = int(input("please enter a number:"))
# mult = 1
# if number < 0:
#     print("poka")
# elif number == 0:
#     print("good bye")
# else:
#     for i in range(1,number+1):
#         mult *= i
#     print(mult)


# r = 8
# for i in range(r):
#     for j in range(i+1):
#         print("*",end ="")
       

l = [10, 11, 12, 13, 14, 15, 16, 17 ,18, 19, 20]
# for i in range(len(l)):
#     l[i] = "t" + str(l[i]) 
# print(l)

#Տրված է եռանիշ թիվ: Ավելացնել նույն եռանիշ թիվը աջից: Օրինակ 123 պատ 123123:
# number = input("enter a number: ")
# x = number[1] + number[0] + number[3] + number[2]
# print(x)


# numbers = [1,2,1,2,5,7,8,8,9,9,10]
# counts = {}
# for number in numbers:
#     counts[number] = counts.get(number,0) + 1
# print(counts)
# for number in numbers:
#     if number not in counts:
#         counts[number] = 1
#     else:
#         counts[number] += 1
# print(counts)
# print(counts.get(2))


dict1 ={"anna":1, "manna":2, "nanna":3}
print(dict1["anna"])
print(dict1.values())
print(dict1.keys())
