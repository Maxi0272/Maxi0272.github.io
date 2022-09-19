#Den virker ikke fordi jeg har skrevet tallene i et stort float

print("Hello and welcome too the number finder. I will find the largest an smallest of 3 numbers. That you get to choose!!")

print ("please write your first number")
number1=input()

print ("please write your second number")
number2=input()

print ("please write your third number")
number3=input()

if float(number1 > number2) and float(number1 > number3):
    print("number 1 (" + number1 + ") is biggest")
elif float(number2 > number1) and float(number2 > number3):
    print ("number 2 (" + number2 + ") is biggest")
elif float(number3 > number2) and float(number3 > number1):
    print("number 3 (" + number3 + ") is biggest")
else:
    print("Two of the numbers are the same and the last is the smallest")

if float(number1 < number2) and float(number1 < number3):
    print("number 1 (" + number1 + ") is smallest")
elif float(number2 < number1) and float(number2 < number3):
    print ("number 2 (" + number2 + ") is smallest")
elif float(number3 < number2) and float(number3 < number1):
    print("number 3 (" + number3 + ") is smallest")
else:
    print("Two of the numbers are the same and the last is the biggest")

if float(number1 == number2) and float(number1 == number3) and float(number2 == number3):
    print("All numbers are the same")