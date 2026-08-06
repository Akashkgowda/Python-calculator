print("Welcome to simple calculator")
while True:
    print("1.Addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.modulus")
    print("6.Exponent")
    print("7.Exit")
    choice=int(input("Enter your choice: "))
    if choice==7:
       print("Thanks for using the calculator")
       break
    if choice<1 or choice>7:
       print("Invalid choice,please enter a number between 1 and 7")
       continue
    if choice==1:
       a=float(input("enter first number: "))
       b=float(input("enter second number: "))
       sum=a+b
       print("The sum is",sum)
    elif choice==2:
       a=float(input("enter first number: "))
       b=float(input("enter second number: "))
       sub=a-b
       print("The difference is",sub)
    elif choice==3:
       a=float(input("enter first number: "))
       b=float(input("enter second number: "))
       mul=a*b
       print("The product is",mul)
    elif choice==4:
       a=float(input("enter first number: "))
       b=float(input("enter second number: "))
       if b==0:
          print("division by zero is not allowed")
       else:
          div=a/b
          print("The quotient is",div)
    elif choice==5:
       a=float(input("enter first number: "))
       b=float(input("enter second number: "))
       mod=a%b
       print("The Remainder is",mod)
    elif choice==6:
      a=float(input("enter first number: "))
      b=float(input("enter second number: "))
      exp=a**b
      print("The exponentiation is",exp)