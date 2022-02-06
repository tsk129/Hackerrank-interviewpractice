# # case 
# First the linked list is NULL. After inserting 141, the list is 141 -> NULL.
# After inserting 302, the list is 141 -> 302 -> NULL.
# After inserting 164, the list is 141 -> 302 -> 164 -> NULL.
# After inserting 530, the list is 141 -> 302 -> 164 -> 530 -> NULL. After inserting 474, the list is 141 -> 302 -> 164 -> 530 -> 474 -> NULL, which is the final list.


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

# def print_singly_linked_list(node, sep, fptr):
#     while node:
#         fptr.write(str(node.data))

#         node = node.next

#         if node:
#             fptr.write(sep)

def insertNodeAtTail(head, data):
    tail = head
    node = SinglyLinkedListNode(data)
    if not tail:
        head = node
    else:
        while tail.next:
            tail = tail.next
        tail.next = node
    return head
  
  
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     llist_count = int(input())

#     llist = SinglyLinkedList()

#     for i in range(llist_count):
#         llist_item = int(input())
#         llist_head = insertNodeAtTail(llist.head, llist_item)
#         llist.head = llist_head

#     print_singly_linked_list(llist.head, '\n', fptr)
#     fptr.write('\n')

#     fptr.close()
