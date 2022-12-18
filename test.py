#! /usr/local/bin/python
#1. print function and """"
# print("Python is cool")
# print('I like the most "Python"')
# print('''I like Taisha's "Python"''')
# print('''Hello
# Python world.
# You
# are
# cool''')

#2. arifmetical functions
# original_price = float(input("Please enter the price: "))
# discount = 0.2*original_price
# new_price = original_price  - discount
# print("new price is", new_price)
# print(10/2-3)
# testl = float(input('Please enter teh frist number: '))
# test2 = float(input('Please enter teh second number: '))
# test3 = float(input('Please enter teh third number: '))
# average = (testl + test2 + test3) / 3.0
# print(average)

# total = float(input("please enter seconds: "))
# hours = total // 3600
# minutes = (total // 60) % 60
# seconds = total % 60

# print(hours)
# print(minutes)
# print(seconds)

# x = 9//2
# print(x)


import random
class Coin:

    def _init_(self):
        self.sideup = "Eagle"
    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = "Eagle"
        else:
            self.sideup = "Not Eagles"
    def get_sideup(self):
        return self.sideup

def main():
    my_coin = Coin()
    print("this is sideup:", my_coin.get_sideup())
    print("throing the coin")
    my_coin.toss()
    print(my_coin.get_sideup())
    
if __name__ == "__name__":
    main() 

