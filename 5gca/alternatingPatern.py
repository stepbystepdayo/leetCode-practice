# def solution(numbers):
#     hashmap ={}
#     for num in numbers:
#         if num not in hashmap:
#             hashmap[num] = 1
#         if num in hashmap:
#             hashmap[num] -= 1
#     print(hashmap)
#     for item in hashmap.items():
#         # print(f"This is value: {value}")
#         # print(f"This is index: {index}")
#         # print(f"This is items: {item}")
#         if item[1] == 0:
#             return "wow you're not pattern"
#         else:
#             return -1


def solution(numbers):
    start,end = 0, len(numbers)-1
    # print(start,end)
    
    while start < end:
        
        








print(solution([1,2,1,3,2,1])) #3
print(solution([1,1,1,1,1])) #-1
print(solution([0])) #-1