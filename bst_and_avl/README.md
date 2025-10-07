# Assignment 4: Binary Search Tree and AVL Tree

An implementation of a Binary Search Tree (BST) and an AVL Tree (self-balancing BST) with traversal algorithms and balancing mechanisms.

## Features

### Binary Search Tree (BST)
- **Tree property**: Maintains BST property (left < parent < right)
- **Core operations**: add, remove, contains, get_first, get_last
- **Traversal algorithms**: in-order and pre-order traversal
- **Utility functions**: size, is_empty, make_empty

### AVL Tree (Self-Balancing BST)
- **Automatic balancing**: Maintains height difference ≤ 1 between subtrees
- **Rotation operations**: Left, right, left-right, right-left rotations to maintain balance
- **Height tracking**: Efficient height calculation and updates
- **All BST operations**: Inherits all BST functionality with added balancing

## File Structure

- `bst.py` - Binary Search Tree implementation
- `avl.py` - AVL Tree implementation (extends BST)
- `queue_and_stack.py` - Supporting data structures for traversal

## Performance Characteristics

| Operation | BST (Average) | BST (Worst) | AVL Tree |
|-----------|---------------|-------------|----------|
| Search | O(log n) | O(n) | O(log n) |
| Insert | O(log n) | O(n) | O(log n) |
| Delete | O(log n) | O(n) | O(log n) |
| Space | O(n) | O(n) | O(n) |
