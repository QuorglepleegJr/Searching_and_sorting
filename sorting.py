from random import shuffle, randrange
from math import inf
from sys import exit
from time import time

class BogoIterationError(Exception):

    pass

class InputRefusedError(Exception):

    pass

def insertion_sort(array):

    start_time = time()

    comparisons = 0
    swap_number = 0
    
    sorted_index = 1

    while sorted_index < len(array):

        swaps = 0

        while sorted_index > swaps:

            comparisons += 1

            if array[sorted_index-swaps] < array[sorted_index-swaps-1]:

                array[sorted_index-swaps], array[sorted_index-swaps-1] = \
                    array[sorted_index-swaps-1], array[sorted_index-swaps]
                
                swap_number += 1
            
            else:

                break
            
            swaps += 1
        
        sorted_index += 1
    
    end_time = time()

    return array, end_time - start_time, comparisons, swap_number

def bubble_sort(array):

    start_time = time()

    comparisons = 0
    swaps = 0

    swap_made = True
    pass_no = 1

    while swap_made:

        swap_made = False

        for index in range(len(array)-pass_no):

            comparisons += 1

            if array[index] > array[index+1]:

                array[index], array[index+1] = \
                    array[index+1], array[index]

                swap_made = True

                swaps += 1
            
        pass_no += 1

    end_time = time()
    
    return array, end_time - start_time, comparisons, swaps

def cocktail_shaker_sort(array):

    start_time = time()

    comparisons = 0
    swaps = 0

    start = 0
    end = len(array)
    current = 1

    direction = 1

    swap_made = True

    while swap_made:

        swap_made = False

        while current < end and current >= start:

            comparisons += 1

            if array[current]*direction < array[current-direction]*direction:

                array[current], array[current-direction] = \
                    array[current-direction], array[current]
                
                swap_made = True

                swaps += 1
            
            current += direction
        
        if direction > 0:

            end -= 1
            current = end-1
        
        else:

            start += 1
            current = start
        
        direction *= -1
    
    end_time = time()
    
    return array, end_time - start_time, comparisons, swaps

def bogo_sort(array):

    start_time = time()

    comparisons = 0

    MAX_ITERATIONS = 1000000
    iterations = 0

    sorted = True

    for index in range(len(array)-1):

        if array[index] > array[index+1]:

            sorted = False
            break

    while not sorted:

        iterations += 1

        if iterations > MAX_ITERATIONS:

            raise BogoIterationError

        shuffle(array)

        sorted = True

        for index in range(len(array)-1):

            comparisons += 1

            if array[index] > array[index+1]:

                sorted = False
                break
    
    end_time = time()
    
    return array, end_time - start_time, comparisons

def merge_sort(array):
    
    start_time = time()

    comparisons = 0

    sublists = [[element] for element in array]

    while len(sublists) > 1:

        for index in range(0, len(sublists)-1, 2):

            new_list = []

            a = sublists[index]
            b = sublists[index+1]

            a_index = 0
            b_index = 0

            while a_index < len(a) and b_index < len(b):

                comparisons += 1

                if a[a_index] < b[b_index]:

                    new_list.append(a[a_index])
                    a_index += 1
                
                else:

                    new_list.append(b[b_index])
                    b_index += 1
            
            if a_index < len(a):

                new_list += a[a_index:]
            
            if b_index < len(b):

                new_list += b[b_index:]

            sublists[index] = new_list
            sublists[index+1] = None
        
        sublists = [element for element in sublists if element is not None]
    
    end_time = time()
    
    if len(sublists) == 1: return sublists[0], end_time-start_time, comparisons

    return [], end_time - start_time, comparisons

