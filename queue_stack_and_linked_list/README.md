# Assignment 3: Queue, Stack, and Singly Linked List

An implementation of fundamental linear data structures: Queue, Stack, and Singly Linked List (SLL). A queue and stack are implemented using both static arrays and singly linked lists to demonstrate different approaches.

## Features

### Queue Implementation
- **Queue (SA)**: Queue using static array (circular buffer)
- **Queue (SLL)**: Queue using singly linked list
- **Operations**: enqueue, dequeue, front, is_empty, size

### Stack Implementation
- **Stack (DA)**: Stack using dynamic array
- **Stack (SLL)**: Stack using singly linked list
- **Operations**: push, pop, top, is_empty, size

### Singly Linked List (SLL)
- **SLNode**: Individual node class
- **LinkedList**: Complete linked list implementation
- **Operations**: insert_front, insert_back, insert_at_index, remove_at_index, remove, count, find, slice, length, is_empty

## File Structure

- **Components:**
    - `static_array.py` - Static array implementation
    - `dynamic_array.py` - Dynamic array implementation
    - `SLNode.py` - Singly Linked List node class
    - `sll.py` - Singly Linked List implementation
- **Implementations:**
    - `queue_sa.py` - Queue implementation using static array
    - `queue_sll.py` - Queue implementation using singly linked list
    - `stack_da.py` - Stack implementation using dynamic array
    - `stack_sll.py` - Stack implementation using singly linked list

## Performance Comparison

| Operation | Static Array | Dynamic Array | Singly Linked List |
|-----------|--------------|---------------|-------------------|
| **Queue** | -- | -- | -- |
| Enqueue | O(1) amortized* | O(1) amortized* | O(1) |
| Dequeue | O(1) | O(n) | O(1) |
| **Stack** | -- | -- | -- |
| Push | O(1) | O(1) amortized* | O(1) |
| Pop | O(1) | O(n) | O(1) |
| **List** | -- | -- | -- |
| Insert Front | N/A | N/A | O(1) |
| Insert Back | N/A | N/A | O(1) |
| Insert Index | N/A | N/A | O(n) |
| Remove At Index | N/A | N/A | O(n) |
| Remove Value | N/A | N/A | O(n) |

***Queue SA doubles capacity when full, affecting amortized performance**