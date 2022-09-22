# Write a program to implement Doubly linked list with Insertion,Traversal, Deletion operation.
# self calls data
# init initialises the link
# doubly linked list goes both ways: forward and backwards
# pointer on both ends points to none
# item: data we enter
# nest- next link
# prev- previous link
# new_node= Node(Data) - new node

class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

# class for doubly linked list
class doublyLinkedList:
    def __init__(self):
        self.start_node = None

    # Insert element to empty list
    def InsertToEmptyList(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is empty")

    # Insert Element at the end\
    def InsertToEnd(self, data):
        # Check if list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        # iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n  # n is last node

    # Delete the elements from the start
    def DeleteAtStart(self):
        if self.start_node is None:
            print("the linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next  # head pointing to next node
        self.start_prev = None

        # Delete the elements from the end
    def delete_at_end(self):
        # Check if the list is empty
        if self.start_node is None:
            print("The linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None  # 2nd last node previous is none

    # Traversing and Displaying each element of the list
    def Display(self):
        if self.start_node is None:
            print("the list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is:", n.item)
                n = n.next
        print(" ")

# Create a new Doubly Linked List
NewDoublyLinkedList = doublyLinkedList()
# Insert the element to empty list
NewDoublyLinkedList.InsertToEmptyList(10)
# Insert the element at the end
NewDoublyLinkedList.InsertToEnd(20)
NewDoublyLinkedList.InsertToEnd(30)
NewDoublyLinkedList.InsertToEnd(40)
NewDoublyLinkedList.InsertToEnd(50)
NewDoublyLinkedList.InsertToEnd(60)
# Display data
NewDoublyLinkedList.Display()
# Delete  elements from start
NewDoublyLinkedList.DeleteAtStart()
# Delete elements  from end
NewDoublyLinkedList.delete_at_end()
# Display data
NewDoublyLinkedList.Display()