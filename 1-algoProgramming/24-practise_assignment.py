
import random

input1 = int(input("Enter the start of the range: "))
input2 = int(input("Enter the end of the range: "))



if input1 != True or input2 != True:
    print("Please enter a valid number.")

    
random_number = random.randint(abs(input1),input2)



