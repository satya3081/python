# -*- coding: utf-8 -*-
"""
Created on Fri May 25 21:04:52 2018
Practise Bed
by Satyabrata Pradhan

@author: Satya
"""


class Queue(object):
    
    def __init__(self):
        self.queue = []
        
    def isEmpty(self):
        return self.queue == []
    
    def enqueue(self, data):
        self.queue.append(data)
        
    def dequeue(self):
        if self.isEmpty():
            return None
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        data = self.queue[0]
        return data

queue = Queue()

print("dequeue %s" %queue.dequeue())

