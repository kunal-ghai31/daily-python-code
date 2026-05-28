"""
a = 2
while a<=20:
    print(a)
    a = a+2

    
a = int(input("enter a number"))
while a<=50:
    print(a)
    a = a+5

choice = "y"
while choice in "Yy":
    name = input("enter your name")
    mob = input("enter yout number")
    choice = input("do you want to continue(y/n")

add = 0
num = int (input ("enter your number: "))
while num>0:
    rem = num%10
    add = add+rem
    num = num//10
print(add)

add = 0
num = int (input ("enter your number: "))
while num>0:
    rem = num%10
    add = add*10+rem
    num = num//10
print("reverse number:",add)

"""

num = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1
