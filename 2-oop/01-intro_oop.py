'''

x = 1 # this is object. type of object is integer 

y = "string" # this is obejct and type of object is string

z = [2,3,4] # type of object is list and mutable.

print(type(x)) # <class 'int'> CLASS
print(type(y)) # <class 'string'> CLASS
print(type(z)) # <class 'list'> CLASS

x + y # ERROR the computer can not combine int and string.they are not the same object.

'''


def func():
    print("hello")

print(type(func)) # <class 'function'> functions are object too!! function is type of object and defines the accepted behaivior of it.　クラスのオブジェクトはプログラムの中でどのように動作するかを定義されている。


# Instance!!!!
# instance is the existance of a object of a specific class. 

x = 1 #value is one and instance is int class

y = "hello" # value is "hello" and instance is string class

# Methods!!!
# methods is kidn of a function that call like on the instance of class

st = "string" # instance is string class

st.upper() # .upper method is acting on st = "string"
st.lower() # .lower is method too

int / float / str / bool  # these are a class 






