class Node:
    
    def __init__(self, val=None):
        self.val = val
        self.link = None
class LinkedList:
    
    def __init__ (self):
        self.head = None
        
    def printlist(self):

        current_node=self.head

        while current_node !=None:

            print(current_node.val)

            current_node=current_node.link
   
        
    def insert_pos(self,pos,val):
        if pos> 0:
            current_node = self.head
            for count in range (pos -1):
                current_node = current_node.link
            next_link = current_node.link
            current_node.link = Node (val)
            current_node.link.link = next_link
    def update_pos(self,pos,val):
        current_node = self.head
        for count in range (pos):
            current_node.val = val
            
    def delete_pos(self,pos):
        if pos > 0:
            current_node = self.head
            for count in range (pos - 1):
                current_node = current_node.link
            current_node.link = current_node.link.link
        else:
            self.head = self.head.link
            
   
n1=Node(10)#assign value inside node1
n2=Node(20)#assign value inside node2
n3=Node(30)#assign value inside node3
n4=Node(40)
n5=Node(50)
print(n1.val)#prints value inside node
print(n2.val)
print(n3.val)
print(n4.val)
print(n5.val)
print("\n")#creates a space between lines of code so this is easier to follow


my_list=LinkedList()
my_list.head =Node(10)
n2 =Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)


my_list.head.link =n2
n2.link=n3
n3.link=n4
n4.link=n5

print("\n")#creates a space between lines of code so this is easier to follow

n3.val=100
my_list.printlist()
print("\n")#creates a space between lines of code so this is easier to follow

#deleting from a linked list
my_list.delete_pos(3)
my_list.printlist()
print("\n")#creates a space between lines of code so this is easier to follow

my_list.insert_pos(1,15)
my_list.printlist()
print("\n")#creates a space between lines of code so this is easier to follow    
