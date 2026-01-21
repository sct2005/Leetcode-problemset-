my_list = [[] for _ in range(10)]

def hash_function(value):
    sum_of_chars = 0 
    for char in value:
        sum_of_chars += ord(char)
    
    return sum_of_chars %10

def add(name):
    index = hash_function(name)
    if name not in my_list[index]:
        my_list[index].append(name)


def remove(name):
    index = hash_function(name)
    my_list[index].remove(name)

def contains(name):
    index = hash_function(name)
    return name in my_list[index]


