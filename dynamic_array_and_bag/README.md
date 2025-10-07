# Assignment 2: Dynamic Array and ADT Implementation

An implementation of a dynamic array with automatic resizing and an abstract bag structure built on top of the dynamic array.

## Features

### DynamicArray
- **Automatic resizing**: Doubles capacity when full
- **Basic operations**: append, remove_at_index, insert_at_index
- **Advanced operations**: slice, merge, map, filter, reduce

### Bag
- **add()**: Add elements to the bag
- **remove()**: Remove elements from the bag
- **count()**: Count occurrences of elements
- **clear()**: Empty the bag
- **size()**: Get current size
- **equal()**: Compare two bags for equality

## File Structure

- `dynamic_array.py` - DynamicArray class implementation
- `bag_da.py` - Bag implementation using dynamic array
- `static_array.py` - StaticArray base class

## Iterator Support

The DynamicArray supports Python's iterator protocol:

```python
da = DynamicArray([1, 2, 3, 4, 5])

# Iterate through all elements
for item in da:
    print(item)

# Convert to list
elements = list(da)

# Use in comprehensions
squared = [x**2 for x in da]
```

## Performance Characteristics

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| append() | O(1) amortized | O(1) |
| remove_at_index() | O(n) | O(1) |
| insert_at_index() | O(n) | O(1) |
| map() | O(n) | O(n) |
| filter() | O(n) | O(n) |
| reduce() | O(n) | O(1) |

