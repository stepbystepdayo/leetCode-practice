

def solution(lst):
    output = []
    for i in range(len(lst)-1):
        # print(lst[-1],len(lst)-1)
        if i == 0:
            output.append(lst[0])
        if i == len(lst)-2:
            output.append(lst[-1])
        else:
            others = lst[i] +lst[i+1]
            output.append(others)
    return output
        







print(solution([4, 0, 1, -2, 3])) # [4,4,1,-1,1,3]