# the captain's Room

d=input()  #get rid of first line 
a=input().split()  #store all to array
s1=set()  #all unique room number
s2=set()  #all unique room number occur more than once
for i in a:
    if  i in s1:
        s2.add(i)
    else:
        s1.add(i)
s3=s1.difference(s2)
print (list(s3)[0])