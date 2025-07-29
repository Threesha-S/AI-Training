# # program to get username & password (3 attempts)

# c_user = "nihal"
# c_pass = "hellcat"
# attempts_remaining = 3

# while attempts_remaining > 0:
#     l_user = input("\nEnter your username: ")
#     l_pass = input("Enter your password: ")

#     if c_user == l_user and c_pass == l_pass:
#         print("\nLogin successful")
#         break
#     else:
#         print("\nWrong credentials")

#     attempts_remaining -= 1

# if attempts_remaining == 0:
#     print("\nAccount suspended for 2 mins !")

# # --------------------------------------------------------------------------------------------- #

# # program to get bank balance & withdrawal amount

# bank_balance = 65000
# print("\n Your bank balance:", bank_balance)
# attempts_remaining = 3
# withdrawal_amount = int(input(" Enter amount to withdraw: "))
# bank_pin = 2004

# while attempts_remaining > 0:
#     l_bank_pin = int(input("\n Enter your pin: "))
#     if l_bank_pin == bank_pin and bank_balance > withdrawal_amount:
#         print("\n Amount withdrawal approved")
#         print("\n Your bank balance:", bank_balance-withdrawal_amount)
#         break
#     else:
#         print("\n Error !")
#     attempts_remaining -= 1

# if attempts_remaining == 0:
#     print("\n Account blocked temporarily")
# # ---------------------------------------------------------------------------------------- #

# # use while loop, get feedback . if I give stop, display "thanks for the feedback".

# while 1:
#     feedback = input("\n Enter your feedback: ")
#     if feedback.lower() == "stop":
#         print("\n Thanks for the feedback !")
#         break

# # ------------------------------------------------------------------------------------------- #

# # Functions - uses 'def' keyword.

# def my_func(name):          # name --> parameter
#     print("\n Hello", name)

# my_func("dilshad")          # "dilshad" --> argument.

# # --------------------------------------------------------------------------------------------- #

# # arbitrary argument - argument(s) are not limited, uses '*'.

# def my_funct(*names):
#     print("\n Hello", names[2])

# my_funct("dilshad", "fahid", "alby", "tebin")

# # ----------------------------------------------------------------------------------------------- #

# # arbitrary keyword argument - uses '**'.

# def my_func(**fruits):
#     print("\n The fruit is", fruits["fruitsname"], "and it's color is", fruits["fruitscolor"])

# my_func(fruitsname = "grape", fruitscolor = "violet")

# # ----------------------------------------------------------------------------------------------- #

# # default parameter

# def my_func(country = "india"):
#     print(f"\n I live in {country}")

# my_func()
# my_func("italy")
# my_func("usa")

# # ----------------------------------------------------------------------------------------------- #
# from os import MFD_ALLOW_SEALING

# # LEGB - Local, Enclosing, Global, Built-in function

# x = "global"
# def outer():
#     x = "Enclosing"
#     def inner():
#         x = "local"
#         print(x)
#     inner()

# outer()

# # ------------------------------------------------------------------------------------------------ #

# # prime numbers - 2, 3, 5, 7, 11, 13, 17, 19, 23, 27, 29, ........

# def prime_num(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# for i in range(30):
#     if prime_num(i):
#         print(i)

# # -------------------------------------------------------------------------------------------- #

# # Factorial number

# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result

# print(factorial(4))

# # ---------------------------------------------------------------------------------------------- #

# # Palindrome

# def palindrome(str):
#     str.lower()
#     if str==str[::-1]:
#         print("It is a palindrome !")
#     else:
#         print("not a palindrome")

# palindrome("malayalam")

# # ----------------------------------------------------------------------------------------------- #

# # List - collection of data, is ordered, mutable & heterogenous

# list1 = ["rishal", "dilshad", 24, 199, 3.14, True]

# # Positive indexing - starts from left and as '0'
# # Negative indexing - starts from right and as '-1'

# print(list1[2: 5: 2])  # slicing --> list(start: end+1: steps)

# # -------------------------------------------------------------------------------------------- #

