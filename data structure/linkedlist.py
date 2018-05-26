# -*- coding: utf-8 -*-
"""
Practise Bed
by Satyabrata Pradhan
"""

class Node(object):
    def __init__(self,data):
        self.data = data
        self.nextNode = None
        

class linkedlist(object):
    def __init__(self):
        self.head = None
        self.size = 0
        
    def inserStart(self, data):
        self.size = self.size+1
        newNode = Node(data)
        
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
    
    def insertEnd(self, data):
        
        self.size = self.size+1
        newNode = Node(data)
        lastNode = self.head
        
        if lastNode is None:
            self.head = newNode
        else:
            while lastNode.nextNode is not None:
                lastNode = lastNode.nextNode
            lastNode.nextNode=newNode
    
    def removeStart(self):
        if self.size == 0:
            print('Linkedlist is Empty!')
        else:
            self.size = self.size - 1
            self.head = self.head.nextNode
            self.traverse()
            
    def remove(self,data):
        if self.size == 0:
            print('Linkedlist is Empty!')
        else:
            self.size = self.size - 1
            currNode = self.head
            prevNode = None
            flag = False
            
            while currNode.nextNode is not None:
                if currNode.data == data:
                    flag = True
                    if prevNode is None:
                        self.head = currNode.nextNode
                    else:
                        prevNode.nextNode = currNode.nextNode
                    self.traverse()
                    return
                else:
                    prevNode = currNode
                    currNode = currNode.nextNode
                    
            if not flag:
                print('Node not found in Linkedlist')
                
    def traverse(self):
        node = self.head
        
        if not node:
            print('Linkedlist is Empty!')
        else:
            while node is not None:
                print('--> %s '%node.data)
                node = node.nextNode
        
    def size1(self):
        return self.size
    
ll = linkedlist()
ll.traverse()
ll.inserStart(12)
ll.inserStart(20)
ll.inserStart(29)
ll.inserStart(30)
ll.insertEnd(100)

ll.traverse()

ll.remove(50)
ll.remove(20)
ll.removeStart()
ll.removeStart()
ll.removeStart()
ll.removeStart()
ll.removeStart()
ll.removeStart()
ll.removeStart()


