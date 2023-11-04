#Declare and initialize 3 three variable and print the biggest number.
var1 = input('first number :')
var2 = input('first number :')
var3 = input('first number :')

def findbiggest(var1,var2,var3):
    biggestnumber = max(var1,var2,var3)
    print(f"The biggestnumber is {biggestnumber}")

findbiggest(var1,var2,var3)