# Given the pointer to the head node of a linked list and an integer to insert at a certain position, create a new node with the given integer as its  attribute, insert this node at the desired position and return the head node.

# A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.

# Example
#  refers to the first node in the list 


# Insert a node at position  with . The new list is 

# Function Description Complete the function insertNodeAtPosition in the editor below. It must return a reference to the head node of your finished list.

# insertNodeAtPosition has the following parameters:

# head: a SinglyLinkedListNode pointer to the head of the list
# data: an integer value to insert as data in your new node
# position: an integer position to insert the new node, zero based indexing
# Returns

# SinglyLinkedListNode pointer: a reference to the head of the revised list

  
  
# import math
# import os
# import random
# import re
# import sys

# class SinglyLinkedListNode:
#     def __init__(self, node_data):
#         self.data = node_data
#         self.next = None

# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def insert_node(self, node_data):
#         node = SinglyLinkedListNode(node_data)

#         if not self.head:
#             self.head = node
#         else:
#             self.tail.next = node


#         self.tail = node

# def print_singly_linked_list(node, sep, fptr):
#     while node:
#         fptr.write(str(node.data))

#         node = node.next

#         if node:
#             fptr.write(sep)


def insertNodeAtPosition(llist, data, position):
    # Write your code here
    node = SinglyLinkedListNode(data)
    head = llist
    cur = head
    if not head:
        head = node
    else:
        c = 0
        while c!=position:
            pre = cur
            cur = cur.next
            c += 1
        pre.next = node
        node.next = cur
    return head

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     llist_count = int(input())

#     llist = SinglyLinkedList()

#     for _ in range(llist_count):
#         llist_item = int(input())
#         llist.insert_node(llist_item)

#     data = int(input())

#     position = int(input())

#     llist_head = insertNodeAtPosition(llist.head, data, position)

#     print_singly_linked_list(llist_head, ' ', fptr)
#     fptr.write('\n')

#     fptr.close()
