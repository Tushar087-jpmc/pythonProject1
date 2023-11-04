"""Write a java program that performs the following tasks.
a. Store a number in a variable
b. If value is not in range (100-1000) prints wrong number else follows
the steps
c. Check even or odd
d. If even divide the number by 3 and print the remainder
e. If odd divide the number by 2 and print the remainder.
"""
import sys
number = int(input("Enter the number to perform the check :"))
def findrightnumberoddeven(number):

    if number not in range(100, 1001):
        print(f"number {number} is not in range 100 to 1000, wrong number provided")
        sys.exit()
    else:
        if number % 2 == 0:
            print("dividing the even number by 3 and the reminder is :", number % 3)
        elif number %2 != 0:
            print("dividing the odd number by 2 and the reminder is", number % 2)
findrightnumberoddeven(number)