# # List methods - append, extend, insert, pop, remove, copy, reverse, sort, clear, lower, upper
# # append - add element at last   # insert - add element at any position
# # extend - ensure to combine list   # pop - remove value based on index
# # remove - remove value by mentioning the element   # clear - clear the data
# # copy - copy the list  # reverse - reverse the list    # sort - arrange elements in list

# # append
# list1 = ["rishal", "dilshad", "alby", 32, 47, 89, True]
# list1.append(False)
# print(list1)

# # insert
# list1.insert(1, "rashin")
# print(list1)

# # extend
# list2 = ["ferrari", "pagani", "bmw", "bugatti"]
# list1.extend(list2)
# print(list1)

# # pop
# list1.pop(1)
# print(list1)

# # remove
# list1.remove("dilshad")
# print(list1)

# # copy
# list3 = list1.copy()
# print(list3)

# # reverse
# list1.reverse()
# print(list1)

# # sort
# list4 = ['ferrari', 'bmw', 'lamborghini']
# list4.sort()
# print(list4)
# list5 = [2, 4, 8, 5, 3, 1]
# print(list5)
# list5.sort()

# # clear
# print(list5)
# list5.clear()
# print(list5)

# list6 = [2, 2, 2, 2, 5, 7, 9, 8]
# print(list6.count(2))

# # ----------------------------------------------------------------------------------------- #

# # define a list using for loop to access all elements in the list.

# list1 = ["ferrari", "bugatti", "pagani", "aston martin"]
# list2 = []

# for i in list1:
#     list2.append(i)

# print(list2)

# # ------------------------------------------------------------------------------------------ #

# # Tuple - represented with (), is ordered, is immutable

# tuple1 = ('abhinav', 'dilshad', 24, 89, 'nihal', 65.00)
# print(tuple1)
# print(tuple1[1::])

# # -------------------------------------------------------------------------------------------- #

# # Tuple methods - count, index
# # count - to get count of an element    index - to get index of an element

# #count
# tuple1 = (2, 3, 2, 4, 7, 9, 8)
# print(tuple1)
# print(tuple1.count(2))

# # index
# tuple1 = (2, 3, 2, 4, 7, 9, 8)
# print(tuple1)
# print(tuple1.index(2))

# # ---------------------------------------------------------------------------------------- #

# # list and tuple allows duplicate elements

# # ---------------------------------------------------------------------------------------- #

# # set - represented with {}, doesn't allow duplicate elements, is unordered, there is no indexing

# set1 = {2, 3, 4, 5, 6, 2, 3, 4, 7, 9, 8, 8}
# print(set1)

# # -------------------------------------------------------------------------------------------- #

# # Set methods - add, update, discard, remove, pop
# # Set operations - union, intersection, difference

# set1 = {1, 3, 2, 2, 4, 6, 6, 5, 7, 9}
# print(set1)
# set1.add(10)
# print(set1)
# set1.update([11, 12, 13, 14])
# print(set1)
# set1.discard(3)
# print(set1)
# set1.remove(15)
# print(set1)
# set1.pop()
# print(set1)

# set1 = {1, 2, 3, 4, 5}
# set2 = {5, 6, 7, 8, 9}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))

# # ------------------------------------------------------------------------------------------- #

# # Function to find unique values

# def unique_items(text):
#     words = text.lower().split()
#     unique = set(words)
#     return len(unique)

# print(unique_items("Python is great. python is simple"))

# # ---------------------------------------------------------------------------------------------- #

# # Remove duplicate from a list

# def rmv_duplicates(nums):
#     result = []
#     for i in nums:
#         if i not in result:
#             result.append(i)
#     return result

# print(rmv_duplicates([1, 2, 2, 2, 3, 4, 6, 7, 9, 7]))

# # ---------------------------------------------------------------------------------------------- #

# # Print words longer than 3 letters from a list

# list1 = ["deepa", "kadhir", "joe", "sri", "priya"]
# for i in list1:
#     if len(i) > 3:
#         print(i)

# # ----------------------------------------------------------------------------------------------- #

# # Dictionary - collection of different elements, is represented using {}

