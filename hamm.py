fo = open("/Users/pierre/Downloads/rosalind_hamm.txt", "r")

string1 = fo.readline()[:-1]
string2 = fo.readline()[:-1]

dH, i, N = 0, 0, len(string1)
while i < N:
    if(string1[i]!=string2[i]):
        print("found at i=",i)
        dH+=1
    i+=1
print("dH=",dH)
