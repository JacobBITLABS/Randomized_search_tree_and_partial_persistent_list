import random
from typing import Tuple
from RST.rstNode import RSTNode

class RST():
    """ Randomized Binary Search Tree (RST)"""

    def __init__(self):
        """ Constructor """
        self.root = None
        self.size = 0

    # Function to print binary tree in 2D
    def print2DUtil(self, root, space):
        # Python3 Program to print binary tree in 2D
        COUNT = [8]

        # Base case
        if (root == None):
            return

        # Increase distance between levels
        space += COUNT[0]

        # Process right child first
        self.print2DUtil(root.right, space)

        # Print current node after space
        # count
        print()
        for i in range(COUNT[0], space):
            print(end=" ")
        print(root.key, ":", root.priority)

        # Process left child
        self.print2DUtil(root.left, space)

    # Wrapper over print2DUtil()
    def print2D(self):
        # Pass initial space count as 0
        self.print2DUtil(self.root, 0)

    def right_rotate(self, y: RSTNode):
        """ Rotation """
        x = y.left
        T2 = x.right

        # assign rotation
        x.right = y
        y.left = T2

        # returns new root
        return x

    def left_rotate(self, x: RSTNode):
        """ Rotation """
        y = x.right
        T2 = y.left

        # assign rotation
        y.left = x
        x.right = T2

        # returns new root
        return y

    def _search(self, key: int, root: RSTNode, found_in_depth: int = 0) -> Tuple[RSTNode, int]:
        """ Search on key return node"""
        # handle base case
        if(root is None or key == root.key):
            # dynamically returns the expected, None, Root or found RST Node
            return (root, found_in_depth)

        # key greater than root
        if(root.key < key):
            return self._search(key, root.right, found_in_depth+1)

        # key smaller than root
        return self._search(key, root.left, found_in_depth+1)

    def search(self, key: int):
        """ Search Wrapper """
        return self._search(key=key, root=self.root)

    def _insert(self, key: int, root: RSTNode, priority: int) -> RSTNode:
        """ Recursive Insert """
        if(root == None):
            node = RSTNode(key, priority)
            return node

        # key smaller than root
        if key < root.key:
            # insertion in left subtree
            root.left = self._insert(key, root.left, priority)

            # test and fix heap property [Move UP]
            if(root.left.priority < root.priority):
                root = self.right_rotate(root)

        elif key >= root.key:
            # key is greater -> insertion in right subtree
            root.right = self._insert(key, root.right, priority)

            # test and fix heap property [Move UP]
            if(root.right.priority < root.priority):
                root = self.left_rotate(root)

        return root

    def insert(self, key: int) -> RSTNode:
        """ Insert wrapper """
        new_root = self._insert(key, self.root, random.randint(0, 130000))

        self.size += 1
        self.root = new_root

        return new_root


    def split(self, p_key: int) -> Tuple[RSTNode, RSTNode]:
        # insert key with small priority
        new_root = self._insert(key=p_key, root=self.root, priority=-99)

        #print("new_root, key:", new_root.key, "priority:", new_root.priority)
        L = RST()
        L.root = new_root.left

        R = RST()
        R.root = new_root.right

        self.root = None

        # return left and right subtree as result
        return (L, R)

    @staticmethod
    def merger(A, B):
        if A == None:
            return B
        if B == None:
            return A
        if A.priority > B.priority:
            A.right = RST.merger(A.right, B)
            return A
        else:
            B.left = RST.merger(A, B.left)
            return B

    @staticmethod
    def merge(A_tree, B_tree):
        """ Wrapper """
        # call merger with roots
        T = RST()
        T.root = RST.merger(A_tree.root, B_tree.root)
        # T.print2D()
        return T

    # delete on node
    def delete(self, node: RSTNode, key):
        if node == None:
            return node
        # test movements
        if(key < node.key):
            node.left = self.delete(node.left, key)
        elif(key > node.key):
            node.right = self.delete(node.right, key)

        else:  # we found the node
            print("key we are removeing: ", key)
            print("current node: ", node.key)

            # replace the node with the merge of the nodes children
            node = self.merger(node.left, node.right)
            # return node

        return node

    # instead of split and merge and merge:
    """
    It is possible to split and merge three trees to insert. Two subtres and the new element
    """
    # def add(self, node, newNode):
    #     if newNode.priority > node.priority:
    #         (first, second) = self.split(node, newNode.key)
    #         newNode.left = first
    #         newNode.right = second
    #         return newNode
    #     if newNode.key < node.key:
    #         node.left = self.add(node.left, newNode)
    #     else:
    #         node.right = self.add(node.right, newNode)
    #     return node


if __name__ == "__main__":
    print("[RST]")
    tree = RST()

    tree.insert(0)
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)

    tree.insert(6)
    tree.insert(7)
    tree.insert(8)
    tree.insert(9)
    tree.insert(10)

    # print(tree.root.key)
    # tree.print2D()

    """
    Test Search
    """
    print("\n ")
    for i in range(6):
        print("searching for: ", i+1)
        (s_res, depth) = tree.search(i+1)

        if s_res is not None:
            print("found, ind depth: ", depth)
        else:
            print("not found")

    """
    Test Split
    """
    # print("\n Testing Split")
    # (L, R) = tree.split(5)

    # print("L.")
    # L.print2D()
    # print("R:")
    # R.print2D()

    """
    Test Merge
    """
    # tree1 = RST()
    # tree1.insert(100)

    #print("Testing Merge")
    # tree1.print2D()
    #new_new_tree = RST.merge(tree, tree1)

    """
    Test Delete
    """
    new_tree = tree.delete(tree.root, 3)

    K = RST()
    K.root = new_tree
    K.print2D()
