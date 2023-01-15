#1 Print First 10 natural numbers using while loop
# num = 1
# while num <= 10:
#     print(num)
#     num += 1

#2 Print the following pattern
# row = 5
# for i in range(1, row + 1, 1):
#     for j in range(1, i+1):
#         print(j, end= " ")
#     print("")

#3 Calculate the sum of all numbers from 1 to a given number
# num = int(input("please enter a number: "))
# sum = 0
# for i in range(num):
#     i += 1
#     sum = sum + i
# print(sum)

#4 Write a program to print multiplication table of a given number
n = 2
# for i in range(1,11,1):
#     n = i*2
#     print(n)


#5: Display numbers from a list using loop

numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i > 500:
#         break              
#     elif i > 150:
#         continue
#     elif i %5 == 0:        
#         print(i)

#6: Count the total number of digits in a number
# number = 75869
# a = (len(str(number)))
# print(a)

#7 Print the following pattern
# for i in range(6,1,-1):
#     i -= 1
#     print(i, end =" ")
#     print()


#8 Print list in reverse order using a loop
# list1 = [10, 20, 30, 40, 50]
# l = list1[::-1]
# for i in l:
#     print(i)

#9 Display numbers from -10 to -1 using for loop
# for i in range(-10,0,1):
#     print(i)

#10: Use else block to display a message “Done” after successful execution of for loop
# for i in range(5):
#     print(i)
# else:
#     print("Done!")

#11: Write a program to display all prime numbers within a range
#range 25 to 50
j = 1
for i in range(25,50):
    if i+1 % i == 0:
        break
    else:
        print(i)
