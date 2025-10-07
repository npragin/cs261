# Name: Noah Pragin
# OSU Email: praginn@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: MinHeap Implementation
# Due Date: 08/05/2024
# Description: MinHeap Implementation using my own dynamic and static array classes


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MinHeap with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MinHeap content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return "HEAP " + str(heap_data)

    def add(self, node: object) -> None:
        """
        Adds a new object to the MinHeap while maintaining heap property
        """
        idx = self._heap.length()
        self._heap.append(node)
        parentIdx = (idx - 1) // 2
        
        while idx > 0 and parentIdx >= 0: #Propogate node up heap until it reaches correct location
            parent = self._heap.get_at_index(parentIdx)

            if parent < node:
                break
            
            if idx == self._heap.length():
                self._heap.append(parent)
            else:
                self._heap.set_at_index(idx, parent)

            self._heap.set_at_index(parentIdx, node)
            idx = parentIdx
            parentIdx = (idx - 1) // 2

    def is_empty(self) -> bool:
        """
        Returns True if the heap is empty; otherwise, it returns False
        """
        return self._heap.length() == 0

    def get_min(self) -> object:
        """
        Returns an object with the minimum key, without removing it from the heap
        """
        if self._heap.length() == 0:
            raise MinHeapException()
        return self._heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Returns an object with the minimum key, and removes it from the heap
        """
        if self._heap.length() == 0:
            raise MinHeapException()
        
        if self._heap.length() == 1: #If length 1, return pop
            return self._heap.pop()
        
        newRoot = self._heap.pop()
        oldRoot = self._heap.get_at_index(0)
        self._heap.set_at_index(0, newRoot) #Set new root to be last node in heap
    
        _percolate_down(self._heap, 0)

        return oldRoot

    def build_heap(self, da: DynamicArray) -> None:
        """
        Receives a DynamicArray with objects in any order, and builds a proper MinHeap
        """
        self._heap = DynamicArray(da)
        for i in range(da.length() // 2 - 1, -1, -1):
            _percolate_down(self._heap, i)

    def size(self) -> int:
        """
        Returns the number of items currently stored in the heap
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        Clears the contents of the heap
        """
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    Takes a DynamicArray and sorts it in non-ascending order using Heapsort
    """
    for i in range(da.length() // 2 - 1, -1, -1): #Heapify
            _percolate_down(da, i)

    k = da.length() - 1
    while k > 0:
        #Swap K and min
        temp = da.get_at_index(k)
        da.set_at_index(k, da.get_at_index(0))
        da.set_at_index(0, temp)

        #Percolate K down, use delimiter so sorted part is not touched
        _percolate_down(da, 0, k)

        k -= 1

def _percolate_down(da: DynamicArray, parent: int, delimiter=None) -> None:
    """
    Maintains the heap property by shifting nodes at the given index.
    """
    while True:
        leftChildIdx = parent * 2 + 1
        rightChildIdx = parent * 2 + 2
        smallest = parent

        if (leftChildIdx < (delimiter or da.length()) and
            da.get_at_index(leftChildIdx) < da.get_at_index(smallest)): #Find smallest
            smallest = leftChildIdx

        if (rightChildIdx < (delimiter or da.length()) and
            da.get_at_index(rightChildIdx) < da.get_at_index(smallest)):
            smallest = rightChildIdx

        if smallest != parent:  #If smallest found, switch around and update indexes
            temp = da.get_at_index(smallest)
            da.set_at_index(smallest, da.get_at_index(parent))
            da.set_at_index(parent, temp)
            if smallest == leftChildIdx:
                parent = leftChildIdx
            else:
                parent = rightChildIdx
        else:   #If no smallest found, stop percolating
            break


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")
