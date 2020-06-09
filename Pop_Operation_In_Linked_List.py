# A linked list node

class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
        
# The opposite of Push().Takes a non-empty list and removes the front
# node, and prints the data which was in that node.

def pop(headRef):

    if headRef is None:
        return None

    result = headRef.data   # pull out data before node is deleted
    headRef = headRef.next  # unlink the head node for the caller

    print("popped node is ",result)

    return headRef

# Helper function to print given linked list

def printList(head):

    ptr = head

    while ptr:
        print(ptr.data,end = '-->')
        ptr = ptr.next

    print("None")


# points to the head node of the linked list

head = None

# construct linked list

for i in reversed(range(1,5)):
    head = Node(i,head)

head = pop(head)

# print remaining linked list

printList(head)



# Output: Popped node is 1
#         2-->3-->4-->None
