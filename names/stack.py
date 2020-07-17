from singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self.size = 0  # keeping track of size
        # 2. use LinkedList as storage
        # To initialize a new stack,set the attr to be an empty
        # linked list. empty link list consist of head & tail = none
        self.storage = LinkedList()

        # 1. use array as storage
        # self.storage = []

    def __len__(self):
        return self.size

        # 1. use array as storage
        # self.size += 1
        # self.storage.append(value)
        # 2. use LinkedList as storage

    def push(self, value):
        self.size += 1  # increment size
        self.storage.add_to_tail(value)  # push the value

        # 1. use array as storage
        # if self.size == 0:
        #     return None
        # else:
        #     self.size -= 1
        #     return self.storage.pop()
        # 2. use LinkedList as storage

    def pop(self):
        if self.size == 0:  # if the stack has no items return none.
            return None
        else:
            self.size -= 1
            return self.storage.remove_tail()


# the idea of stacks logic is:
# add to the tail and increment the size
# remove from the tail and decrement the size.
# when the stack has no items in it we return none.
# you could think of stack as dishes in a resturant after they
# are wash and stacked 1 on top the other.
