


# def solution(words):
#     booleanList = [False] * len(words)
#     for i , word in enumerate(words):

        
#         # print(words[i][0])
#         # almost, you CANT do this logic statement
#         # print(f" {words[i][0]} - {words[i][-1]} v.s. {words[i + 1][0]} - {words[i +1][-1]} ")
#         if (words[i][0] == words[i - 1][0]) and (words[i][-1] ==  words[i -1][-1]):
#         # if words[i][0] and words[i][-1] == words[i + 1][0] and words[i +1][-1]:
#             # print(f" {words[i][0]} - {words[i][-1]} v.s. {words[i -1][0]} - {words[i -1][-1]} ")
#             print(f"before list = {booleanList}")
#             booleanList[i-1] = True
#             print(f"after list = {booleanList}")

#         else:
#             pass
#     print(booleanList)
#     return booleanList
# , index {i} / {length}


def solution(words):
	# make some sort of default array
	booleanlist = [0] * (len(words) -1 )
	
	for index in range(len(words) - 1):
		print(index)
		if words[index][0] == words[index + 1][0] and words[index][-1] == words[index +1][-1]:
			booleanlist[index] = True
		else:
			booleanlist[index] = False
		
	return booleanlist




print(solution(["abcd","adbdd","da","dd"])) # [True, False,False]