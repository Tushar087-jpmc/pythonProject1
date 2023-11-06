#  Write programs to print the following series. 5^2, 7^2,9^2.....25^2

start = 5
end = 25

for num in range(start, end + 1, 2):
    print(f"{num}^2", sep= ',', end=", ")
