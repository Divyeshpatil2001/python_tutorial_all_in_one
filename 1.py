# def max_num(x,y,z):
#     if x >= y and x >= z:
#         return x
#     elif y >= x and y >= z:
#         return y
#     else:
#         return z
# print(max_num(150,250,145))


# num1 = float(input("enter first num:"))
# num2 = float(input("enter second num:"))
# opt = input("enter operator")

# if opt == "+":
#     print(num1 + num2)
# elif opt == "-":
#     print(num1 - num2)
# elif opt == "*":
#     print(num1 * num2)
# elif opt == "/":
#     print(num1 / num2)
# else:
#     print("invalid operator")
    

# monthdict = {
#     "jan" : "january",
#     "feb" : "feburary",
#     "mar" : "march"
# }

# print(monthdict["feb"])
# print(monthdict.get("mar"))
# if there is a no key then get is helpful for the default value
# print(monthdict.get("apr","not a valid key"))


# building guessing game

# secret_word = "abc"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guess = False

# while guess != secret_word:
#     if guess_count < 3:
#         guess = input("enter guess word:")
#         guess_count += 1
#     elif guess_count >= 3:
#         print("out of guesses")
#         break
# else:
#     print("win!")

# 2 method

# while guess != secret_word and not(out_of_guess):
#     if guess_count < guess_limit:
#         guess = input("enter guess word:")
#         guess_count += 1
#     else:
#         out_of_guess = True
# if out_of_guess :
#     print("lose")
# else:
#     print("win")


# friends = ["abc","xyz","def"]
# for i in range(len(friends)):
#     print(friends[i])

# def raise_to_power(a,b):
#     result = 1
#     for i in range(b):
#         result = result * a
#     return result
# print(raise_to_power(5,2))
    
    
# 2d lists
# num_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#     ]
# print(num_grid[0][2])

# nested loop
# num_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#     ]

# for i in num_grid:
#     for j in i:
#         print(j)

# def translate(phrase):
#     translation = ""
#     for i in phrase:
#         if i.lower() in "aeiou":
#             if i.isupper():
#                 translation = translation + "G"  
#             else:  
#                 translation = translation + "g"
#         else:
#             translation = translation + i
#     return translation

# print(translate(input("enter phrase:")))



# try except

# try:
    # ans = 10/0
    # num = int(input("enter num"))
    # print(num)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as err:
#     print(err)
# except:
#     print("erroe")

# reading file
# file = open("1.txt","r")
# print(file.readable())
# print(file.read())
# print(file.readline())
# print(file.readlines())

# for i in file.readlines():
#     print(i)
# file.close()

# appending file
# file = open("1.txt","a")
# file.write("\nc = bbjcsj ")
# file.close()

# writing file
# file = open("2.txt","w")
# file.write("1 = hu")
# file.close()

# file = open("index.html","w")
# file.write("<p>hihello</p>")
# file.close()

# modules
# import array
# print(array.typecodes)

# class objects
# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(name , age)
# std1 = student("abc",22)
# std2 = student("xyz",21)
# print(std1.name)
# print(std1.age)

# inheritance

# class chef:
#     def make_chicken(self):
#         print("chicken")
#     def make_salad(self):
#         print("salad")
#     def make_special_dish(self):
#         print("special dish")

# class chinese_chef(chef):
#     def make_special_dish(self):
#         print("chines special")
#     def make_fried_rice(self):
#         print("fried rice")
        
# mychef = chef()
# mychef.make_special_dish()

# mychinesechef = chinese_chef()
# mychinesechef.make_fried_rice()
# mychinesechef.make_special_dish()

# iterator
# list = [4,5,7,8]
# iterator = iter(list)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# list = [4,5,7,8]
# iterator = iter(list)
# for i in iterator:
#     print(i)
    
# class powtwo:
#     def __init__(self,max):
#         self.max = max
#     def __iter__(self):
#         self.n = 0
#         return self
#     def __next__(self):
#         if self.n <= self.max:
#             result = 2 ** self.n
#             self.n += 1
#             return result
#         else:
#             StopIteration
# num = powtwo(4) 
# print(num.__iter__())      
# print(num.__next__()) 
# iterator = iter(num)
# for i in iterator:
#     print(i) 

# class even:
#     def __init__(self,max):
#         self.n = 2
#         self.max = max
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n <= self.max:
#             result = self.n
#             self.n += 2
#             return result
#         else:
#             raise StopIteration
# ab = even(10)
# for i in ab:
#     print(i)


# generator
# def my_generator(n):
#     value = 0
#     while value < n:
#         yield value
#         value += 1
# for i in my_generator(5):
#         print(i)

# square_genrator = (i*i for i in range(5))
# for i in square_genrator:
#     print(i)

# def calculate():
#     num = 1
#     def inner_func():
#         nonlocal num
#         num += 2
#         return num
#     return inner_func

# call the outer function
# odd = calculate()

# call the inner function
# print(odd())
# print(odd())
# print(odd())

# call the outer function again
# odd2 = calculate()
# print(odd2())


# closure
# def abc(n):
#     def xyz(x):
#         return x*n
#     return xyz
# q = abc(2)
# print(q(5))

# decorators
# def a(func):
#     def inner(a,b):
#         print("dived  a n b")
#         if b == 0:
#             print("its 0 soorry")
#             return
#         return func(a,b)
#     return inner
# @a
# def simple(a,b):
#     print(a/b)
# simple(4,2)  
# simple(4,0)

# import os
# print(os.getcwd())

# super class used
# class dog:
#     def __init__(self):
#         print("parent")
#     def eat(self):
#         print("eatingg")
# class cat(dog):
#     def __init__(self):
#         super().__init__()
#         super().eat()
#         print("child")
# a = cat()