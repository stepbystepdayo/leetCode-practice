
'''

THIS IS GLOBAL variable: 
x = 10 
print('global scope:', x)

def func1():
    THIS IS LOCAL variable:
    x = 'foo'  
    print('func1 scope:', x)  
    -> blocked scope: is not accessible outside of the function. but inside of fucntion, we can access anything. 

def func2():
    print('func2 scope:', x)

func1() -> 'foo'
func2() -> 10 

function2 doesn't have variable but, there is global scope x = 10,so return 10.
function1 has x = 'foo' local variable, so return 'foo'


'''

# BLOCKED SCOPE!!!

# inp = int(input("Enter a number: "))

# if inp > 5:
#     value = "Greater than 5!"
# else:
#     value = "Not greater than 5!"

# print(value)

# def append_5(x):
#     x = x[:]
#     x.append(5)
#     print(x)

# x =[]
# print(x) #[]
# append_5(x) # [5]
# print(x) #[]

# inside the function, we made x =x[:] copy of x. so we didn't NOT modify the original x. 

value = 5

def foo():
    global value # if there is not global, print(value) will be 5. but if you use global, whatever you made value inside the local, value will be global variable(value = 5). be careful to use this. because, it cause to error easliy.so avoid this.
    value = 10
    # print(value) # 10

print(value)# 5
foo()
print(value)#10

