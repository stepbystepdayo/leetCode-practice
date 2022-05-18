'''

  Write a function that takes in an array of at least three integers and,
  without sorting the input array, returns a sorted array of the three largest
  integers in the input array.

  The function should return duplicate integers if necessary; for example, it should return [10,10,12] for an input array of [10,5,9,10,12]

'''


def solution(array):
    #This is the solution using sorted
    # sortedArray = sorted(array)
    # split = sortedArray[-3:]
    # return split

    # This is the solution without sorted

    # need to make three empty spaces in array 
    threeLargest = [None, None, None]

    
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest

def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num,2) 
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num,1) 
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest,num,0) 
def shiftAndUpdate(array, num, index):
    for i in range(index + 1):
        if i == index:
            array[i] = num
        else:
            array[i] = array[i + 1]






print(solution([141,1,17,-7,-17,18,541,8,7,7]))