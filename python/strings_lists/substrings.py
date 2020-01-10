#! /usr/bin/python3

# Write your code here
def is_substring(substring, string):
    for index in range(len(string)):
        if string[index:(index + len(substring))] == substring:
            return True

    return False

# Below are some calls you can use to test it

# This one should return False
print(is_substring('bad', 'abracadabra'))

# This one should return True
print(is_substring('dab', 'abracadabra'))

def count_substring(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index : (index + len(target))] == target:
            total += 1
            index += len(target)   # <- This is the key line
        else:
            index += 1
    return total

# Here's a call you can test it with. This should print 4:
print(count_substring('love, love, love, all you need is love', 'love'))

def locate_first(string, target):
#     total = 0
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
#             total += 1
#             index += len(target)
            return index
        else:
            index += 1
#     return total
    return -1

# Here are a couple function calls to test with.

# This one should return 1
print(locate_first('cookbook', 'ook'))

# This one should return -1
print(locate_first('all your bass are belong to us', 'base'))
-1

def locate_all(string, target):
#     total = 0
    index = 0
    occurence = []
    while index < len(string):
        if string[index : index + len(target)] == target:
            occurence.append(index)
#             total += 1
            index += len(target)
#             return index
        else:
            index += 1
#     return total
#     return -1
    return occurence

# Here are a couple function calls to test with.

# This one should return 1
print(locate_all('cookbook', 'ook'))

# This one should return -1
print(locate_all('all your bass are belong to us', 'base'))
-1
