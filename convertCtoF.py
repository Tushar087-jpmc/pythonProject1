# Write a program to covert temperature from degree C to F. (Input 80C)
def convertctof(celius=80):
    fahrenheit = celius * 1.8 + 32
    print(f"The Fahrenheit equivalent of {celius} celsius is {fahrenheit}")


convertctof(80)
