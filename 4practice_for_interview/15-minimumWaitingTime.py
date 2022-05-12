'''


'''

def solution(times):
    times.sort()

    output = 0

    for index, time in enumerate(times):
        substruction =  len(times) - (index+1)
        output += time * substruction

    return output


print(solution([3,2,1,2,6]))