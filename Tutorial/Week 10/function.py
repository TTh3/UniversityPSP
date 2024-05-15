# Functions Week 10 Tutorial


# Add All numbers
def add_numbers(*numList):
    total = 0
    for num in numList:
        total += num
    return total


result = add_numbers(1, 2, 3, 4)
# print("Result is:", result)


# Find Item
def find_item(my_list, value):
    for val in range(len(my_list)):
        if my_list[val] == value:
            return val
    return -1


my_list = ["I", "love", "python", "programming"]
findingVal = "love"
result = find_item(my_list, findingVal)
# print("Result is:", result)




