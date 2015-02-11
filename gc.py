fo = open("/Users/pierre/Downloads/rosalind_gc.txt", "r")
id = ""
dict = {}

def gcContent(s):
    return float(s.count("G")+s.count("C"))/float(len(s))*100

for line in fo.readlines():
    if(line.startswith(">")):
        id = line
        dict[id] = ""
    else:
        dict[id]+=line[:-1]

keyMax=""
gcMax = 0
for key, value in dict.items():
    print(key,gcContent(value), " vs ", gcMax, "length ", len(value))
    if gcContent(value) > gcMax:
        gcMax = gcContent(value)
        keyMax = key
print(keyMax.replace(">",""))
print(gcMax)       
