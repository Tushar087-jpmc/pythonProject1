# Write a Program to print the all alphabets by using character Variable

# Print lowercase alphabets
print("Lowercase Alphabets:")
for char in range(ord('a'), ord('z') + 1):
    print(chr(char), end=" ")

print("\n")

# Print uppercase alphabets
print("Uppercase Alphabets:")
for char in range(ord('A'), ord('Z') + 1):
    print(chr(char), end=" ")
