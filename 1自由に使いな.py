    # MAIN CODE
    # we will use a hashmap to record how many count we have of each letter in array
    # for example, for "[7,3,2,7]" => {7:2, 3:1, 2:1}

    # subsequencyFreq = {}

    # for number in subsequence:
    #     # lets count!
    #     if number not in subsequencyFreq:
    #         subsequencyFreq[number] = 1
    #     else:
    #         subsequencyFreq[number] += 1
    # print(subsequencyFreq)

    # now, let's count down, use the freq map to see if each number in subsequence is in array, in order.

# this is test for abs()
# test= abs(-2.3)
# test2 = abs(3-4j)
# print(test,test2)



# practice for loop over values

# randomObj = {"sayo": 27, "kai": 30, "micah": 25 }

# def loopOverDict(obj):

#     for key in obj:
#         print(f"this is the key, {key}")
#         print(f"Here is the value:{obj[key]}")

        

    
# loopOverDict(randomObj)


# SORTING!!! 
# Insertion Sort and Bubble sort are stable so these are so useful

# Insertion Sort

def sort_list(unsorted_list):
    for i, entry in enumerate(unsorted_list):
        current = i
        while current > 0 and unsorted_list[current] < unsorted_list[current - 1]:
            unsorted_list[current], unsorted_list[current -1] = unsorted_list [current -1],unsorted_list[current]
            current -= 1
        return unsorted_list

if __name__ == '__main__':
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))


