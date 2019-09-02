# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:08:29 2019

@author: Lori
"""

class Node :
    def __init__(self , val= None ):
        self.val=val
        self.link=None
class LinkedList :
    def __init__( self ):
        self.head=None
        
    def insert_pos(self,pos,val ):
         if pos > 0:
             current_node=self.head
             for count in range(pos -1):
                 current_node=current_node.link
             next_link=current_node.link
             current_node.link=Node(val)
             current_node.link.link=next_link
         else:
            next_link=self.head
            self.head=Node(val)
            self.head.link=next_link
            
    def delete_pos(self,pos):
        if pos > 0:
            current_node=self.head
            for count in range(pos- 1):
                current_node=current_node.link
                current_node.link=current_node.link.link
        else :
            self.head=self.head.link
            
    def printlist(self):
        current_node=self.head
        while current_node !=None:
            print(current_node.val)
            current_node=current_node.link
            
    def update_pos(self,pos,val):
        current_node=self.head
        for count in range(pos):
            current_node=current_node.link
        current_node.val=val
    def append(self,val ):
        current_node=self.head
        while current_node.link !=None:
            current_node=current_node.link
        current_node.link=Node(val)
        
my_list=LinkedList()
my_list.head=Node(10)

n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)
my_list.head.link=n2
n2.link=n3
n3.link=n4
n4.link=n5
my_list=LinkedList()
my_list.head=Node(10)
my_list.append(30)
my_list.append(100)
my_list.printlist()
my_list=LinkedList()
my_list.head=Node(10)
my_list.delete_pos(3)
my_list.printlist()
my_list=LinkedList()
my_list.head=Node(5)

my_list.insert_pos(2,15)

my_list.printlist()


