'''
Given an array of integers numbers, your task is to count all numbers that are not equal to the first or the second element of the array.

Example

For numbers = [4, 3, 2, 3, 2, 5, 4, 3], the output should be solution(numbers) = 3.

Explanation:
The first two elements of the array are 4 and 3. There are three elements in numbers that are not equal to 4 or 3:

numbers[2] = 2
numbers[4] = 2
numbers[5] = 5
So, the answer is 3.
For numbers = [3, 3, 1, 1, 3], the output should be solution(numbers) = 2.

Explanation:
The first two elements of the array are 3 and 3. There are two elements in numbers that are not equal to 3:

numbers[2] = 1
numbers[3] = 1
So, the answer is 2.
For numbers = [-2], the output should be solution(numbers) = 0.

Explanation:
The first element of the array is -2, and the second element does not exist, so the only requirement is to count numbers different from -2. There are no elements in numbers that are not equal to -2, so the answer is 0.

'''



def solution(numbers):
    first = numbers[0]
    second = numbers[1]
    result = 0
    
    for idx in range(len(numbers)-1):
        if numbers[idx] == first or numbers[idx] == second:
            print(f"this is a BAD number, index is {idx} and value is {numbers[idx]}")
        else:
            result += 1
    return result

print(solution([4, 3, 2, 3, 2, 5, 4, 3])) # 3
print(solution([3, 3, 1, 1, 3])) # 2 

