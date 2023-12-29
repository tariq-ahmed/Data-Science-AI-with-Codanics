# function: is a   block of code which only runs when it is called.
# you can pass data, known as paramenter into a function.
# function can return data as a result.
# In Python, a function is defined using the def keyword.

#let create function

# def greet_user():
#     print("Hello, user!")
# greet_user()

# def aoa():
#     print("Aslam O Aleakum")

# aoa()

# def aoa(name):
#     print(f"Aslam O Aleakum, {name}!, How are you?")

# aoa("Ali")

# def aoa(name = "mere bhai"):
#     print(f"Aslam O Aleakum, {name}!, How are you?")

# aoa("Ali")

# # return values

# def square(number):
#     return number * number

# print(square(3))

# # 4 line of code
# def square(number):
#     return number * number
# result = square(3)
# print(result)


# recursion: function calling itself is called recursion and the function is called recursive function. 
# 

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1) # 5 * 4 * 3 * 2 * 1

# print(factorial(5)) # 5 * 4 * 3 * 2 * 1 = 120


# # lamda function: A lambda function is a small anonymous function. 
# #  A lambda function can take any number of arguments, but can only have one expression.

# x = lambda a:a + 10
# print (x(5))

# x = lambda a : a / 2
# print(x(10))


# x = lambda a, b : a * b
# print(x(5,7))

# #  write 10 functions of your own choice on def and lambda function.
# # 1
# def add (a,b):
#     return a + b
# print(add(5,7))

# # 2

# def sub(a,b):
#     return a - b

# print(sub(7,5))

# # 3

# def mul(a,b):
#     return a * b

# print(mul(5,7))

# # 4

# def div(a,b):
#     return a / b

# print(div(10,2))


# # 5

# def mod(a,b): # mod is a remainder
#     return a % b

# print(mod(10,3))

# 6

x = lambda a,b : a ** b
print(x(5,2))

# 7

x = lambda a,b : a // b  # // is a floor division  5 // 2 = 2 
print(x(10,3))

# 8

x = lambda a,b : a + b + 10
print(x(5,7))

# 9

x = lambda a , b : a - b + 10
print(x(7,5))

# 10

x  = lambda a , b : a * b + 11
print(x(5,7))


