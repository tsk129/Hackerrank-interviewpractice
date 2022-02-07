# Reverse a doubly linked list

# Given the pointer to the head node of a doubly linked list, reverse the order of the nodes in place. That is, change the next and prev pointers of the nodes so that the direction of the list is reversed. Return a reference to the head node of the reversed list.

# Note: The head node might be NULL to indicate that the list is empty.

# Function Description

# Complete the reverse function in the editor below.

# reverse has the following parameter(s):

# DoublyLinkedListNode head: a reference to the head of a DoublyLinkedList
# Returns
# - DoublyLinkedListNode: a reference to the head of the reversed list

# Input Format

# The first line contains an integer , the number of test cases.

# Each test case is of the following format:

# The first line contains an integer , the number of elements in the linked list.
# The next  lines contain an integer each denoting an element of the linked list.
# Constraints

# Output Format

# Return a reference to the head of your reversed list. The provided code will print the reverse array as a one line of space-separated integers for each test case.


# import math
# import os
# import random
# import re
# import sys

# class DoublyLinkedListNode:
#     def __init__(self, node_data):
#         self.data = node_data
#         self.next = None
#         self.prev = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def insert_node(self, node_data):
#         node = DoublyLinkedListNode(node_data)

#         if not self.head:
#             self.head = node
#         else:
#             self.tail.next = node
#             node.prev = self.tail


#         self.tail = node

# def print_doubly_linked_list(node, sep, fptr):
#     while node:
#         fptr.write(str(node.data))

#         node = node.next

#         if node:
#             fptr.write(sep)



def reverse(llist):
    # Write your code here
    temp = None
    cur = llist
    
    while cur:
        temp = cur.prev
        cur.prev = cur.next
        cur.next = temp
        cur = cur.prev
    if temp:
        llist = temp.prev
    return llist
  
  
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input())

#     for t_itr in range(t):
#         llist_count = int(input())

#         llist = DoublyLinkedList()

#         for _ in range(llist_count):
#             llist_item = int(input())
#             llist.insert_node(llist_item)

#         llist1 = reverse(llist.head)

#         print_doubly_linked_list(llist1, ' ', fptr)
#         fptr.write('\n')

#     fptr.close()
