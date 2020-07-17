class RingBuffer:
    def __init__(self, capacity):
        # define capacity
        self.capacity = capacity
        # current_node
        self.current = 0
        # list of None * capacity
        # holds a space to increase number of items in list based on its capacity
        self.storage = [None] * capacity

    def append(self, item):
        # set item passed in to storage's current node
        self.storage[self.current] = item
        # increase current by one
        self.current += 1
        # if the capacity is full
        if self.current >= self.capacity:
            # reset current to 0
            self.current = 0

    def get(self):
        # return all elements in storage that aren't None
        return [x for x in self.storage if x != None]


# https://repl.it/@phillipsdev/Ring-Buffer#main.py