def heap_sort(array):

    start_time = time()

    comparisons = 0
    swaps = 0

    x = 1

    while (2**x-1) < len(array):

        x += 1

    heap = [-inf] + [inf] * (2**x-1)

    tail_index = 1

    for element in array:
            
        heap[tail_index] = element

        problem_index = tail_index

        comparisons += 1

        while heap[problem_index] <= heap[problem_index//2]:

            comparisons += 1
            swaps += 1

            heap[problem_index], heap[problem_index//2] = \
                heap[problem_index//2], heap[problem_index]

            problem_index //= 2
        
        tail_index += 1
    
    out_array = []
    
    while tail_index > 1:

        out_array.append(heap[1])

        tail_index -= 1

        heap[1] = heap[tail_index]
        heap[tail_index] = inf

        problem_index = 1

        comparisons += 1

        while problem_index*2+1 < len(heap) and heap[problem_index] > \
                min(heap[problem_index*2], heap[problem_index*2+1]):
            
            comparisons += 2

            if heap[problem_index*2] <= heap[problem_index*2+1]:

                heap[problem_index], heap[problem_index*2] = \
                    heap[problem_index*2], heap[problem_index]

                problem_index *= 2

                swaps += 1
            
            else:
                
                heap[problem_index], heap[problem_index*2+1] = \
                    heap[problem_index*2+1], heap[problem_index]

                problem_index *= 2
                problem_index += 1

                swaps += 2
    
    end_time = time()

    return [x for x in out_array if x != inf], end_time - start_time, \
        comparisons, swaps

def stooge_sort(array):

    start_time = time()

    comparisons = 0
    swaps = 0

    if len(array) < 2:

        return array, 0, comparisons, swaps
    
    if len(array) == 2:

        comparisons += 1

        if array[0] > array[1]:

            swaps += 1

            return [array[1], array[0]], 0, comparisons, swaps

        return array

    if len(array) == 3:

        comparisons += 3

        if array[0] > array[1]:

            swaps += 1

            array[0], array[1] = \
                array[1], array[0]
        
        if array[1] > array[2]:

            swaps += 1

            array[1], array[2] = \
                array[2], array[1]
        
        if array[0] > array[1]:

            swaps += 1

            array[0], array[1] = \
                array[1], array[0]
        
        return array, 0, comparisons, swaps
    
    length = (len(array)*2+2)//3

    array_return = stooge_sort(array[:length])
    array = array_return[0] + array[length:]
    comparisons += array_return[2]
    swaps += array_return[3]

    array_return =stooge_sort(array[-length:])
    array =  array[:-length] + array_return[0]
    comparisons += array_return[2]
    swaps += array_return[3]
    
    array_return = stooge_sort(array[:length])
    array = array_return[0] + array[length:]
    comparisons += array_return[2]
    swaps += array_return[3]
    
    end_time = time()
    
    return array, end_time - start_time, comparisons, swaps

def quick_sort(array):
    
    if len(array) == 0: return array, 0, 0, 0

    start_time = time()

    comparisons = 0
    swaps = 0

    pivot = randrange(len(array))

    low = 0
    high = len(array)-1

    while low < pivot or high > pivot:

        swap = True

        comparisons += 2

        if array[low] <= array[pivot] and low < pivot:

            low += 1
            swap = False
        
        if array[high] >= array[pivot] and high > pivot:

            high -= 1
            swap = False
        
        if swap:
            
            if high == pivot:

                pivot = low

            elif low == pivot:

                pivot = high
            
            array[low], array[high] = \
                array[high], array[low]
            
            swaps += 1
    
    begin = quick_sort(array[:pivot])
    comparisons += begin[2]
    swaps += begin[3]

    middle = [array[pivot]]

    end = quick_sort(array[pivot+1:])
    comparisons += end[2]
    swaps += end[3]

    end_time = time()

    return begin[0]+middle+end[0], end_time - start_time, comparisons, swaps

def counting_sort(array):

    start_time = time()

    if len(array) < 2:

        end_time = time()

        return array, end_time - start_time

    shifts = 0

    all_ints = True

    for value in array:

        if isinstance(value, float) and not value.is_integer():

            all_ints = False

    while not all_ints:

        array = [x*10 for x in array]

        shifts += 1

        all_ints = True

        for value in array:

            if isinstance(value, float) and not value.is_integer():

                all_ints = False
    
    array = [int(x) for x in array]

    minimum = min(array)
    maximum = max(array)

    values = dict([(x, 0) for x in range(minimum, maximum+1)])

    for value in array:

        values[value] += 1
    
    for value in range(maximum, minimum-1, -1):

        for x in range(minimum, value):

            values[value] += values[x]

    out_array = [None] * len(array)

    for value in array:

        out_array[values[value]-1] = value

        values[value] -= 1
    
    end_time = time()

    return out_array, end_time - start_time

def radix_sort(array):

    start_time = time()

    comparisons = 0
    swaps = 0

    for index in range(len(array)):

        pass

def array_input():

    arr = []

    print("Enter array one element at a time - leave blank to finish:")

    inp = input()

    if inp == "":

        raise InputRefusedError()

    while inp != "":

        arr.append(eval(inp))
        
        inp = input()
    
    return arr

def sort_input():

    print("Enter sort type - leave blank to quit:")

    sort_type = input()

    while sort_type not in SORTS:

        if sort_type == "":

            raise InputRefusedError

        print("That is not a valid sort, must be in", list(SORTS.keys()))

        sort_type = input()

    return SORTS[sort_type]

def full_input_sort():

    print(sort_input()(array_input()))


SORTS = {
        "Insertion": insertion_sort, 
        "Bubble" : bubble_sort,
        "Cocktail shaker" : cocktail_shaker_sort,
        "Merge" : merge_sort,
        "Heap" : heap_sort,
        "Quick" : quick_sort,
        #"Counting" : counting_sort,
        #"Stooge" : stooge_sort,
        #"Bogo" : bogo_sort,
}

COMPARISON_SORTS = {
        "Insertion",
        "Bubble",
        "Cocktail shaker",
        "Merge",
        "Heap",
        "Quick",
        #"Counting",
        "Stooge",
}

SWAP_SORTS = {
        "Insertion",
        "Bubble",
        "Cocktail shaker",
        "Heap",
        "Quick",
        #"Stooge",
}

if __name__ == "__main__":

    for sort in SORTS:
        
        print(f"\nTESTING {sort} Sort\n")

        with open("sorting_unit_tests.txt", "r") as tests:

            for index, test in enumerate(\
                [[eval(y) for y in x.strip().split(" ")] for x in tests]):

                print(f"Test {index+1}:\nInput {test[0]}")

                try:

                    result = SORTS[sort](test[0])
                
                except BogoIterationError:

                    print("PLAUSABLE, failed due to iteration limit")

                else:

                    if result[0] == test[1]:

                        print("PASSED")
                    
                    else:

                        print(f"FAILED, expected {test[1]}, got {result}")
                            
                        exit(1)
    
    print("\n\n")

    speed_iterations = 100

    length_test = 1000

    speeds = {}
    comparisons = {}
    swaps = {}

    for count in range(speed_iterations):

        test = [x for x in range(length_test)]
        shuffle(test)

        for sort in SORTS:

            result = SORTS[sort](test[:])

            if result[0] != [x for x in range(length_test)]:

                print(count, sort, test, result)
                break

            print(count, sort)

            if sort in speeds:

                speeds[sort] += result[1]
            
            else:

                speeds[sort] = result[1]
            
            if sort in COMPARISON_SORTS:
            
                if sort in comparisons:

                    comparisons[sort] += result[2]
                
                else:

                    comparisons[sort] = result[2]
            
            if sort in SWAP_SORTS:

                if sort in swaps:

                    swaps[sort] += result[3]
                
                else:

                    swaps[sort] = result[3]
    
    for sort in speeds:

        speeds[sort] /= speed_iterations

    for sort in comparisons:

        comparisons[sort] /= speed_iterations
    
    for sort in swaps:

        swaps[sort] /= speed_iterations
    
    print("\nAverage times:\n")
    for sort in speeds:
        print(f"{sort}: {speeds[sort]}")

    print("\nAverage comparisons:\n")
    for sort in comparisons:
        print(f"{sort}: {comparisons[sort]}")

    print("\nAverage swaps:\n")
    for sort in swaps:
        print(f"{sort}: {swaps[sort]}")

        
    while True:

        try:

            full_input_sort()
        
        except InputRefusedError:

            print("Quitting")

            break

    exit(0)