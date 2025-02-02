num=int(input("Enter a number "))
while num>=10 and num<100:
    print("This number is a 2 digit number")
while num>=100 and num<1000:
    print("This number is a 3 digit number")
if num<10 and num>0:
    print("This number is a 1 digit number")
else:
    print("Your number is either less than 1 or more than 3 digits")
