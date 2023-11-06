#Write a program to print the series : 10@9,9@8,8@7.......-5@-6

for num1 in range(10, -6, -1):
    num2 = num1 - 1
    print(f"{num1}@{num2}", end=", ")
