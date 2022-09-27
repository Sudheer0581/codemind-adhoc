n=int(input())
arr=list(map(int,input().split()))
k=int(input())
d={}
s=set(arr)
m=0
for i in s:
    d[i]=arr.count(i)
    if(arr.count(i)>m):
        m=arr.count(i)
l=[]
l1=[]
l2=[]
for i in range(k):
    for j in d.keys():
        if(d[j]==m):
            if(len(l1)==0):
                l1.append(j)
            else:
                l1.append(j)
    l1.sort()
    l2=l1[::-1]
    #print(l2)
    l.extend(l2)
    l1=[]
    l2=[]
    m=m-1
for i in range(k):
    print(l[i],end=" ")
                