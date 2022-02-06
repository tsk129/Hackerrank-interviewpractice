# Given the pointer to the head node of a linked list, change the next pointers of the nodes so that their order is reversed. The head pointer given may be null meaning that the initial list is empty.

# Example
#  references the list 

# Manipulate the  pointers of each node in place and return , now referencing the head of the list .

# Function Description

# Complete the reverse function in the editor below.

# reverse has the following parameter:

# SinglyLinkedListNode pointer head: a reference to the head of a list
# Returns

# SinglyLinkedListNode pointer: a reference to the head of the reversed list
# Input Format

# The first line contains an integer , the number of test cases.

# Each test case has the following format:

# The first line contains an integer , the number of elements in the linked list.
# Each of the next  lines contains an integer, the  values of the elements in the linked list.

# Constraints

# , where  is the  element in the list.

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


def reverse(llist):
    # Write your code here
    head = llist
    if not head:
        return
    pre = None
    cur = head
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    head = pre
    return head
  
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     tests = int(input())

#     for tests_itr in range(tests):
#         llist_count = int(input())

#         llist = SinglyLinkedList()

#         for _ in range(llist_count):
#             llist_item = int(input())
#             llist.insert_node(llist_item)

#         llist1 = reverse(llist.head)

#         print_singly_linked_list(llist1, ' ', fptr)
#         fptr.write('\n')

#     fptr.close()
