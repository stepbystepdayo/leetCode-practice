'''
Slices returns a new abject that contains the result of the slice. it does not modify the exsting object!!

You can only use [list], (tuple) and "string"

'''



lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lst[:8])

# # -> new_list = my_list[start:stop:step]

# new_list = my_list[0:2] #index 0 to 2 but not include index 2!! so, [2,3].

# new_list = my_list[:4] # [2,3,4,2] 0 to 4 but not include index 4 number

# new_list = my_list[1:4] #[3,4,2] 1 to 4 started index 1 and not include index 4 number

# new_list = my_list[1:6:2] # [3,2,1] 2steps and not include index 6 number

# # how to do negative index

# new_list = my_list[8:0:-1]  # start index 8 then, neagtive step -1 and not include index 0 so, [3,2,2,1,3,2,4,3] 

# new_list = my_list[:] # copy of all of list [2,3,4,2,3,1,2,2,3,1,2,1]

# new_list = my_list[2:]# start index 2 to end of index

# new_list = my_list[:-1] # end -1 index


# # REVERSE!!

# new_list = my_list[::-1] # [1,2,1,3,2,2,1,3,2,4,3,2]

# # STRING SLICES

# string = "hello"

# print(string[::2]) # 2steps: hlowrd

# print(string[1::2]) # start index 1 and 2 steps: el ol

# print(string[1:6:2]) # start index 1, end index 6(not include index 6number) and 2steps : el

# # TUPLES SLICES

# tup = 1,2,3,4,2,3

# print(tup[1:6:2]) #(2,4,3) this is blandnew tuple not same one. they can not modify




