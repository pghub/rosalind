fo = open("/Users/pierre/Downloads/rosalind_ini5.txt", "r")
i = 0
for line in fo.readlines():
    if(i%2 == 0):
        i+=1
    else:
        print(line)
        i+=1
    
