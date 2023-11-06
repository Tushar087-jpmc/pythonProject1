#Write a program to print all numbers which are divisible by 11 from 250 to 550

for num in range(250, 551):
    if num % 11 == 0:
        print(num)
