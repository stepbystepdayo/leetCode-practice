
x = [1,2,3,True, 3.4, "Hello"]
# index: 0,1,2,3,4,5 we will count from 0
print(x[4]) # 3.4

# when you want to change the elements in []:
x[2] = 100 # x[2] that 3 will change to 100. you can modify in []

print(len(x)) # 6 lenght of list will count normal.

# when you want to serch a uniqe chars, you can use index like s[0]. but we cannot modify like s[0] = "a" in string
s = "hello"
print(s[0]) # h 

# APPEND!!!
# if you want to attach the element to the very end of list:
x.append("this is last") # [1,2,3,True, 3.4, "Hello","this is last"]

#POP method!!

popped = x.pop()

print(popped)
print(x) #[1,2,3,True, 3.4] last element will delete 

# COUNT!!
count = x.count(1)
print(count) # 1 it will count how many 1 inside of list

#INDEX!!

index = x.index(3)
print(index) # 2 it will return index of 3 [1,2,3,True, 3.4]

#REMOVE!!
x.remove(3)
print(x) #[1,2,3,True, 3.4] => #[1,2,True, 3.4]



# TRUE OR FALSE

list_contain = 5 in x 
print(list_contain) # True

# LAST ELEMENT:

x[-1] # this means last element : [1,2,3,True, 3.4, "Hello"] => "Hello"

# Combine together

a = [1,2,3]
b = [1,2]

combined = a + b
print(combined) # [1,2,3,1,2]

# extend

a.extend(b) # [1,2,3,1,2]
b.extend(a) #[1,2,1,2,3,1,2]


# There is the dimension

lst = [[5,6,[100]],[1,2],[1,2,3]]
# yellow [] is first dimension
# pink [] is second dimension
# blur [] is third dimention

print(lst[-1]) # [1,2,3] because, lst(first dimention) of last element is [1,2,3]
print(lst[-1][1]) # 2 lst[-1]: first dimention and [1]: second dimention. [1] is index of second dimention so 2

print(lst[0][2]) # [100] lst[0] is index 0 of the first dimention so [5,6,[100]] and [2] is index 2 of second dimention[5,6,[100]] so [100]

print(lst[0][2][0]) # 100 last [0] in print is index 0 of third dimention 

lst =[]
string = "yo"
string2 = "yo"
string3 = "yo"
# lst.append(string,string2,string3) # we can NOT put multiple elements inside append()
lst.append(string)
lst.append(string2)
lst.append(string3)
print(lst)





lst = []

string1 = str(input("Enter a string: "))
string2 = str(input("Enter a string: "))
string3 = str(input("Enter a string: "))
string4 = str(input("Enter a string: "))
string5 = str(input("Enter a string: "))
lst.append(string1)
lst.append(string2)
lst.append(string3)
lst.append(string4)
lst.append(string5)

number1 = float(input("Enter a number: "))
number2 = float(input("Enter a number: "))
number3 = float(input("Enter a number: "))

print(lst[number1])
