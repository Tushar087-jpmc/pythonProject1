#Write programs to print the following series. 5*4,5*3,5*2,......5*(-12) (Print in two ways – patter & multiplied value)

for num1 in range(5, -12, -1):
    num2 = num1 - 1
    print(f"5*{num2}", end=", ")