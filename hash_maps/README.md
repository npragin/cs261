# Assignment 5: Hash Maps - Separate Chaining and Open Addressing

An implementation of hash maps using two different collision resolution strategies: Separate Chaining and Open Addressing with Quadratic Probing.

## Features

### Both Implementations
- **Hash function**: Custom hash functions (hash_function_1 and hash_function_2)
- **Operations**: put, get, remove, contains_key, clear, empty_buckets, resize_table, table_load, get_keys_and_values
- **Dynamic resizing**: Automatically resizes when load factor exceeds threshold

### HashMapSC (Separate Chaining)
- **Collision resolution**: Uses linked lists (chains) to handle collisions

### HashMapOA (Open Addressing)
- **Collision resolution**: Uses quadratic probing to find alternative slots
- **Probing sequence**: i, i+1², i+2², i+3², ... (where i is initial hash)
- **Tombstone handling**: Marks deleted entries without breaking probe sequences

## File Structure

- `hash_map_sc.py` - Hash map with separate chaining collision resolution
- `hash_map_oa.py` - Hash map with open addressing (quadratic probing)
- `a6_include.py` - Supporting data structures and helper functions

## Performance Comparison

| Operation | Separate Chaining | Open Addressing |
|-----------|-------------------|-----------------|
| **Average Case** | | |
| Get | O(1 + α) | O(1/(1-α)) |
| Put | O(1 + α) | O(1/(1-α)) |
| Remove | O(1 + α) | O(1/(1-α)) |
| **Worst Case** | | |
| Get | O(n) | O(n) |
| Put | O(n) | O(n) |
| Remove | O(n) | O(n) |

*Where α (alpha) is the load factor (size/capacity)*

## Load Factor Management

### Separate Chaining
- **Resize trigger**: When load factor >= 1.0
- **Resize factor**: Doubles capacity (next prime)

### Open Addressing
- **Resize trigger**: When load factor >= 0.5
- **Resize factor**: Doubles capacity (next prime)
- **Why lower threshold**: Prevents clustering and maintains performance
