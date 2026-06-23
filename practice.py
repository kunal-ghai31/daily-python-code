 #even or Odd
"""
a= int(input('Enter a number'))
if a%2==0:
    print('Number is Even')
else:
    print('Number is Odd')
    """
# Find greater value
"""
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))       
if a > b:
    print(f'{a} is greater')
else:
    print(f'{b} is greater')

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))       
c = int(input('Enter third number: '))

if a >= b and a >= c:
    print(f'{a} is greater')
elif b >= a and b >= c:
    print(f'{b} is greater')
else:
    print(f'{c} is greater')

    """
# Calculate marks and find the percentage
"""
Maths = int (input('Enter Your Marks in Maths: '))
English = int (input('Enter Your Marks in English: '))
Computer = int (input('Enter Your Marks in Computer: '))
Science = int (input('Enter Your Marks in Science: '))
total = Maths+English+Computer+Science
percentage= total/4

print ("/n----Result----")
print (f'Total Marks:{total} /400')
print(f"Average Percentage: {percentage:}%")

if Maths < 59:
    print("Failed in Maths")

if English < 59:
    print("Failed in English")

if Computer < 59:
    print("Failed in Computer")

if Science < 59:
    print("Failed in Science")
    
if percentage >=90 and percentage <= 100:
    print("Result: Pass  Grade: A")
elif percentage >=80 and percentage <= 89:
    print("Result: Pass  Grade: B")
elif percentage >=70 and percentage <= 79:
    print("Result: Pass  Grade: C")
elif percentage >=60 and percentage <= 69:
    print("Result: Pass  Grade: D")
elif percentage >=0 and percentage <= 59:
    print(" Result: FAIL")
else:
    print('INVALID')
"""
correct_password = 0000

while True:
    try:
        p = int(input("Enter Your Password: "))

        if p == correct_password:
            print("Password is Correct")
            break
        else:
            print("Invalid Password")

    except ValueError:
        print("Please enter numbers only")
