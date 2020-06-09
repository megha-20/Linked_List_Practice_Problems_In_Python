# A linked list node

class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

# Function to insert the given node into the correct sorted position in
# the given list sorted in increasing order

def SortedInsert(head,newNode):

    # Special case for the head end
    
    if head is None or head.data>=newNode.data:
        newNode.next = head
        head = newNode
        return head
    
    # Locate the node before the poof insertion
    
    current = head
    while current.next and current.next.data <= newNode.data:
        current = current.next

    newNode.next = current.next
    current.next = newNode

    return head
    
# Helper function to print given linked list

def printList(head):
    ptr = head

    while ptr:
        print(ptr.data,end = '-->')
        ptr = ptr.next

    print("None")

Keys = [2,4,6,8]

# points to the head node of the linked list

head = None

# construct linked list

for i in reversed(range(len(Keys))):
    head = Node(Keys[i],head)

head = SortedInsert(head,Node(5))
head = SortedInsert(head,Node(9))
head = SortedInsert(head,Node(1))

# print linked list

printList(head)



# Output: 1-->2-->4-->5-->6-->8-->9-->None
    
