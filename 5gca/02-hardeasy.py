def solution(words):
    booleanList = [False] * len(words)
    for i , word in enumerate(words):

        
        # print(words[i][0])
        # almost, you CANT do this logic statement
        # print(f" {words[i][0]} - {words[i][-1]} v.s. {words[i + 1][0]} - {words[i +1][-1]} ")
        if (words[i][0] == words[i - 1][0]) and (words[i][-1] ==  words[i -1][-1]):
        # if words[i][0] and words[i][-1] == words[i + 1][0] and words[i +1][-1]:
            # print(f" {words[i][0]} - {words[i][-1]} v.s. {words[i -1][0]} - {words[i -1][-1]} ")
            print(f"before list = {booleanList}")
            booleanList[i-1] = True
            print(f"after list = {booleanList}")

        else:
            pass
    print(booleanList)
    return booleanList






print(solution(["abcd","adbdd","da","dd"]))