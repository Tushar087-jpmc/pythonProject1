# Write a Program to print the count of the even numbers between the given range

count = 0
for num in range(700, 901):
    if num % 2 == 0:
        count = count + 1

print("The count of even numbers between 700 and 900 is:", count)
