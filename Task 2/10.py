n=int(input())

s = set(map(int,input().split()))

N=int(input())

for i in range(N) :

    choice=input().split()
    if choice[0]=="pop" : # remove random item
        s.pop()
    elif choice[0]=="remove" : # remove specifice item
        s.remove(int(choice[1]))
    elif choice[0]=="discard" :# remove specifice item
        s.discard(int(choice[1])) 
print(sum(s))