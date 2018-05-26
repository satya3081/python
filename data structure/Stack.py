# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:33:47 2018
Practise Bed
by Satyabrata Pradhan

@author: Satya
"""

class Stack(object):
    
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return self.stack == []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    def peek(self):
        data = self.stack[-1]
        return data
    
    def checkSize(self):
        return len(self.stack)

stack = Stack()

print('Size of stack is %d' %stack.checkSize())

stack.push(1)
stack.push(3)
stack.push(7)

print('Size of stack is %d' %stack.checkSize())

stack.pop()
stack.pop()

print('Size of stack is %d' %stack.checkSize())

stack.pop()

print('Size of stack is %d' %stack.checkSize())