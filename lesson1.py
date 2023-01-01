# print('hello world')
# print("hello world "+" from")
# print(2019+15)
# print("2019"+"15")
# myCountry = "USA"

# print("Hello "+myCountry)
# boolOne = True
# boolTwo = False
# print(boolOne)
# print(boolTwo)
# x = 5
# y = 7
# print(x>7)
# days = ['Monday', 'Tuesday', 'Wednesday',
# 'Thursday', 'Friday']
# print(days)
# word = 'word'
# sentence = "This is a sentence."
# paragraph = """This is a paragraph. It is
# made up of multiple lines and sentences."""
# print(sentence)
# print(paragraph)
# import sys; x = 'foo'; sys.stdout.write(x + '\n')

 

# Տրված տողի բոլոր "k" սիմվոլները փոխարինել "hh"-ով։

# string1 = input("please enter a string: ")
# new_string = string1.replace('k', 'hh')    
# print(new_string)

# Տրված է տող հաշվել տողում եղած թվանշանների քանակը։

# string1 = input("please enter a string: ")
# print(len(string1))


# Տրված տողից առանձնացնել ենթատող և արտածել ենթատողում եղած փոքրատառ և մեծատառ սիմվոլների քանակը։
# string1 = input("please enter a string: ")
# new_string = []
# for i in string1:
#     if i.isalpha():
#         new_string.append(i)
# print(len(new_string))

# Տրված տողից առանձնացնել ենթատող, որը պետք է կազմված լինի տեղի սկզբի 3 սիմվոլներից և վերջի 2 սիմվոլներից։ 
# Ստուգել եթե տողի սիմվոլների քանակը փոքր է 5-ից ապա արտածել տողը շրջված տեսքով։ Օր․՝  'abc'  պատ․՝ 'cba'

# string1 = input("please enter a word: ")
# if len(string1) <= 5:
#     print(string1[::-1])
# else:
#     print(string1[0:3] + string1[-2:])



# Տրված է 'I am a programmer' տողը, ստանալ՝ 'I-AM-A-PROGRAMMER'

# string1 = "I am a programmer"
# string2 = string1.upper()
# string3 = string2.split()
# print("-".join(string3))



# Տրված է տող։ Եթե տողում '12c3' ենթատողի առաջին հանդիպման ինդեքսը հավասար է 5-ի, ապա արտածել ենթատողից հետո տողի մնացած մասի միայն զույգ ինդեքսով սիմվոլները
# string1 = input("please enter a string: ")

# tox = "afyfa12c3fagsdfgdgdfg"
# ind = tox.index("12c3")
# if ind == 5:
#     next = tox[ind + 4::]
#     for i in range(0,len(next),2):
#         print(next[i], end="")


myDict = {"a":51, "b":15, "c":20,"d":5,"e":25}
values = list(myDict.values())
keys = myDict.keys()
for j in keys:
    for i in values:
        if str(i)[0] == '5':
            del myDict[j]      
print(myDict)       


