s = "anagram"

t = "nagaram"


def anagram (s,t):
    if sorted(s) == sorted(t):  #--- sorted will just sort them in alpahbetical order
        print(True)#- so if truly an anagram once sorted it should be the same 
    else:
        print(False)


anagram(s,t)


#another aproach 


'''
class ListNode:
    def __init__(self, key, val, nxt):
        self.key = key # key
        self.val = val #value for key 
        self.next = nxt # next linked node 
class MyHashMap:
    def __init__(self):
        self.size = 5 #number of buckets in hash map
        self.mult = 234567 # large number used to spread the keys across buckets
        self.data = [None for _ in range(self.size)] # creates array of empty buckets 


    def hash(self, key): #convert a key into an index inour array 
        return key * self.mult% self.size

    def put(self, key, val):

        # If the key already exists, remove it first
        # This prevents duplicate keys
        self.remove(key)

        # Find which bucket this key belongs to
        h = self.hash(key)

        # Create a new node
        # The new node points to whatever was previously
        # at this bucket
        node = ListNode(key, val, self.data[h])

        # Make the new node the first node in the bucket
        self.data[h] = node

    # Find the value associated with a key
    def get(self, key):

        # Find the bucket for this key
        h = self.hash(key)

        # Start at the first node in that bucket
        node = self.data[h]

        # Search through the linked list
        while node:

            # Found the key
            if node.key == key:
                return node.val

            # Move to the next node
            node = node.next

        # Key wasn't found
        return -1

    # Remove a key-value pair
    def remove(self, key: int):

        # Find the bucket containing this key
        h = self.hash(key)

        # Start at the first node
        node = self.data[h]

        # Bucket is empty
        if not node:
            return

        # If the first node contains the key,
        # remove it by moving the bucket to the next node
        if node.key == key:
            self.data[h] = node.next
            return

        # Otherwise search through the linked list
        while node.next:

            # Check the NEXT node
            if node.next.key == key:

                # Skip over the node we want to delete
                node.next = node.next.next
                return

            # Move forward through the list
            node = node.next

'''

s = "anagram"
t = "nagaram"

class Soultion:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = {}

        for char in s: 
            if char in count:
                count[char] += 1
            else:
                count[char] = 1 

        for char in t:

            if char not in count:
                return False

            count[char] -= 1 

            if count[char] < 0:
                return False

        return True

# if they are not the same length there false , create a dictinory to keep counts of charecters, if its in there increase the count else we will add letter to dict


'''
class ListNode:
    def __init__(self, key, val, nxt):
        self.key = key # key
        self.val = val #value for key 
        self.next = nxt # next linked node 
class MyHashMap:
    def __init__(self):
        self.size = 5 #number of buckets in hash map
        self.mult = 234567 # large number used to spread the keys across buckets
        self.data = [None for _ in range(self.size)] # creates array of empty buckets 


    def hash(self, key): #convert a key into an index inour array 
        return key * self.mult% self.size

    def put(self, key, val):

        # If the key already exists, remove it first
        # This prevents duplicate keys
        self.remove(key)

        # Find which bucket this key belongs to
        h = self.hash(key)

        # Create a new node
        # The new node points to whatever was previously
        # at this bucket
        node = ListNode(key, val, self.data[h])

        # Make the new node the first node in the bucket
        self.data[h] = node

    # Find the value associated with a key
    def get(self, key):

        # Find the bucket for this key
        h = self.hash(key)

        # Start at the first node in that bucket
        node = self.data[h]

        # Search through the linked list
        while node:

            # Found the key
            if node.key == key:
                return node.val

            # Move to the next node
            node = node.next

        # Key wasn't found
        return -1

    # Remove a key-value pair
    def remove(self, key: int):

        # Find the bucket containing this key
        h = self.hash(key)

        # Start at the first node
        node = self.data[h]

        # Bucket is empty
        if not node:
            return

        # If the first node contains the key,
        # remove it by moving the bucket to the next node
        if node.key == key:
            self.data[h] = node.next
            return

        # Otherwise search through the linked list
        while node.next:

            # Check the NEXT node
            if node.next.key == key:

                # Skip over the node we want to delete
                node.next = node.next.next
                return

            # Move forward through the list
            node = node.next

'''

s = "anagram"
t = "nagaram"

class Soultion:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = {}

        for char in s: 
            if char in count:
                count[char] += 1
            else:
                count[char] = 1 

        for char in t:

            if char not in count:
                return False

            count[char] -= 1 

            if count[char] < 0:
                return False

        return True

# if they are not the same length there false , create a dictinory to keep counts of charecters, if its in there increase the count else we will add letter to dict




