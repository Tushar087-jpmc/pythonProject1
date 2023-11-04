"""
Declare & initialize a number. Check whether the number is in range 0-100
or not. If not in range print invalid input. Else – if the number is in range 90-
100 then print Super Smart, 80-90 print Smart,70-80 print smart enough,
60-70 print just smart, 35-60 print no smart, 0-35 print dump.
"""
import sys
number = int(input("Enter the number to perform the check :"))
def numberchecker(number):

    if number not in range(0, 101):
        print(f"number {number} is not in range 0 to 100, invalid input")
        sys.exit()
    elif number in range(90, 101):
        print("Super Smart")
    elif number in range(80, 91):
        print("Smart")
    elif number in range(70, 81):
        print("Smart Enough")
    elif number in range(60, 71):
        print("just smart")
    elif number in range(35, 61):
        print("No Smart")
    else:
        print("dump")

numberchecker(number)