# dict1 = {"name" : "shaz",
#          "department" : "AI&DS",
#          "age" : 20 }

# print(dict1["age"])

# # ------------------------------------------------------------------------------------------------ #

# # Example for dictionary

# dict1 = {"name" : "nihal",
#          "age" : 20,
#          "department" : "CSE"}

# print(dict1)

# dict2 = {}      # Empty dictionary

# print(dict2)

# # -------------------------------------------------------------------------------------------------- #

# # Using 'dict' keyword, while using 'dict', replace ':' with '='

# dict3 = dict(name = 'nihal', age = 20, dep = 'CSE')

# print(dict3)

# # From a list or tuples
# dict4 = dict([('a', 1), ('b', 2)])
# print(dict4)

# # Dictionary methods - get, setdefault, update, items, keys, values

# # get method
# dict1 = {'name' : 'nihal', 'age' : 20, 'dep' : 'cse', 'place' : 'malappuram'}
# print(dict1)
# print(dict1.get('place', 'kerala'))
# print(dict1)
# print(dict1.get('height', 156))
# print(dict1)

# # setdefault
# dict1 = {'name' : 'nihal', 'age' : 20, 'dept' : 'cse'}
# print(dict1)
# dict1.setdefault('email', 'abc@shanmugha.edu.in')
# print(dict1)

# # update
# dict1 = {'name' : 'nihal', 'age' : 20, 'height' : 156}
# print(dict1)
# dict1.update({'place' : 'kerala'})
# print(dict1)
# dict1['name'] = 'mufeed'
# print(dict1)

# # keys & values
# dict1 = {'name' : 'nihal', 'age' : 20}
# print(dict1)
# print(dict1.keys())
# print(dict1.values())

# # delete method - del, pop

# # del
# dict1 = {'name' : 'nihal', 'age' : 20}
# print(dict1)
# del dict1['age']
# print(dict1)

# # pop
# print(dict1)
# dict1.pop('name')
# print(dict1)

# dict1 = {'name' : 'nihal'}
# print(dict1)
# dict1.pop('age', "not found")   # display 'not found'

# # ------------------------------------------------------------------------------------------------ #

# # Create frequency dictionary from text

# text = 'banana apple banana apple kiwi'
# dict1 = {}
# for i in text.split():
#     dict1[i] = dict1.get(i, 0) + 1

# print(dict1)

# # ------------------------------------------------------------------------------------------------- #

# # Nested dictionary

# dict1 = {
#     "class1" : {
#         'A' : {'name' : 'abc', 'age' : 25},
#         'B' : {'name' : 'xyz', 'age' : 23}
#     }
# }

# print(dict1['class1']['A']['name'])

# # ------------------------------------------------------------------------------------------------- #

# users = {
#     101 : 'aaa',
#     102 : 'aab',
#     103 : 'aac'
# }

# def my_func(users, userid):
#     return users.get(userid, "unknown")

# print(my_func(users, 105))

# # ----------------------------------------------------------------------------------------------- #

# # File handling

# # Absolute path - entire path.      # Relative path - only the file name.

# # Files are named locations on disk to store data.

# # File operations - open(), read(), write(), append()

# # open the file, do read/write operation, close the file.

# # Files can be .txt, binary, csv, etc.

# # open()
# # syntax - file = open('filepath', 'mode')

# # mode - read the file -> 'r'       write contents into file -> 'w'     append contents into file -> 'a'
# # read and write into file -> 'r+'      write and read into file -> 'w+'        append and read into file -> 'a+'

# # Reading from a file - read, readline, readlines
# # read - reads the entire file      readline - reads one line       readlines - reads line by line

# # file = open('/home/nika/PycharmProjects/FileHandling/sample1.txt', 'r')
# data = file.read()
# print(data)
# data1 = file.readline()
# print(data1)
# data2 = file.readlines()
# print(data2)

# # Write methods - write(), writelines()
# # write()

# file = open(r'/home/nika/PycharmProjects/FileHandling/sample1.txt', 'w')
# content = 'this is a sample sentence.\n,This is the second line'
# file.write(content)
# file = open(r'/home/nika/PycharmProjects/FileHandling/sample1.txt', 'r')
# print(file.read())

