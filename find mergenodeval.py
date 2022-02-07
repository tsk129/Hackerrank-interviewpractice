# Find Merge Point of Two Lists

# Given pointers to the head nodes of  linked lists that merge together at some point, find the node where the two lists merge. The merge point is where both lists point to the same node, i.e. they reference the same memory location. It is guaranteed that the two head nodes will be different, and neither will be NULL. If the lists share a common node, return that node's  value.

# Note: After the merge point, both lists will share the same node pointers.

# Example

# In the diagram below, the two lists converge at Node x:

# [List #1] a--->b--->c
#                      \
#                       x--->y--->z--->NULL
#                      /
#      [List #2] p--->q
# Function Description

# Complete the findMergeNode function in the editor below.

# findMergeNode has the following parameters:

# SinglyLinkedListNode pointer head1: a reference to the head of the first list
# SinglyLinkedListNode pointer head2: a reference to the head of the second list
# Returns

# int: the  value of the node where the lists merge
# Input Format

# Do not read any input from stdin/console.

# The first line contains an integer , the number of test cases.

# Each of the test cases is in the following format:
# The first line contains an integer, , the node number where the merge will occur.
# The next line contains an integer,  that is the number of nodes in the first list.
# Each of the following  lines contains a  value for a node. The next line contains an integer,  that is the number of nodes in the second list.
# Each of the following  lines contains a  value for a node.

# Constraints

# The lists will merge.
# .
#  .
      
      
      
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


def findMergeNode(head1, head2):
    while head1:
        node = head2
        while node:
            if head1 == node:
                return head1.data
            node = node.next
        head1 = head1.next
        
  
#   if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     tests = int(input())

#     for tests_itr in range(tests):
#         index = int(input())

#         llist1_count = int(input())

#         llist1 = SinglyLinkedList()

#         for _ in range(llist1_count):
#             llist1_item = int(input())
#             llist1.insert_node(llist1_item)
            
#         llist2_count = int(input())

#         llist2 = SinglyLinkedList()

#         for _ in range(llist2_count):
#             llist2_item = int(input())
#             llist2.insert_node(llist2_item)
            
#         ptr1 = llist1.head;
#         ptr2 = llist2.head;

#         for i in range(llist1_count):
#             if i < index:
#                 ptr1 = ptr1.next
                
#         for i in range(llist2_count):
#             if i != llist2_count-1:
#                 ptr2 = ptr2.next

#         ptr2.next = ptr1

#         result = findMergeNode(llist1.head, llist2.head)

#         fptr.write(str(result) + '\n')

#     fptr.close()
