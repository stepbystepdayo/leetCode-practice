'''

  If you're unfamiliar with Bubble Sort, we recommend watching the Conceptual
  Overview section of this question's video explanation before starting to code.


'''


def solution(array):
    isSorted = False

    while not isSorted:
        isSorted = True

        for i in range(len(array) -1):
            # if the number is greater than the right side of number, swap them.
            if array[i] > array[i+1]:
                # swap function
                swap(i,i+1,array)
                
                isSorted = False

    return array

def swap(i,j,array):
    # array[i] that mean left side of the number will swap to right side of the number. 
    array[i],array[j] = array[j],array[i]









print(solution([8,5,2,9,5,6,3]))