# # append()
# file = open(r'/home/nika/PycharmProjects/FileHandling/sample1.txt', 'a')
# file.write("\nThis is the first line")
# file.write("This is the second line")
# file.write("\nThe real second line")
# file = open(r'/home/nika/PycharmProjects/FileHandling/sample1.txt', 'r')
# print(file.read())

# # read & write()
# file = open('/home/nika/PycharmProjects/FileHandling/sample1.txt', 'r+')
# content = file.read()
# print(content)
# file.write("This is a sample sentence")
# file = open('/home/nika/PycharmProjects/FileHandling/sample1.txt', 'r')
# content = file.read()
# print(content)

# # write & read
# file = open("/home/nika/PycharmProjects/FileHandling/sample1.txt", 'w+')
# file.write('you guys are very smart, especially alby')
# file = open("/home/nika/PycharmProjects/FileHandling/sample1.txt", 'r')
# print(file.read())

# # append & read
# file = open('/home/nika/PycharmProjects/FileHandling/sample1.txt', 'a+')
# file.write('\nThis is the second line.')
# file = open('/home/nika/PycharmProjects/FileHandling/sample1.txt', 'r')
# print(file.read())

# # -------------------------------------------------------------------------------------------- #

# # Structured - tabular data
# # pandas - package used to perform data manipulation
# import pandas as pd
# file = pd.read_csv('demo.csv')

# # ---------------------------------------------------------------------------------------------- #

# # Read a file & return longest sequence
# def ls(filepath):
#     with open(filepath, 'r') as file:
#         text = file.read()
#         sentence = text.split('.')
#         max_sentence = max(sentence, key=len)
#         return max_sentence.strip()

# print(ls('/home/nika/PycharmProjects/FileHandling/sample1.txt'))

# # -------------------------------------------------------------------------------------------------- #

# # Exception handling in python

# # Type error        Syntax error        Name error      Indentation error       Zero division error     Key error
# # Index error       Runtime error       Arithmetic error        Compilation error       Module not found error
# # File not found error      Value error     Keyboard interrupt error

# # try block - lets you test a block of code for errors
# # except block - lets you handle the error
# # else block - lets you execute code when there is no error
# # finally block - lets you execute code regardless of result of try and except block

# num = int(input('Enter a number: '))
# try:
#     var = num / 0
#     print(var)
# except(ZeroDivisionError):
#     print("is divided by zero")
# finally:
#     print('code executed successfully')

# number = int(input('Enter a number: '))
# try:
#     var = number / 0
#     print(var)
# except(ZeroDivisionError):
#     print('is divided by zero')
# except(ValueError):
#     print('Enter an integer')
# else:
#     print('is divided successfully')
# finally:
#     print('code executed successfully')

# try:
#     file = open('', 'r')
#     content = file.read()
#     print(content)
# except(FileNotFoundError):
#     print('no file on the path')
# else:
#     print('file read successfully')
# finally:
#     print('program executed successfully')

# # get age from user, if age > 18, eligible else not,    user try, except, finally

# userAge = int(input('Enter your age: '))
# try:
#     if userAge >= 18:
#         print('eligible for voting')
# except(ValueError):
#     print('not eligible for voting')
# else:
#     print('that is eligible')
# finally:
#     print('program executed successfully')

# # ------------------------------------------------------------------------------------------ #

# # OOP - Object Oriented Programming

# class Goatrip():
#     def beach(self):
#         print('to watch the sunset')
#     def party(self):
#         print('to party')

# abhinav = Goatrip()         # object creation and class initialization
# tebin = Goatrip()           # object creation and class initialization
# abhinav.beach()
# tebin.party()

# class FoodOrder():
#     # name & other values can directly be added here as well.
#     def frenchfries(abc):
#         print(f'french fries is added to {abc.name} cart')
#     def sausage(abc):
#         print(f'sausage is added to {abc.name} cart')

# nihal = FoodOrder()
# munthazir = FoodOrder()

# nihal.name = 'Nihal'
# munthazir.name = ('Munthazir')

