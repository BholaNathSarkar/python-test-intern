def num(n):
    p=[]
    f=0
    
    for j in range(2,n):
        for i in range(2,j):
            if j%i==0:
                f=1
                break;
        if f==0:
            p.append(int(j))
        f=0    
    # print(p)
    n1=len(p)
    a=0
    b=0
    f=0
    for i in range(n1-1):
        for j in range(i+1,n1):
            if (p[i]+p[j])==n:
                a=p[i]
                b=p[j]
                f=1

    if f==1:
        print(a,b)
        # print(b)
    else:
        print("-1")
n=int(input())
num(n)
