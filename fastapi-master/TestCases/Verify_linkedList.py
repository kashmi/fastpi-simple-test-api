# Task 2: Problem 1
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def Circular(head):
    if head==None:
        return True
    current = head.next
    i = 0
    while((current is not None) and (current is not head)):
        i = i + 1
        current = current.next

    return(current==head)


node = LinkedList()
node.head = Node(1)
second =  Node(2)
third =  Node(3)
fourth = Node(4)

node.head.next = second
second.next = third
third.next = fourth

if (Circular(node.head)):
    print('The given linked list is a circular list')
else:
    print('The given linked list is not a circular list')
fourth.next = node.head
if (Circular(node.head)):
    print('The given linked list is a circular list')
else:
    print('The given linked list is not a circular list')