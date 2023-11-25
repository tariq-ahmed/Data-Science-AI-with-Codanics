# Nested for Loops: 
# A nested for loop is a for loop that is contained within another for loop.
#  This means that the inner for loop will be executed multiple times
#  for each iteration of the outer for loop.

# colors = ["red", "greeen", "blue"]
# items = ["book", "pen", "pencil"]

# for color in colors:
#     for item in items:
#         print(color, item)

# nested while loops, while loop inside while loop 

# i = 0
# while i < 3:
#     j = 0
#     while j < 3:
#         print(i, j)
#         j += 1
#     i += 1


# # for loop inside while loop

# i = 1 
# while i < 3:
#     for j in range(3):
#         print(i, j)
#     i += 1

# while loop inside for loop

for i in range(3):
    j = 0
    while j < 3:
        print(i, j)
        j += 1
    i += 1
