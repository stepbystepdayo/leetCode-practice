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