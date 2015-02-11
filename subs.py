import sys
fo = open("/Users/pierre/Downloads/rosalind_subs.txt", "r")

string = fo.readline()[:-1]
print("string "+string)
substring = fo.readline()[:-1]
print("sub "+substring)
      
answers = list()

print(len(string))

i, N = 0, len(string)
while i < N:
    k = string.find(substring,i)
    if(k>0):
        print("found at k=",k)
        answers.append(k+1)
        i=k+1
    else:
        break

for j in answers:
    sys.stdout.write(str(j)+" ")
print
