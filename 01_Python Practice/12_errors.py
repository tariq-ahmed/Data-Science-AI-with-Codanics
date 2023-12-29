# # syntax or indentation error
# x = 5
# if x > 3:
# print("x is greater than 3") # indeqntation error


# # logical or human error
# x  = 5
# if x >3:
#     print("y is greater than 3") # logical error, y is not defined

# # runtime error or module not found error
# print(np.sqrt(25)) # name np is not defined



# # value error 
# x = int("ten") # value error, invalid literal for int() with base 10: 'ten'


# # zero division error
# x = 5/0 # zero division error, division by zero is not possible in python 




# # attribute error
# x = 5
# print(x.shape) # int object has no attribute shape  # attribute error 



# import error
# # index error
# x = [1,2,3]
# print(x[3]) # index error, list index out of range




# # key error
# x = {"a":1, "b":2}
# print(x["c"]) # key error, key c is not present in dictionary x 



# # name error 
# x = 5
# print(y) # name y is not defined





# # stop iteration error 
# x = iter([1,2,3]) # iterator object 
# print(next(x)) # 1 





# # unbound local error
# x = 5
# def add():
#     x = x + 5 # unbound local error, local variable x referenced before assignment
#     return x
# print(add())






# # unindentation error, unexpected indent , 
# # indentation error, expected an indented block
# x = 5
# if x > 3:
#     print("x is greater than 3") # unindentation error, unexpected indent

# # file not found error
# x = open("abc.txt") # file not found error, no such file or directory: 'abc.txt'

# # memory error, memory is not sufficient to create a list of 100000000 elements
# x = [1]*100000000
# print(x) # memory error, memory is not sufficient to create a list of 100000000 elements


# # timeout error: 
# import time
# time.sleep(10) # timeout error, time out after 5 seconds











