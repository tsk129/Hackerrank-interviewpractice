# Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. Either head pointer may be null meaning that the corresponding list is empty.

# Example
#  refers to 
#  refers to 

# The new list is 

# Function Description

# Complete the mergeLists function in the editor below.

# mergeLists has the following parameters:

# SinglyLinkedListNode pointer headA: a reference to the head of a list
# SinglyLinkedListNode pointer headB: a reference to the head of a list
# Returns

# SinglyLinkedListNode pointer: a reference to the head of the merged list
# Input Format

# The first line contains an integer , the number of test cases.

# The format for each test case is as follows:

# The first line contains an integer , the length of the first linked list.
# The next  lines contain an integer each, the elements of the linked list.
# The next line contains an integer , the length of the second linked list.
# The next  lines contain an integer each, the elements of the second linked list.

# Constraints

# , where  is the  element of the list.


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


def mergeLists(head1, head2):
    temp = SinglyLinkedListNode(None)
    head = temp
    while head1 and head2:
        if head1.data < head2.data:
            head.next = head1
            head1 = head1.next
        else:
            head.next = head2
            head2 = head2.next
        head = head.next
    if head1:
        head.next = head1
    if head2:
        head.next = head2
    return temp.next
  
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     tests = int(input())

#     for tests_itr in range(tests):
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

#         llist3 = mergeLists(llist1.head, llist2.head)

#         print_singly_linked_list(llist3, ' ', fptr)
#         fptr.write('\n')

#     fptr.close()
