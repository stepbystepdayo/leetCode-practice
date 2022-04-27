"""
997. Find the Town Judge
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Input: n = 2, trust = [[1,2]]
Output: 2

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
"""

# iterate through all the nodes? 

# so, let's start at some node
## what do we do? we should have a seen array, to know if we saw something
## we should have either stack or queue to hold all the edges of the node, and go through them

# import defaultdict is better

from collections import defaultdict
from typing import List

def judgeSolution(numberOfPeople, trust):

    # numberOfPeople is the number of people in the town
    
    # there are two conditions we need to keep track of
    ## everyone must trust the judge (meaning there's an edge to that vert from every other vert)
    ## that person must not trust anyone (there must be no directed edges from that vert)
    trustMap = defaultdict(list) # key is the truster, value is the list of trustees
    trustedMap = defaultdict(list) # this tracks a particular person and those who trust that person (value-side)

    # defaultDictTrustMap = defaultdict(list)

    # print(defaultDictTrustMap)
    for truster, trustee in trust:
        # if truster not in trustMap:
        #     trustMap[truster] = []
        trustMap[truster].append(trustee)
        # if trustee not in trustedMap:
        #     trustedMap[trustee] = []
        trustedMap[trustee].append(truster)
        # print(f"current truster {truster}", trustMap)
        # print(f"current trustee {trustee}", trustedMap)
        
    for i in range(1, numberOfPeople+1):
        if i not in trustMap:
            # print(f"{i} doesn't trust anyone")
            if len(trustedMap[i]) == numberOfPeople -1:
                # print(f"We found the judge!!!! the Judge is {i}")
                return f"this is the JUDGEEEEEE {i}"
    return "there is no judge!!!!"
    


print(judgeSolution(2, [[1,2]])) # 2
print(judgeSolution(3, [[1,3], [2,3]])) # 3
print(judgeSolution(4, [[1,3], [2,3], [4,1]])) # NONE