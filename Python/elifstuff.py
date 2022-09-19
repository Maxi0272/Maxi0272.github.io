from imghdr import what
from xmlrpc.client import APPLICATION_ERROR


print ("what is your name?")
name = input()
print ("what is your age?")
age = input()
if name =="alice":
    print ("hi, alice")
elif age < 12:
    print ("mindre end 12")

elif age > 100:
    print ("større ned 15")

elif age < 3000:
    print ("næsten 3000")

else:
    print ("thats not a number!")