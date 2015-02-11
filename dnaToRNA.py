str = open("/Users/pierre/Downloads/rosalind_revc.txt", "r").readline()
i=0
ans=""
while i < len(str):
    if(str[i]=="A"):
        ans="T"+ans
    elif(str[i]=="T"):
        ans="A"+ans
    elif(str[i]=="C"):
        ans="G"+ans
    elif(str[i]=="G"):
        ans="C"+ans
    i+=1
print(ans)
