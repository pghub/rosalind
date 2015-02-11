fo = open("/Users/pierre/Downloads/rosalind_cons.txt", "r")
id = ""
DNA = {}

def printMatrix(testMatrix):
    for i in range(4):
        if(i==0):
            print "A:",
        elif(i==1):
            print "C:",
        elif(i==2):
            print "G:",
        elif(i==3):
            print "T:",
        for j in range(len(testMatrix[i])):
              print testMatrix[i][j],
        print

for line in fo.readlines():
    if(line.startswith(">")):
        id = line
        DNA[id] = ""
    else:
        DNA[id]+=line[:-1]

strandLength = len(DNA[DNA.keys()[0]])
profileMatrix = [[0]*strandLength for i in range(4)]

for key,value in DNA.items():
    i=0
    while i < len(value):
        if(value[i]=="A"):
            profileMatrix[0][i]+=1
        elif(value[i]=="C"):
            profileMatrix[1][i]+=1
        elif(value[i]=="G"):
            profileMatrix[2][i]+=1
        elif(value[i]=="T"):
            profileMatrix[3][i]+=1
        i+=1
        

consensus = [""]*strandLength

for j in range(len(profileMatrix[0])):
    currentMax = 0
    rowMax = 0
    for i in range(4):
        if(profileMatrix[i][j] > currentMax):
            currentMax = profileMatrix[i][j]
            rowMax = i
    if(rowMax == 0):
        consensus[j] = "A"
    elif(rowMax == 1):
        consensus[j] = "C"
    elif(rowMax == 2):
        consensus[j] = "G"
    elif(rowMax == 3):
        consensus[j] = "T"

print "".join(consensus)

printMatrix(profileMatrix)
