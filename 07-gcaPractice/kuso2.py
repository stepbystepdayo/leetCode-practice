

def solution(arr):
    result = []

    for i in range(0,len(arr)-1,2):
        if arr[i] > arr[i +1]:
            result.append(arr[i + 1])
            result.append(arr[i])

        else:
            result.append(arr[i])
            result.append(arr[i + 1])
    if len(arr) % 2 == 1:
        result.append(arr[-1])
    return result




print(solution([1,5,7,3,2,1])) #[1,5,3,7,1,2]
print(solution([6,7,8,8,5,3,2])) #[6,7,8,8,3,5,2]
print(solution([27])) #[27]