# nihal.sausage()
# munthazir.frenchfries()

# class GoaTrip():
#     def __init(self):
#         self.name = name
#         self.budget = budget
#     def beach(self):
#         print(f'{self.name} - to watch the sunset')
#     def party(self):
#         print(f'{self.name} - to party')

# abhinav = GoaTrip('abhinav', 7000)
# tebin = GoaTrip('tebin', 8000)
# not completed

# # create a class - bank account, create a simple bank software - deposit, balance, withdraw

# class bank():
#     def __init__(self, balance, dep_amount, withdraw):
#         self.dep_amount = dep_amount
#         self.balance = balance
#         self.withdraw = withdraw
#     def Deposit(self):
#         if self.dep_amount > 0:
#             print(f'{self.dep_amount} is deposited into your Acc: xxxxxxxxxx98')
#             self.balance += self.dep_amount
#         else:
#             print('Invalid deposit amount')
#     def Balance(self):
#         print(f'your current balance is {self.balance}')
#     def Withdraw(self):
#         if self.balance >= self.withdraw:
#             print(f'{self.withdraw} was withdrawn from your Acc: xxxxxxxxxx98')
#             self.balance -= self.withdraw
#         else:
#             print('Insufficient balance')

# print('-------------\n')
# nihal = bank(8000, 10000, 2000)
# nihal.Balance()
# nihal.Deposit()
# nihal.Balance()
# nihal.Withdraw()
# nihal.Balance()
# # also try it in another method

# # create a class - Rectangle, get to objects - height, width

# class Rectangle():
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
#     def area(self):
#         x = self.height * self.width
#         print(f'calculated area: {x}')
#     def perimeter(self):
#         y = 2 * (self.height + self.width)
#         print(f'calcualted perimeter: {y}')

# a = Rectangle(20, 40)
# a.area()
# a.perimeter()

# # Text document editor

# # ----------------------------------------------------------------------------------------------- #

# # 4 pillars in OOPS - abstraction, encapsulation, inheritance, polymorphism

# # abstraction - hiding of internal information, shows only the necessary parts of an object / process.
# # encapsulation - binds the data into single unit.
# # inheritance - one class attain the behaviour and properties of another class
# # polymorphism - perform single task in many ways.

# class Animal():
#     def sound(self):
#         print('All animals are giving sound')
# class Dog(Animal):
#     def bark(self):
#         print('Dog barks')
# class Cat(Animal):
#     def meow(self):
#         print('Cat meows')

# c1 = Cat()
# d1 = Dog()
# c1.meow()
# d1.sound()
# c1.sound()
# d1.bark()

# # ----------------------------------------------------------------------------------------------- #

# # Encapsulation - binding the data into a single unit.
# # Methods - setter & getter -> used on private mode.

# # Access modifiers - public, private, protected

# class person():
#     def __init__(self, name, age):         # is a constructor
#         self.name = name        # public mode - no underscore
#         self.__age = age        # private mode - double underscore
#         # self._age = 20          # protected mode - single underscore

#     def display(self):
#         print(f'name is {self.name} and age is {self.__age}')
#     def setter(self, newAge):
#         if newAge > 0:
#             self.__age = newAge
#     def getter(self):
#         return self.__age

# p1 = person('Godson', 19)
# p1.display()
# p1.getter()         # returns 19
# p1.setter(21)
# p1.display()

# # ------------------------------------------------------------------------------------------------- #

# class person():
#     def __init__(self, name, age):
#         self.name = 'Code Alpha'
#         self.__age = age
#     def display(self):
#         print(f' name: {self.name}\n age: {self.__age}')
#     def setter(self, newAge):
#         if newAge > 0:
#             self.__age = newAge
#     def getter(self):
#         return self.__age

# p1 = person('Godson', 20)
# p1.getter()
# p1.setter(21)
# p1.display()

# # ------------------------------------------------------------------------------------------ #

# # create ATM class, create parameter pin(private), use setter - get newPin, use getter.

