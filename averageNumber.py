#Write a program to find the average of 24,26,28,.....100

# Initialize variables
start = 24
end = 100
step = 2
count = 0
total = 0

# Calculate the total and count of numbers
for num in range(start, end + 1, step):
    total += num
    count += 1

# Calculate the average
average = total / count

# Print the average
print("Average:", average)
