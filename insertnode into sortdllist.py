# Inserting a Node Into a Sorted Doubly Linked List


# Given a reference to the head of a doubly-linked list and an integer, , create a new DoublyLinkedListNode object having data value  and insert it at the proper location to maintain the sort.

# Example

#  refers to the list 

# Return a reference to the new list: .

# Function Description

# Complete the sortedInsert function in the editor below.

# sortedInsert has two parameters:

# DoublyLinkedListNode pointer head: a reference to the head of a doubly-linked list

# int data: An integer denoting the value of the  field for the DoublyLinkedListNode you must insert into the list.

# Returns

# DoublyLinkedListNode pointer: a reference to the head of the list
# Note: Recall that an empty list (i.e., where ) and a list with one element are sorted lists.

# Input Format

# The first line contains an integer , the number of test cases.

# Each of the test case is in the following format:

# The first line contains an integer , the number of elements in the linked list.
# Each of the next  lines contains an integer, the data for each node of the linked list.
# The last line contains an integer, , which needs to be inserted into the sorted doubly-linked list.
# Constraints



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



def sortedInsert(llist, data):
    # Write your code here
    node = DoublyLinkedListNode(data)
    if not llist:
        llist = node
        return llist
    if not llist.next:
        if llist.data<node.data:
            llist.next = node
            node.prev = llist
        else:
            node.next = llist
            llist.prev = node
            llist = node
        return llist
    cur = llist
    if cur.data>node.data:
        node.next = llist
        llist = node
        return llist
    while cur and cur.data<node.data:
        pre = cur
        if cur.next:
            cur = cur.next
        else:
            cur = None
    pre.next = node
    node.prev = pre
    node.next = cur
    if cur:
        cur.prev = node
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

#         data = int(input())

#         llist1 = sortedInsert(llist.head, data)

#         print_doubly_linked_list(llist1, ' ', fptr)
#         fptr.write('\n')

#     fptr.close()
