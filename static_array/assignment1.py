# Name: Noah Pragin
# OSU Email: praginn@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 1: Python Review
# Due Date: 07/09/2024
# Description: Solutions to coding problems designed to warm-up python skills


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple[int, int]:
    """
    Return a tuple containing the minimum and maximum of a given StaticArray

    :param arr: an array of integers

    :return:    tuple (minimum, maximum)
    """	
    #If array is empty return None
    if arr.length() == 0:
        return None
    
    #Set min and max to first element
    minimum = arr[0]
    maximum = arr[0]

    #Iterate through array and replace min and max as needed
    for i in range(arr.length()):
        if arr.get(i) > maximum:
            maximum = arr.get(i)
        elif arr.get(i) < minimum:
            minimum = arr.get(i)

    return (minimum, maximum)

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Given an array, returns a new array but replaces multiples of 3 with 'fizz', 5
    with 'buzz', and both with 'fizzbuzz'

    :param arr: an integer array

    :return:    New array with multiples of 3 replaced with 'fizz', 5 with 'buzz',
                and both with 'fizzbuzz'
    """
    newArr = StaticArray(arr.length())
    for i in range(newArr.length()):
        if arr.get(i) % 15 == 0: #Multiple of 5 and 3
            newArr.set(i, "fizzbuzz")
        elif arr.get(i) % 3 == 0: #Multiple of 3
            newArr.set(i, "fizz")
        elif arr.get(i) % 5 == 0: #Multiple of 5
            newArr.set(i, "buzz")
        else:                     #Multiple of neither
            newArr.set(i, arr.get(i))

    return newArr

# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    Reverses given integer array's elements in-place

    :param arr: integer array, will be mutated
    """
    #Initialize pointer to start and back of array
    lag = 0
    lead = arr.length() - 1

    #Iterate while pointers do not point to same element or pass each other
    while lag < lead:
        temp = arr.get(lag) #Store lag value before overwriting
        arr.set(lag, arr.get(lead)) #Overwrite lag value with lead value
        arr.set(lead, temp) #Overwrite lead value with stored lag value

        #Move pointers one closer to each other
        lag += 1
        lead -= 1

# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Given an array, returns a new array with all elements rotated steps number
    of times.

    :param arr: an integer array to be duplicated and rotated
    :param steps: the number of steps to rotate the new array by

    :return:    Mew array with elements rotated steps number of times.
    """
    #Run-time optimization/out of bounds handle
    steps = steps % arr.length()

    #Convert backward rotation to a forward one
    if steps < 0:
        steps += arr.length()

    newArr = StaticArray(arr.length())

    #Iterates through the original array, placing elements in the new array
    #with the correct rotation
    for i in range(arr.length()):
        newArr.set((i + steps) % arr.length(), arr.get(i))
    
    return newArr

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    Given two integers, start and end, returns a new StaticArray containing all
    values between start and end (inclusive)

    :param start: an integer to start at
    :param end: an integer to end at

    :return: New array with elements from start to end (inclusive).
    """
    if start > end:
        arr = StaticArray(start - end + 1) #Instantiate array

        for idx, num in enumerate(range(start, end - 1, -1)): #Populate array
            arr.set(idx, num)

        return arr

    arr = StaticArray(end - start + 1) #Instantiate array

    for idx, num in enumerate(range(start, end + 1)): #Populate array
        arr.set(idx, num)
    
    return arr

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    Given an array, returns 1 if sorted ascending, -1 if descending, and 0 otherwise.

    :param arr: Array to check if sorted

    :return: 1 if param is ascending, -1 if descending, 0 otherwise
    """
    if arr.length() == 1: #Default case
        return 1
    
    if arr.get(0) < arr.get(1): #If seems to be ascending
        for i in range(arr.length() - 1):
            if arr.get(i) >= arr.get(i + 1): #When starts descending, return 0
                return 0
        return 1
    
    for i in range(arr.length() - 1): #If seems to be descending
        if arr.get(i) <= arr.get(i + 1): #When starts ascending, return 0
            return 0
    return -1

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple[object, int]:
    """
    Given a sorted array, returns a tuple representing the mode: (val, freq)

    :param arr: Array to find mode

    :return: tuple representing mode (value, frequency)
    """
    mode = (arr[0], 1) #Default mode to first value, freq of 1
    count = 1
    for i in range(1, arr.length()): #Iterate through array
        if arr.get(i) == arr.get(i - 1): #If matches prev element, add count
            count += 1
        else: #If not the same as prev element, reset count
            count = 1

        if count > mode[1]: #If new mode, replace old mode
            mode = (arr.get(i), count)

    return mode

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Given an array, returns a new array without any duplicates

    :param arr: an integer array to be stripped of duplicates

    :return:    New array without any duplicates
    """
    newArr = StaticArray(arr.length())
    newArr.set(0, arr.get(0)) #Set first element of new array to first element of old
    j = 0 #New array iterator

    for i in range(1, arr.length()):
        if arr.get(i) != newArr.get(j): #If last element in newArr is diff, add new
            newArr.set(j + 1, arr.get(i))
            j += 1

    finalArr = StaticArray(j + 1) #Fix size of the new array
    for i in range(finalArr.length()):
        finalArr.set(i, newArr.get(i))
            
    return finalArr

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    Given an array, returns a new array sorted

    :param arr: an integer array to be sorted

    :return: New sorted array
    """
    minimum, maximum = min_max(arr) #Get min and max
    countArr = StaticArray(maximum - minimum + 1) #Create count array using min and max

    for i in range(arr.length()): #Iterate through array, populating count array
        currentVal = countArr.get(arr.get(i) - minimum)
        newVal = 1 if currentVal is None else currentVal + 1 #If uninitialized value, set to 1, else increment
        countArr.set(arr.get(i) - minimum, newVal)
    
    newArr = StaticArray(arr.length()) #New sorted array
    idx = 0
    for i in range(countArr.length() - 1, -1, -1): #Iterate backwards through count arr for descending order
        freq = countArr.get(i)
        if freq is not None:
            for _ in range(freq): #Add the right # of duplicate elements
                newArr.set(idx, minimum + i)
                idx += 1

    return newArr

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    Given a sorted array, returns a new array containing the sorted squares of the original array

    :param arr: an integer array to be squared and sorted, must be sorted in some order to start

    :return: New sorted and squared array
    """
    newArr = StaticArray(arr.length())
    lag = 0
    lead = arr.length() - 1

    for i in range(arr.length() - 1, -1, -1): #Start from the end of the result array, it is harder to guarantee success from start
        if arr.get(lag) ** 2 > arr.get(lead) ** 2: #Compare the squares of the elements at the two pointers
            newArr.set(i, arr.get(lag) ** 2)
            lag += 1
        else:
            newArr.set(i, arr[lead] ** 2)
            lead -= 1

    return newArr

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(f"Before: {arr}")
        result = count_sort(arr)
        print(f"After : {result}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
