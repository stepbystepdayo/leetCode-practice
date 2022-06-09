'''
sorted() # it will make new [] or so
.sort() # it will sort in original [] or so

'''
# This is ASCENDING order
# lst =[2,1,3,4,2,3,2,1]
# lst.sort()
# print(lst) # lst.sort() will modify lst

# print(sorted(lst)) # this will make new [] and sorted.

# # How to DESCENDING order

# lst2 =[2,1,3,4,2,3,2,1]
# lst2.sort(reverse = True)
# sorted(lst2, reverse= True)

# TUPLES
# lst3 = [2,1,3,4,2,3,2,1]
# print(lst3.sort()) # we cannot use .sort()
# print(sorted(lst3)) 
# print(tuple(sorted(lst3))) #(1, 1, 2, 2, 2, 3, 3, 4)
# this will return as list [1, 1, 2, 2, 2, 3, 3, 4]. NOT TUPLES. so! if you want to return as TUPLES. you should print(tuple(sorted(lst3))) 

# lst4 = [[1,2],[3,4],[5,6],[-1,-2],[0,0]]
# lst4.sort()
# print(lst4) #[[-1, -2], [0, 0], [1, 2], [3, 4], [5, 6]]

# lst5 = [[1,2],[3,-4],[5,-6],[-1,-2],[0,0]]
# lst5.sort()
# print(lst5) #[[-1, -2], [0, 0], [1, 2], [3, -4], [5, -6]] this sorted by first elements
# how to sort by second elements

# def sorte_by_second(item):
#     return item[1] #sum(item)
# lst6 = [[1,2],[3,-4],[5,-6],[-1,-2],[0,0]]
# lst6.sort(key = sorte_by_second)
# print(lst6) #[[5, -6], [3, -4], [-1, -2], [0, 0], [1, 2]]

# new_list = sorted(lst6, key = sorte_by_second)
# print(new_list)#[[5, -6], [3, -4], [-1, -2], [0, 0], [1, 2]]


# Be careful to use .sort()!!

lst = [3, 4, 2, -1, 2] 

print(lst.sort()) # we can not print .sort() directly. it will None!!


# how to sort dict

people = {"Tim": 21, "Joe": 18, "Sarah": 25, "Jennie": 26, "Bill": 34}

result = sorted(people, key = people.get)
print(result) # ["Joe","Tim","Sarah","Jennie","Bill"]
# in dict, key function will be sorted by their values. {key : value} 




