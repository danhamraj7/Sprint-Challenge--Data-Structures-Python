"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from singly_linked_list import LinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # 2. use LinkedList as storage
        # 3. on initialization head & tail = none
        self.storage = LinkedList()

        # 1. use array as storage
        # self.storage = []


# if we try to find out the length of a queue it will return the
# size variable.

    def __len__(self):
        return self.size

        # 1. use array as storage
        # self.storage.append(value)
        # self.size += 1

        # 2. use LinkedList as storage
        # 3. this is adding to the tail of the link list.

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

        # 1. use array as storage
        # if self.size == 0:
        #     return None
        # else:
        #     value = self.storage[0]
        #     self.storage.remove(value)
        #     self.size -= 1
        #     return value
        # 2. use LinkedList as storage
        # 3. This will remove a node from the head of the link list.

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()

# a queue is like a line in the bank or super market checkout
# when you join the line you wait for the persons in front of
# you to be attended to first.
# so when you add to the queue it is added to the tail
# when you remove it is from the head.
