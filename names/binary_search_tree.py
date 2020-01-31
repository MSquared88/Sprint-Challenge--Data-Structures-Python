# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare root node
        # if lesser go to left child
        if value < self.value:
            # if no child on that side, insert
            if self.left == None:
                self.left = BinarySearchTree(value)
            # else insert the value with recursion
            else:
                self.left.insert(value)
        # if greater got to right child
        elif value > self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # look at root if target is root return true
        if self.value == target:
            return True

        # if target is less than node, go left
        elif target < self.value:
            if self.left == None:
                return False

            else:
                return self.left.contains(target)

        # if target is more than node, go right
        elif target > self.value:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        # go right till you cant go right no more
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

        # while self.right:
        #     self = self.right
        # return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # call function on current node
        cb(self.value)
        # if there is a right node call for each and pass cb
        if self.right != None:
            self.right.for_each(cb)
        # if there is a LEFT node call for each and pass cb
        if self.left != None:
            self.left.for_each(cb)

    # DAY 2 Project ------------------s-----

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node.value:
            if node.left:
                node.left.in_order_print(node.left)
            print(node.value)
            if node.right:
                node.in_order_print(node.right)
                # if there is a LEFT node call for each and pass cb


    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     # make a queue
    #     q = Queue()
    #     temp = None

    #     # add root to queue
    #     q.enqueue(node)
    #     # while there is stuff in the queue
    #     while q.size > 0:
    #         temp = q.dequeue()
    #         # deque root and save in temp
    #         # DO THE THING!!!!
    #         print(temp.value)

    #         # if temp.left add to queue
    #         if temp.left:
    #             q.enqueue(temp.left)

    #         # if temp.right add to queue
    #         if temp.right:
    #             q.enqueue(temp.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # def dft_print(self, node):
    #     # make a stack
    #     s = Stack()
        
    #     # add root to stack
    #     s.push(node)

    #     #declare temp variable

    #     # while there is stuff in the stack
    #     while s.size > 0:
            
    #         # pop root and save in temp
    #         temp = s.pop()
    #         # DO THE THING!!!!
    #         print(temp.value)

    #         # if temp.left add to stack
    #         if temp.left:
    #             s.push(temp.left)

    #         # if temp.right add to stack
    #         if temp.right:
    #             s.push(temp.right)


# bst = BinarySearchTree(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)
# bst.bft_print(bst)

    # # STRETCH Goals -------------------------
    # # Note: Research may be required

    # # Print In-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
