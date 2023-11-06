#Write programs to print the following series. 1,even,3,even,5,even,.......35,even

for num in range(1, 36):
    if num % 2 == 1:
        print(num, end=", ")
    else:
        print("even", end=", ")
