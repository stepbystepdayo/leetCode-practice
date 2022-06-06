
# when you want to try something,put something in try: and if that was not working, exception: will run 
# this is Exception and DONE
# try:
#     int("hello")
# except:
#     print("Exception")
# print("DONE") 


# try:
#     2/0
#     int("hello")
# except ValueError as e:
#     print("Exception",e)
# except ZeroDivisionError as e:
#     print("Exception",e)
# finally: # no matter happen in try: and except:, finally: will work. 
#     pass
# print("Done")

# x = []
# x[1]

# this is how to raise exception
# raise ValueError("This is an error!")
# raise Exception("This is an error!")
# raise IndexError("This is an error!")

# if not num.isdigit():
#     raise ValueError("This is not a valid number!")

while True:
    num = input("Enter a number: ")

    try:
        num = float(num)
    except ValueError:
        print("Not a valid float, try again")










