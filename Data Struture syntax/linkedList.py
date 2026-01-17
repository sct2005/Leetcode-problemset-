#Linked list 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end= " ->") #pritn the data of the node
        currentNode = currentNode.next# and change the next node to this node 
    print("null")

def traverse(head):
    currentNode = head
    while currentNode:
        currentNode = currentNode.next
    print("finished")

def findLowestValue(head):
     
    lowest_value = head.data
    currentNode = head.next

    while currentNode:
        if currentNode.data < lowest_value:
            lowest_value = currentNode.data
            currentNode = currentNode.next
        else:
            currentNode = currentNode.next
        
    print(lowest_value)
    







node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

findLowestValue(node1)
