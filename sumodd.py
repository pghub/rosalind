#!/usr/bin/python
a=4737
b=9343
if(a%2==0):
    a+=1
s=0
while a<=b:
    s+=a
    a+=2
print(s)
