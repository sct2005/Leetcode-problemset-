#LeetCode 225 - implement a stack using queues

#LIFO queue -- opertions = puch , popremove top  , top(top element) , empty
# use dequeue  - no indexing - queue operations only 

from collections import deque

class MyStack:

    def __init__(self):# the constructer runs automatically whenever you create a new instance of the class , sets up variables or data strutures
        #that will be used later 
    
        self.q = deque

    def push(self, x: int) -> None:
        #push element x on stack, in queue based u hhave to re structure the queue,so last element becomes the top 
        pass

    def pop(self) -> int:
        pass#remocves top element and returns it , only queue operations (append,pop;est ) should be used

    def top(self) -> int:
        pass # returns top element without removing it 

    def empty(self) -> bool:# return true if empty 
        return not self.q
