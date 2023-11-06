#Write programs to print the following series. 1,3,
# divisible by five, 7,9,11,13, divisible by five,.....21,23, divisible by five


for num in range(1, 24):
    if num % 5 == 0:
        print("divisible by five", end=", ")
    elif num % 2 != 0:
        print(num, end=", ")

