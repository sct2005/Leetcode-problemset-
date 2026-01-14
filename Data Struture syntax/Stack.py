

class Stack():

    def __init__(self):
        self.stack = []

    def push(self,element):#pass the stack and elemet appending if u dont specife the posiion append goes at end or in our case the top 
        self.stack.append(element)


    def pop(self):
        if self.isEmpty():#check empty top avoid erros 
            return "Stack is empty"
        else:
            return self.stack.pop()#normal pop operation 
    
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.stack[-1]#last eleemtnin a list in case of stack thats the top 
        
    def empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
