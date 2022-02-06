# You are given the pointer to the head node of a sorted linked list, where the data in the nodes is in ascending order. Delete nodes and return a sorted list with each distinct value in the original list. The given head pointer may be null indicating that the list is empty.

# Example

#  refers to the first node in the list .

# Remove 1 of the  data values and return  pointing to the revised list .

# Function Description

# Complete the removeDuplicates function in the editor below.

# removeDuplicates has the following parameter:

# SinglyLinkedListNode pointer head: a reference to the head of the list
# Returns

# SinglyLinkedListNode pointer: a reference to the head of the revised list
# Input Format

# The first line contains an integer , the number of test cases.

# The format for each test case is as follows:

# The first line contains an integer , the number of elements in the linked list.
# Each of the next  lines contains an integer, the  value for each of the elements of the linked list.

# Constraints



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


def removeDuplicates(llist):
    # Write your code here
    head = llist
    if not llist:
        return
    if not llist.next:
        return llist
    while head.next:
        temp = head.next
        while temp.next and head.data == temp.data:
            head.next = temp.next
            temp = temp.next
        if not temp.next and head.data == temp.data:
            head.next = None
        if head.next:
            head = head.next
    return llist
  
  
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input())

#     for t_itr in range(t):
#         llist_count = int(input())

#         llist = SinglyLinkedList()

#         for _ in range(llist_count):
#             llist_item = int(input())
#             llist.insert_node(llist_item)

#         llist1 = removeDuplicates(llist.head)

#         print_singly_linked_list(llist1, ' ', fptr)
#         fptr.write('\n')

#     fptr.close()
