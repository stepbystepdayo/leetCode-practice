
# name  = input("Name: ")
# if name == "Sayo":
#     print("Hello!")

number = float(input("Enter a number 5: "))

if number < 5:
    print("yayy good!")
elif number < 10: # this is additional check
    print("ohh this is less than 10!")
else:
    print("not good 🥲")

print("finished") # no matter what you finished if statment, it will show.


if number > 0 and number % 2 == 0:
    print("This is a positive even number!")

    number2 = float(input("number: "))
    if number2 < 0:
        print("negative")

    else:
        print("positive")

x = 6

result = "Ok" if x > 5 else "" 
# this is one-line if statement


# you can write like this too!
print("Hello") if x > 5 else print("Not Okay")


