# Assignment 6: Min Heap Implementation

An implementation of a Min Heap using a dynamic array as the underlying storage. The heap maintains the min-heap property where the parent node is always smaller than or equal to its children.

## Features

### MinHeap
- **Heap property**: Parent nodes are always ≤ their children
- **Dynamic array storage**: Built on top of DynamicArray for automatic resizing
- **Core operations**: add, get_min, remove_min, build_heap
- **Utility functions**: size, is_empty, clear
- **Heap sort**: Separate heapsort function for external arrays

## File Structure

- `min_heap.py` - MinHeap class implementation
- `dynamic_array.py` - DynamicArray class
- `static_array.py` - StaticArray class

## Performance Characteristics

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| add() | O(log n) | O(1) |
| get_min() | O(1) | O(1) |
| remove_min() | O(log n) | O(1) |
| build_heap() | O(n) | O(1) |
| heapsort() | O(n log n) | O(1) |
