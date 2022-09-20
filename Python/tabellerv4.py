tabel=1 
start=1 
mål=11
while mål <=110:
    print(str(tabel) + "-tabel")
    for i in range (start,mål,start):
        print(i) 
        mål=mål+11 
        start = start+1 
        tabel = tabel + 1