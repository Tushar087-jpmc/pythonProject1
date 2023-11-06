# Write programs to print the following series.
# 1,2,factor of three,4,5,factor of three, 7,8,factor of three,..........22,23,factor of three.

for num in range (1, 24):
    if num % 3 == 0:
        print('factor of three', end= ", ")
    else:
        print(num, end= ", ")