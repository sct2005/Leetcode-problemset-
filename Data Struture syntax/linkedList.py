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



def findLowestValue(head):
     
    lowest_value = head.data#set lowest value to head to start only know value 
    currentNode = head.next #current node is next node 

    while currentNode:
        if currentNode.data < lowest_value:#check if lower than the lowest value 
            lowest_value = currentNode.data#set the node to lowest 
            currentNode = currentNode.next # and change to next node
        else:
            currentNode = currentNode.next#if not qualify as lowest then justr continue to next node 
        
    print(lowest_value)# at the end show what the lowest value is 
    
def deleteSpecificNode(head, nodeToDelete): # pass the head and the node that u want to delete 
  if head == nodeToDelete: # if head off the bat is one to delte return it 
    return head.next

  currentNode = head
  while currentNode.next and currentNode.next != nodeToDelete:#if its not the node to deleet we will ocntinue to traverse 
    currentNode = currentNode.next

  if currentNode.next is None:
    return head#if list only head return head 

  currentNode.next = currentNode.next.next#traverse

  return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deletion:")
traverseAndPrint(node1)

# Delete node4
node1 = deleteSpecificNode(node1, node4)

print("\nAfter deletion:")
traverseAndPrint(node1)
    





