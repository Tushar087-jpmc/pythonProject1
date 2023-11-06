# Write programs to print the following series. 0.5^2, 0.7^2,0.9^2....5.1^2

start = 0.5
end = 5.2
step = 0.2

num = start

while num <= end:
    print(f"{num}^2", end=', ')
    num = num + step
