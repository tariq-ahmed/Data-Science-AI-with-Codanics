# # data structure
# # list
# # define a list

# food = ["rice", "beans", "briyani", "pasta", "pizza", "burger", "fries", "noodles", "chicken", "mutton"]
# # rice etc are string values, list is a data structure. index starts from 0 like rice has index 0, beans has index 1 and so on.

# print(food[0]) # rice
# print(food[1]) # beans
# print(food[-1]) # mutton

# food[0] = "pulao" # rice is replaced by pulao
# print(food[0]) # pulao

# print(food) # ['pulao', 'beans', 'briyani', 'pasta', 'pizza', 'burger', 'fries', 'noodles', 'chicken', 'mutton']

# # 2. tuple

# coordinates = (4.21, 9.11) # tuple is immutable, cannot be changed
# print(coordinates) # (4.21, 9.11)
# print(coordinates[1 ]) # 9.11
# print(coordinates[0]) # 4.21

# # 3. set

# fruit_set = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"} # set is unordered, cannot be accessed by index, the difference between set and list is that set does not allow duplicate values and list allows duplicate values and set is unordered and list is ordered and set is immutable and list is mutable and set is represented by curly braces and list is represented by square brackets and set is used to store unique values and list is used to store multiple values.   
# fruit_set.add("grapes") # add() is used to add a value in set
# print(fruit_set) # {'apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'grapes'}  

# 4. dictionary

car = {"brand": "Ford", "model": "Mustang", "year": 1964} # dictionary is mutable, can be changed
print(car) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(car["model"]) # Mustang
print(car["year"]) # 1964

car["year"] = 2020 # year is changed from 1964 to 2020

print(car) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}    # year is changed from 1964 to 2020








