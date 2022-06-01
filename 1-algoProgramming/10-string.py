# s = "Hello"
# print(s[-1]) # o
# print(len(s)) # 5
# print(s.count("l")) # 2 count the "l"
# print(s.find("l")) # find the index of "l"

# upperChar = s.upper()
# print(upperChar) # only return upper chapital # H

# answer = input("what is my name?: ")

# if answer.lower() == "sayo": # lower() lower capital
#     print("nice")
# else:
#     print("ok!")

# capitalize() : alogo -> Algo

# .isdigit() : 19.4 -> False | 19 -> True

# s = "194"
# is_digit = s.isdigit()

# print(is_digit)

# .split!!!!

# s = "hello my name is Sayo"

# words = s.split()
# # we can separate indivisual words

# print(words) # ['hello', 'my', 'name', 'is', 'Sayo']

# o = "hello,my,name,is,Sayo"
# wordsSplit1 = o.split() #['hello,my,name,is,Sayo']
# wordsSplit = o.split(",") #['hello', 'my', 'name', 'is', 'Sayo']
# print(wordsSplit1)
# print(wordsSplit)

# #replace!!!
# str = "hello,my,name,is,,,Sayo"
# s2 = str.replace(",","|") # changing "," to "|"

# print(s2)

name = input("name?: ")
# print("hello",name,"! Thanks!")

# s = f"Hello,{name}!"
# print(s)

print(name * 5)
string = """hello my name is Sayo and this is a mulyilinr string
!
"""

# we can call multiple comment by string

string3 = f'{name}\'s'

# when you use ' in string, you need to use "" double courtation around string or after {}, use \ 


lst = ["t","i","m"]

string = "!".join(lst)
# when you want to add string into list, use .join()
