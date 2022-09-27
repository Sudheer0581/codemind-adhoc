n=int(input())
a=list(map(int,input().strip().split()))
k=0
for i in a:
    if a.count(i)==1:
        k=1
        print(i,end=' ')
if(k==0):
    print("-1")