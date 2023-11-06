#Write a program to sum all even numbers between 382 and 582.

total = 0
for num in range(382, 583):
    if num % 2 == 0:
        total = total + num

print("The sum of even numbers between 382 and 582 is:", total)