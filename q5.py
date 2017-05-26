'''
Question 5

Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
'''


class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

# Added for test cases for ques5 with a newly defined linked list
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

def ques5(ll, m):
    count = 1
    head = ll
    current = head

    # Find the length of the Linked List
    while current.next:
        current = current.next
        count += 1

    # Depth of the mth element from the end of the Linked List
    '''
    Note that two is added to the depth to account for the last element and
    the mth element as elements in part of the caluation to finding from the mth element
    from the end of the linked List
    '''
    depth = count - m
    depth += 2

    # Reset current to the first node
    current = head

    for i in range(1, depth):
        current = current.next

    return current

# Test cases #################################
# Set up some Elements
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

# Start setting up a LinkedList
ll = LinkedList(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)
ll.append(n5)
##############################################
