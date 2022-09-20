tabel1=1
tabel2=2
tabel3=3
tabel4=4
tabel5=5
tabel6=6
tabel7=7
tabel8=8
tabel9=9
tabel10=10

print("Hej, hvilken tabel vil du se? Vælg en ved at skrive et tal mellem 1-10")
valg=input()
if valg == "1":
    while tabel1 <=10:
        print (tabel1)
        tabel1= tabel1 + 1
elif valg == "2":
    while tabel2 <=20:
        print (tabel2)
        tabel2= tabel2 + 2
elif valg == "3":
    while tabel3 <=30:
        print (tabel3)
        tabel3= tabel3 + 3
elif valg == "4":
    while tabel4 <=40:
        print (tabel4)
        tabel4= tabel4 + 4
elif valg == "5":
    while tabel5 <=50:
        print (tabel5)
        tabel5= tabel5 + 5
elif valg == "6":
    while tabel6 <=60:
        print (tabel6)
        tabel6= tabel6 + 6
elif valg == "7":
    while tabel7 <=70:
        print(tabel7)
        tabel7= tabel7 + 7     
elif valg == "8":
    while tabel8 <=80:
        print (tabel8)
        tabel8= tabel8 + 8
elif valg == "9":
    while tabel9 <=90:
        print (tabel9)
        tabel9= tabel9 + 9
elif valg == "10":
    while tabel10 <=100:
        print (tabel10)
        tabel10= tabel10 + 10
else:
    print("Oops something went wrong :)")