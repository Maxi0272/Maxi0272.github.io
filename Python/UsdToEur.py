print ("Welcome to the currency exchange")
print ("please enter the desired amount to convert from DKK to EUR. MINIMUM 3.72 DKK")
print ("A 2% COMISSION WILL BE CHARGED")
DKK=input()
if (float(DKK)) < 3.72:
    print ("Invalid amount")
else:
    print (DKK + " will be exchanged at a rate of 100 DKK to 13.45 EUR")
    EUR1= float((float(DKK))/100*13.45)
    EUR= EUR1 * 0.98
    print ("you have succsesfully converted " + str(DKK) + " DKK to " + str(EUR) + " EUR")
    