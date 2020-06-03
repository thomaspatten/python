number = int(input("what is your number "))

factorial = 1


if number == 0:
   print("The factorial of 0 is 1")
else:
   for n in range(1,number + 1):
       factorial = factorial*n
   print("The factorial of",number,"is",factorial)
