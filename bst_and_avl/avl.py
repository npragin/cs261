# Name: Noah Pragin
# OSU Email: npragin@gmail.com
# Course: CS261 - Data Structures
# Assignment: BST/AVL Tree Implementation
# Due Date: 07/29/2024
# Description: An AVL Tree implementation based on my BST


import random

from bst import BST, BSTNode
from queue_and_stack import Queue, Stack


class AVLNode(BSTNode):
    """
    AVL Tree Node class. Inherits from BSTNode
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(value)

        # new variables needed for AVL
        self.parent = None
        self.height = 0

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return "AVL Node: {}".format(self.value)


class AVL(BST):
    """
    AVL Tree class. Inherits from BST
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(start_tree)

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        super()._str_helper(self._root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                # check for correct height (relative to children)
                left = node.left.height if node.left else -1
                right = node.right.height if node.right else -1
                if node.height != 1 + max(left, right):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self._root:
                        return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Adds a new value to the tree while maintaining its AVL property
        """
        if self._root is None:  # Handle empty tree
            self._root = AVLNode(value)
            return

        newNode = self._insert(self._root, value)

        while newNode:  # Maintain the AVL property
            self._rebalance(newNode)
            newNode = newNode.parent

    def remove(self, value: object) -> bool:
        """
        Removes value from AVL tree; Returns True if value is removed. Otherwise, False
        """
        itr = self._root
        while itr:  # Iterate through tree to find value
            if value == itr.value:
                break
            elif value < itr.value:
                itr = itr.left
            else:
                itr = itr.right

        if itr is None:
            return False
        elif itr.left and itr.right:
            itr = self._remove_two_subtrees(itr)
        elif itr.left or itr.right:
            itr = self._remove_one_subtree(itr)
        else:
            self._remove_no_subtrees(itr.parent, itr)

        while itr:
            self._rebalance(itr)
            itr = itr.parent

        return True

    def _remove_one_subtree(self, remove_node: BSTNode) -> AVLNode:
        """
        Remove node that has a left or right subtree (only)
        """
        child = remove_node.left or remove_node.right  # Non-None child

        if remove_node.parent is None:
            self._root = child  # Returns non-None
        elif remove_node.parent.left is remove_node:
            remove_node.parent.left = child
        elif remove_node.parent.right is remove_node:
            remove_node.parent.right = child
        else:
            raise BaseException("_remove_one_subtree ", remove_node)

        if child:
            child.parent = remove_node.parent

        return remove_node.parent

    def _remove_two_subtrees(self, remove_node: AVLNode) -> AVLNode:
        """
        Remove node that has two subtrees
        """
        itr = remove_node.right
        while itr.left:  # Get left-most value in right subtree to replace remove_node
            itr = itr.left

        remove_node.value = itr.value

        if itr.parent.left is itr:
            itr.parent.left = itr.right
        elif itr.parent.right is itr:
            itr.parent.right = itr.right
        else:
            raise BaseException("_remove_two_subtrees")

        if itr.right:
            itr.right.parent = itr.parent

        return itr.parent

    def _insert(self, node: AVLNode, value: object) -> AVLNode:
        """
        Recursively inserts a value in the tree and returns the inserted node
        """
        if value < node.value:
            if node.left is None:
                node.left = AVLNode(value)
                node.left.parent = node
                return node.left
            return self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = AVLNode(value)
                node.right.parent = node
                return node.right
            return self._insert(node.right, value)

    def _balance_factor(self, node: AVLNode) -> int:
        """
        Returns the balance factor of a node.
        """
        rightHeight = leftHeight = -1
        if node.right:
            rightHeight = node.right.height
        if node.left:
            leftHeight = node.left.height
        return rightHeight - leftHeight

    def _get_height(self, node: AVLNode) -> int:
        """
        Returns the height of a node.
        """
        if node is None:
            return -1
        return max(self._get_height(node.left), self._get_height(node.right)) + 1

    def _rotate_left(self, node: AVLNode) -> AVLNode:
        """
        Performs a single left rotation, centered at the parameterized node
        """
        nodeChild = node.right
        nodeChildLeftHandoff = nodeChild.left

        nodeChild.left = node  # Swap the pointers
        node.right = nodeChildLeftHandoff

        if nodeChildLeftHandoff:  # Update parents
            nodeChildLeftHandoff.parent = node
        nodeChild.parent = node.parent
        node.parent = nodeChild

        if nodeChild.parent:
            if nodeChild.parent.right is node:
                nodeChild.parent.right = nodeChild
            elif nodeChild.parent.left is node:
                nodeChild.parent.left = nodeChild
        else:
            self._root = nodeChild

        self._update_height(node)  # Update height
        self._update_height(nodeChild)

        return nodeChild

    def _rotate_right(self, node: AVLNode) -> AVLNode:
        """
        Performs a single right rotation, centered at the parameterized node
        """
        nodeChild = node.left
        nodeChildRightHandoff = nodeChild.right

        nodeChild.right = node  # Swap the pointers
        node.left = nodeChildRightHandoff

        if nodeChildRightHandoff:  # Update parents
            nodeChildRightHandoff.parent = node
        nodeChild.parent = node.parent
        node.parent = nodeChild

        if nodeChild.parent:
            if nodeChild.parent.right is node:
                nodeChild.parent.right = nodeChild
            elif nodeChild.parent.left is node:
                nodeChild.parent.left = nodeChild
            else:
                raise BaseException("Problem in rotate left")
        else:
            self._root = nodeChild

        self._update_height(node)  # Update height
        self._update_height(nodeChild)

        return nodeChild

    def _update_height(self, node: AVLNode) -> None:
        """
        Updates the height of a node
        """
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

    def _rebalance(self, node: AVLNode) -> None:
        """
        Rebalance the AVL tree
        """
        self._update_height(node)
        balance = self._balance_factor(node)

        if balance < -1:
            if self._balance_factor(node.left) > 0:  # Check for double rotation
                self._rotate_left(node.left)
            self._rotate_right(node)

        elif balance > 1:
            if self._balance_factor(node.right) < 0:  # Check for double rotation
                self._rotate_right(node.right)
            self._rotate_left(node)


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        tree = AVL(case)
        print(tree)
        tree.print_tree()

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),  # RR, RR
        (10, 20, 30, 50, 40),  # RR, RL
        (30, 20, 10, 5, 1),  # LL, LL
        (30, 20, 10, 1, 5),  # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ("A", "B", "C", "D", "E"),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = AVL(case)
        print("INPUT  :", case)
        print("RESULT :", tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL()
        for value in case:
            tree.add(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print("add() stress test finished")

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),  # no AVL rotation
        ((1, 2, 3), 2),  # no AVL rotation
        ((1, 2, 3), 3),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print("INPUT  :", tree, "DEL:", del_value)
        tree.remove(del_value)
        print("RESULT :", tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print("INPUT  :", tree, "DEL:", del_value)
        tree.print_tree()
        tree.remove(del_value)
        print("RESULT :", tree)
        tree.print_tree()
        print("")

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = AVL(case)
    for del_value in case:
        print("INPUT  :", tree, del_value)
        tree.remove(del_value)
        print("RESULT :", tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = AVL(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print("INPUT  :", tree, root_value)
        tree.remove(root_value)
        print("RESULT :", tree)

    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL(case)
        for value in case[::2]:
            tree.remove(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
    print("remove() stress test finished")

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = AVL([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = AVL()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
