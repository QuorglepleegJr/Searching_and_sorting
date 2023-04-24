from random import shuffle, randrange
from math import inf
from sys import exit

def insertion_sort(array):

    sorted_index = 1

    while sorted_index < len(array):
        
        insert_index = 0

        while array[insert_index] < array[sorted_index] and \
            insert_index < sorted_index:

            insert_index += 1
        
        array = array[:insert_index] + [array[sorted_index]] + \
              array[insert_index:sorted_index] + array[sorted_index+1:]
        
        sorted_index += 1

    return array

def bubble_sort(array):

    swap_made = True

    while swap_made:

        swap_made = False

        for index in range(len(array)-1):

            if array[index] > array[index+1]:

                temp = array[index]
                array[index] = array[index+1]
                array[index+1] = temp

                swap_made = True
    
    return array

def bogo_sort(array):

    sorted = True

    for index in range(len(array)-1):

        if array[index] > array[index+1]:

            sorted = False
            break

    while not sorted:

        shuffle(array)

        sorted = True

        for index in range(len(array)-1):

            if array[index] > array[index+1]:

                sorted = False
                break
    
    return array

def merge_sort(array):

    sublists = [[element] for element in array]

    while len(sublists) > 1:

        for index in range(0, len(sublists)-1, 2):

            new_list = []

            a = sublists[index]
            b = sublists[index+1]

            a_index = 0
            b_index = 0

            while a_index < len(a) and b_index < len(b):

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
    
    if len(sublists) == 1: return sublists[0]

    return []

def heap_sort(array):

    x = 1

    while (2**x-1) < len(array):

        x += 1

    heap = [-inf] + [inf] * (2**x-1)

    tail_index = 1

    for element in array:
            
        heap[tail_index] = element

        problem_index = tail_index

        while heap[problem_index] <= heap[problem_index//2]:

            temp = heap[problem_index]
            heap[problem_index] = heap[problem_index//2]
            heap[problem_index//2] = temp
            problem_index //= 2
        
        tail_index += 1
    
    out_array = []
    
    while tail_index > 1:

        out_array.append(heap[1])

        tail_index -= 1

        heap[1] = heap[tail_index]

        problem_index = 1

        while problem_index < tail_index//2 and heap[problem_index] > \
            min(heap[problem_index*2], heap[problem_index*2+1]):

            if heap[problem_index*2] <= heap[problem_index*2+1]:

                temp = heap[problem_index]
                heap[problem_index] = heap[problem_index*2]
                heap[problem_index*2] = temp

                problem_index *= 2
            
            else:
                
                temp = heap[problem_index]
                heap[problem_index] = heap[problem_index*2+1]
                heap[problem_index*2+1] = temp

                problem_index *= 2
                problem_index += 1

    return [x for x in out_array if x != inf]

def stooge_sort(array):

    if len(array) < 2:

        return array
    
    if len(array) == 2:

        if array[0] > array[1]:

            return [array[1], array[0]]

        return array

    if len(array) == 3:

        if array[0] > array[1]:

            temp = array[0]
            array[0] = array[1]
            array[1] = temp
        
        if array[1] > array[2]:

            temp = array[1]
            array[1] = array[2]
            array[2] = temp
        
        if array[0] > array[1]:

            temp = array[0]
            array[0] = array[1]
            array[1] = temp
        
        return array
    
    length = (len(array)*2+2)//3

    array = stooge_sort(array[:length]) + array[length:]
    array = array[:-length] + stooge_sort(array[-length:])
    array = stooge_sort(array[:length]) + array[length:]
    
    return array

def quick_sort(array):
    
    if len(array) == 0: return array

    pivot = randrange(len(array))

    low = 0
    high = len(array)-1

    while low < pivot or high > pivot:

        swap = True

        if array[low] <= array[pivot] and low < pivot:

            low += 1
            swap = False
        
        if array[high] >= array[pivot] and high > pivot:

            high -= 1
            swap = False
        
        if swap:
            
            if high == pivot:

                pivot = low

            if low == pivot:

                pivot = high
            
            temp = array[low]
            array[low] = array[high]
            array[high] = temp
    
    return quick_sort(array[:pivot]) + [array[pivot]] + quick_sort(array[pivot+1:])


if __name__ == "__main__":

    for sort in [("Insertion", insertion_sort), 
                ("Bubble", bubble_sort),
                ("Merge", merge_sort),
                ("Heap", heap_sort),
                ("Quick", quick_sort),
                ("Stooge", stooge_sort),
                ("Bogo", bogo_sort),]:
        
        print(f"\nTESTING {sort[0]} Sort\n")

        with open("unit_tests.txt", "r") as tests:

            for index, test in enumerate(\
                [[eval(y) for y in x.strip().split(" ")] for x in tests]):

                print(f"Test {index+1}:\nInput {test[0]}")

                result = sort[1](test[0])

                if result == test[1]:

                    print("PASSED")
                
                else:

                    print(f"FAILED, expected {test[1]}, got {result}")
                    
                    exit(1)

    exit(0)