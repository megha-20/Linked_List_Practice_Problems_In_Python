# A linked list node

class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

# Function that takes a linked list and returns a complete copy of that
# list using dummy node

def copyList(head):
    current = head
    dummy = Node()
    tail = dummy

    while current:
        tail.next = Node(current.data,tail.next)
        tail = tail.next
        current = current.next

    return dummy.next

# Helper function to print given linked list

def printList(head):

    ptr = head
    while ptr:
        print(ptr.data,end='-->')
        ptr = ptr.next

    print("None")

# construct linked list

head = None
for i in reversed(range(4)):
    head = Node(i+1,head)

# copy linked list
               
dup = copyList(head)

# print duplicate linked list
               
printList(dup)               
