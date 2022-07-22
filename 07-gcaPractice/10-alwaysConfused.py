
def solution(n,a):
    result = []
    if n == 1:
        return a

    for i in range(len(a)-1):
        
        if i == 0:
            first = a[i] + a[i + 1]
            result.append(first)
        if i == len(a)-2:
            last = a[-1] + a[-2]
            result.append(last)
        else:
            other = a[i] + a[i +1] + a[i +2]
            result.append(other)
    return result





print(solution(5,[4, 0, 1, -2, 3])) #[4, 5, -1, 2, 1]
print(solution(1,[9])) #[9]
