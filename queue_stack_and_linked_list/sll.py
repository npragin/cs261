# Name: Noah Pragin
# OSU Email: praginn@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3: Linked List and ADT Implementation
# Due Date: 07/22/2024
# Description: Singly linked list implementation


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        Adds a new node at the beginning of the list (after front sentinel)
        """
        node = SLNode(value) #Create new node
        node.next = self._head.next #New node points to old head
        self._head.next = node #New node is new head

    def insert_back(self, value: object) -> None:
        """
        Adds a new node at the end of the list.
        """
        itr = self._head
        while itr.next is not None: #Iterate through list to the end
            itr = itr.next

        itr.next = SLNode(value) #Insert node at the end

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts a new value at the specified index position in the linked list
        """
        if index < 0 or index > self.length():
            raise SLLException

        node = SLNode(value)
        idx = self._head
        for i in range(index): #Get to node preceding insertion index
            idx = idx.next

        node.next = idx.next #Swap pointers to insert new node after preceding node
        idx.next = node
        

    def remove_at_index(self, index: int) -> None:
        """
        Removes the node at the specified index position from the linked list
        """
        if index < 0 or index >= self.length():
            raise SLLException

        idx = self._head
        for i in range(index): #Get to node preceding deletion index
            idx = idx.next

        idx.next = idx.next.next #Swap pointers to delete/cut out node after preceding node

    def remove(self, value: object) -> bool:
        """
        Traverses the list from the beginning to the end, and removes the first node
        that matches the provided value
        """
        idx = self._head
        while idx.next is not None:
            if idx.next.value == value: #If value matches
                idx.next = idx.next.next #Cut node out of the linked list
                return True
            else:
                idx = idx.next
        return False
        

    def count(self, value: object) -> int:
        """
        Counts the number of elements in the list that match the provided value.
        """
        count = 0
        idx = self._head.next
        while idx is not None: #Iterate through list
            if idx.value == value: #If value found, increment count
                count += 1
            idx = idx.next
        return count
        

    def find(self, value: object) -> bool:
        """
        Returns a Boolean value based on whether or not the provided value exists in the
        list
        """
        idx = self._head.next
        while idx is not None: #Iterate through list
            if idx.value == value: #If value found, return true
                return True
            idx = idx.next
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        TODO: Write this implementation
        """
        if (start_index < 0 or
        size < 0 or
        size > self.length() or
        start_index >= self.length() or
        start_index + size > self.length()): #Input validation
            raise SLLException
        
        idx = self._head.next
        for i in range(start_index): #Iterate through list until reach index node
            idx = idx.next

        newList = LinkedList() #Create new list starting from node
        for i in range(size):
            newList.insert_back(idx.value)
            idx = idx.next

        return newList


if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
