'''
Given an array of integers a, your task is to calculate the digits that occur the most number of times in the array. Return the array of these digits in ascending order.

Example

For a = [25, 2, 3, 57, 38, 41], the output should be solution(a) = [2, 3, 5].

Here are the number of times each digit appears in the array:

0 -> 0
1 -> 1
2 -> 2
3 -> 2
4 -> 1
5 -> 2
6 -> 0
7 -> 1
8 -> 1
The most number of times any number occurs in the array is 2, and the digits which appear 2 times are 2, 3 and 5. So the answer is [2, 3, 5].



'''


def solution(a):
    
    mapped = ''.join(map(str,a))
    print(mapped)
    
    sepa = [int(n) for n in str(mapped)]
    print(sepa)
    
    hashmap = {}
    
    for num in sepa:
        if num not in hashmap:
            hashmap[num] = 0
        hashmap[num] += 1
    print(hashmap)
    # maxV =max(hashmap.values())
    
    # result = [k for k,v in hashmap.items()if v == maxV]
    # result.sort()
    result = []
    maxV = max(hashmap.values())
    for k, v in hashmap.items():
        if v == maxV:
            result.append(k)
    result.sort()

            

    return result


print(solution([25, 2, 3, 57, 38, 41])) #[2,3,5]


            