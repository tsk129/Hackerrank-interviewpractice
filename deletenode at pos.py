# Delete the node at a given position in a linked list and return a reference to the head node. The head is at position 0. The list may be empty after you delete the node. In that case, return a null value.

# Example



# After removing the node at position , .

# Function Description

# Complete the deleteNode function in the editor below.

# deleteNode has the following parameters:
# - SinglyLinkedListNode pointer llist: a reference to the head node in the list
# - int position: the position of the node to remove

# Returns
# - SinglyLinkedListNode pointer: a reference to the head of the modified list
  
  
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


def deleteNode(llist, position):
    # Write your code here
    head = llist
    cur = head
    if not head:
        return None
    else:
        c = 0
        while c!=position:
            pre = cur
            cur = cur.next
            c += 1
        pre.next = cur.next
    return head
  
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     llist_count = int(input())

#     llist = SinglyLinkedList()

#     for _ in range(llist_count):
#         llist_item = int(input())
#         llist.insert_node(llist_item)

#     position = int(input())

#     llist1 = deleteNode(llist.head, position)

#     print_singly_linked_list(llist1, ' ', fptr)
#     fptr.write('\n')

#     fptr.close()
