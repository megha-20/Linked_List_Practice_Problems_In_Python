# A linked list node

class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
        
# Function that takes a linked list and returns a complete copy of that

def copyList(head):
    
    current = head  # used to iterate over original list
    newList = None  # head of the list
    tail = None     # point to last node in list

    while current:

        # special case for the first node
        
        if newList is None:
            newList = Node(current.data,newList) # add each node at tail
            tail = newList # advance the tail to last node

        else:
            tail.next = Node(current.data,tail.next)
            tail = tail.next
            
        current = current.next
    return newList

# Helper function to print given linked list

def printList(head):
    
    ptr = head
    
    while ptr:
        print(ptr.data,end = '-->')
        ptr = ptr.next

    print(None)
    
# construct linked list

head = None

for i in reversed(range(4)):
    head = Node(i+1,head)
    
# copy linked list

dup = copyList(head)

# print duplicate linked list

printList(dup)






# Output: 1-->2-->3-->4-->None
    
