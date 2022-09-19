from cgi import print_exception


print("Shipping calculator for your letter")
print("How much does your letter wheigh in grams")
Vægt=input()
price1=" 29DKK "
price2=" 58DKK "
price3=" 87DKK "
if float(Vægt)<=0:
    print("That weight is too small for a letter")
elif float(Vægt)<=100:
    print("The price is" + price1 + "for your letter")
elif float(Vægt)<=200:
    print("The price is" + price2 + "for your letter")
elif float(Vægt)<=2000:
     print("The price is" + price3 + "for your letter")
else:
    print("Thats a package not a letter")
