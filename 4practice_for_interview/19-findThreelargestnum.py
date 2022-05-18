'''

  Write a function that takes in an array of at least three integers and,
  without sorting the input array, returns a sorted array of the three largest
  integers in the input array.

  The function should return duplicate integers if necessary; for example, it should return [10,10,12] for an input array of [10,5,9,10,12]

'''

 #This is the solution using sorted
#  def solution(array):
    # sortedArray = sorted(array)
    # split = sortedArray[-3:]
    # return split


# This is the solution without sorted
def solution(array):
    # need to make three empty spaces in array 
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest

# making the updated largest function 
def updateLargest(threeLargest, num):
    # if index[2] is none or number is greater than [2] inside threeLargest array,then we need to use shiftAndUpdate function
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num,2) 
    # if index[1] is none or number is greater than [1] inside threeLargest array,then we need to use shiftAndUpdate function
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num,1) 
    # if index[0] is none or number is greater than [0] inside threeLargest array,then we need to use shiftAndUpdate function
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest,num,0) 

# this is for changing the order 
def shiftAndUpdate(array, num, index):
    # loop over i and if i is eaqle to index, arrya[i] will be number
    for i in range(index + 1):
        if i == index:
            array[i] = num
        else:
            array[i] = array[i + 1]






print(solution([141,1,17,-7,-17,18,541,8,7,7]))