# class ATM:
#     def __init__(self, pin):
#         self.__pin = pin
#     def display(self):
#         print(f'pin: {self.__pin}')
#     def setter(self, newPin):
#         newPin = str(newPin)
#         if len(newPin) == 4:
#             # newPin = int(newPin)              # optional
#             self.__pin = newPin
#     def getter(self):
#         return self.__pin

# user1 = ATM(2020)
# user1.getter()
# user1.display()
# user1.setter(4040)
# user1.getter()
# user1.display()

# # ------------------------------------------------------------------------------------------------- #

# # Polymorphism

# class Bird:
#     def fly(self):
#         print('Bird is flying in the sky')
# class Flight:
#     def fly(self):
#         print('Flight flies')
# class Superman:
#     def fly(self):
#         print("Superman fly using super powers")

# b1 = [Bird(), Flight(), Superman()]

# for i in b1:
#     i.fly()

# class Car:
#     def drive(self):
#         print('Car drives')
# class Bike:
#     def drive(self):
#         print('Bike drives')
# class Rickshaw:
#     def drive(self):
#         print('Rickshaw drives')

# s1 = [Car(), Bike(), Rickshaw()]
# for i in s1:
#     i.drive()

# # -------------------------------------------------------------------------------------------- #

# # Abstraction

# class Juicemaker:                   # private or public, doesn't matter.
#     def make_juice(self):
#         self.__wash()
#         self.__cut_the_fruits()
#         self.__blending()
#         self.__adding_sugar()
#         self.__serve()
#     def __wash(self):
#         print('washing the fruits')
#     def __cut_the_fruits(self):
#         print('cut the fruits using knife')
#     def __blending(self):
#         print('Grid the fruits')
#     def __adding_sugar(self):
#         print('add required sugar')
#     def __serve(self):
#         print('serve & enjoy')

# jm = Juicemaker()
# jm.make_juice()

# # ----------------------------------------------------------------------------------------------- #

# # Dunder method - double underscore method / special method

# # __init__      __str__     __add__     __repr__        __del__                    etc.

# from datetime import date

# class Person:
#     def __init__(self, name):
#         self.name = name
#     # def __str__(self):          # used to help user to understand.
#     #     return self.name
#     # def __repr__(self):           # used to help developer to understand.
#     #     return self.name
#     # def __del__(self):
#     #     print('Object is destroyed!')
#     def __add__(self, x, y):
#         self.x = x
#         self.y = y

# p1 = Person('nihal')
# # print(p1.name)          # normal way to print name
# # print(p1)               # doesn't return 'nihal'
# # after using string method
# print(p1)
# # p2 = Person(21)          # display TypeError
# # print(p2)

# # after adding 'datetime'
# d = date(year=2025, month=7, day=24)
# print(d)
# # y = datetime.date(2025, 7, 24)

# print(repr(p1))         # display 'nihal' as understandable to a developer.
# print(repr(d))          # display date as understandable to a developer.

# del p1          # to delete an object.

# p1 = Person('nihal')
# print(p1)      # represent again when __repr__ is used.

# class Person:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return f'{self.x}, {self.y}'
#     def __add__(self, other):               # also same for '__sub__', '__mul__', '__eq__', '__lt__', '__gt__', '__le__', '__ge__'
# # '__contains__', '__getitems__', '__call__', '__hash__'
#         return Person(self.x + other.x, self.y + other.y)
#     # def __eq__(self, other):
#     #     return Person(self.x == other.x, self.y == other.y)

# p1 = Person(3, 4)
# p2 = Person(3, 4)
# print(p1 + p2)
# # print(p1 == p2)         # returns 'True, True'
# # after commenting '__eq__' function.
# print(p1 == p2)         # compares memory address.

# class Person:
#     def __init__(self, data):
#         self.data = data
#     def __len__(self):
#         return len(self.data)
#     def __contains__(self, item):
#         return item in self.data
#     def __abs__(self):
#         return (self.x ** 2 + self.y**2) ** 0.5

# m1 = Person([15, 16, 2])
# print(len(m1))

# m1 = Person([15, 16, 2, 89, 000])
# print(len(m1))
# print(000 in m1)
