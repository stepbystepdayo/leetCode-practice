'''

'''




def solution(tree, target):
    # need helper method    
    return solutionHelper(tree,target,float("inf"))

def solutionHelper(tree, target, closest):
    currentNode = tree

    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            coloset = currentNode.value
        if target < currentNode:
            currentNode = currentNode.left
        elif target > currentNode:
            currentNode = currentNode.right
        
    return closest

    


# def findClosestValueInBst(tree, target):
#     # Write your code here.
# 	return findClosestValueInBstHelper(tree, target, tree.value)
	

# def findClosestValueInBstHelper(tree, target, closest):
# 	if tree is None:
# 		return closest
# 	if abs(target - closest) > abs(target - tree.value):
# 		closest = tree.value
# 	if target < tree.value:
# 		return findClosestValueInBstHelper(tree.left, target, closest)
# 	elif target > tree.value:
# 		return findClosestValueInBstHelper(tree.right, target, closest)
# 	else:
# 		return closest
	
	
# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
