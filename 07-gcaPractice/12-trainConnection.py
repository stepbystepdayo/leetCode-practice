

def solution(a,b,c,start,end):
    together = [a,b,c]

    hashmap = {0:"A",1:"B",2:"C"}
    output = []
    for i,places in enumerate(together):
        if start in places:
            placeName = hashmap[i]
            output.append(placeName)
            for i, places in enumerate(together):
                if end in places:
                    placeName = hashmap[i]
                    output.append(placeName)

    output.sort()
    final = "".join(output)
    if final == "AC":
        return "ABC"
    return final


'''
    testTolist1 = [final] #['AB']
    testTolist2 = list(final) #['A', 'B']
    print(testTolist1,testTolist2)

'''

print(solution(["Green Park","Holbone"],["Bow Road","Mile End"],["Balham","Forest Hill"],"Bow Road","Green Park")) # "AB"
print(solution(["Green Park","Holbone"],["Bow Road","Mile End"],["Balham","Forest Hill"],"Green Park","Forest Hill")) # "ABC"
print(solution(["Green Park","Holbone"],["Bow Road","Mile End"],["Balham","Forest Hill"],"Mile End","Balham")) #"BC"