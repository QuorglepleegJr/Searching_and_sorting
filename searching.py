from sys import exit

def linear_search(array, value):

    for index in range(len(array)):

        if array[index] == value:

            return index
    
    return None

def binary_search(array, value):

    start = 0
    end = len(array)

    while start < end:

        mid = (start + end)//2

        if array[mid] == value:

            return mid

        if array[mid] < value:

            start = mid + 1
        
        else:

            end = mid
    
    return None

if __name__ == "__main__":

    searches = {
        "l": linear_search,
        "b": binary_search,
    }

    with open("searching_unit_tests.txt","r") as tests:

        for line in tests.readlines():

            test = line.strip().split(" ")

            print(f"Test input {test}")

            for search in test[0]:

                print(search)

                result = searches[search](eval(test[1]), eval(test[2]))

                if result == eval(test[3]):

                    print("PASSED")
                
                else:

                    print(f"FAILED\nExpected {eval(test[3])}, got {result}")

                    exit(1)
    
    exit(0)


            

