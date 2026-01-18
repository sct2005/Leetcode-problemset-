my_list = [[] for _ in range(10)]
#each element is called a bucket 

#UNICODE -num of each charecter and return a n umber between 0 and 9 

def hash_function(value):
    sum_of_chars = 0 
    for char in value:
        sum_of_chars += ord(char)#B has unicode 66, o has 111, and b has 98. addding those together we get 275
# we take mod 10 of 275 is 5 
    return sum_of_chars %10

print("'Bob' has a hash code:" , hash_function('Bob'))


def add(name):
  index = hash_function(name)
  my_list[index].append(name)

def contains(name):
    index = hash_function(name)
    return my_list[index] == name






add('Bob')
add('Pete')
add('Lisa')
add('Stuart')
print("'Pete' is in the hash table:", contains('Pete'))
print(my_list)
