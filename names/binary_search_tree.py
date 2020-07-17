"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from stack import Stack
from queue import Queue


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: given value is less than self.value
        #  go to the left block
        if value < self.value:
            # If there is no left child, insert value here
            # the root pointer will now point to this node
            if self.left is None:
                self.left = BSTNode(value)
            # if the left block has a child
            else:
                # now we are in the sub tree.
                self.left.insert(value)  # Recurrsion
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: target is less than self.value
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        # just keep going right until you cannot go any more
        # if that is the only node and no more on the right
        if self.right is None:
            return self.value
            # if there are more nodes on the right
            # we do the same logic again on those sub tree
            # it will continue until it finds the node with
        else:
            return self.right.get_max

    # Call the function `fn` on the value of each node recu
    # this will not return anything

    def for_each(self, fn):
        # this method will want to traverse every tree node
        # this has to call the fn on the self.value
        fn(self.value)
        # if there is a left child call the same fn in the left child
        if self.left:
            self.left.for_each(fn)
        # if there is a right side call the fn on the right child
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return
        # check if we can "move left"
        if self.left is not None:
            self.left.in_order_print(node)
    # visit the node by printing its value
        print(self.value)
# check if we can "move right"
        if self.right is not None:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
    # You should import the queue class from earlier in the
    # week and use that class to implement this method
    # Use a queue to form a "line"
    # for the nodes to "get in"
        queue = Queue()
        queue.enqueue(node)

    # start by placing the root in the queue
    # need a while loop to iterate
    # what are we checking in the while statement?
    # while length of queue is greater than 0
    # dequeue item from front of queue
        while queue.len() > 0:
            current_node = queue.dequeue()


    # print that item
    # place current item's left node in queue if not None
​ if current_node.left:
            queue.enqueue(current_node.left)

           # place current item's right node in queue if not None
        if current_node.right:
                queue.enqueue(current_node.right)
            print(current_node.value

   # Print the value of every node, starting with the given node,
   # in an iterative depth first traversal
   def dft_print(self, node):
       # initialize an empty stack
        # push the root node onto the stack
         stack = Stack()
        stack.push(node)
       # need a while loop to manager our iteration
       # if stack is not empty enter the while loop
           # pop top item off the stack
           # print that item's value
           while stack.len() > 0:
            current_node = stack.pop()
​
           # if there is a right subtree
               # push right item onto the stack
            if current_node.right:
                stack.push(current_node.right)

           # if there is a left subtree
               # push left item onto the stack
             if current_node.left:
                stack.push(current_node.left)
            print(current_node.value)

   # Stretch Goals -------------------------
   # Note: Research may be required

   # Print Pre-order recursive DFT
   def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
