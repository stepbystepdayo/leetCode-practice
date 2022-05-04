'''Binary search is an efficient array search algorithm. It works by narrowing down the search range by half each time. If you have looked up a word in a physical dictionary, then you've already used binary search in real life. Let's look at a simple example:

Given a sorted array of integers and an integer called target, find the element that equals to the target and return its index. If the element is not found, return -1.'''

def solution(arrs, target):
    left, right = 0, len(arrs)-1
    # set up left and right pointers 

    while left < right: # while loop left and right then, left and right can point the numbers
        pivot = (left + right)// 2 # set up the middle of array so, add left and right of numbers and divided 2.
        if arrs[pivot] == target: # if the pivot in array is same number to target, return pivot number
            return pivot
        if arrs[pivot] < target:# if the pivot in array is less than target, we need to move left pointer to be pivot +1(thats mean lefy point is going to be next number)
            left = pivot + 1
        else: # else, right pointer is going to be left number
            right = pivot - 1
    return -1

