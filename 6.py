def max_array(a,k):
    # print(k)
    list  = a.split()
    sum=0
    p=[]
    n=len(list)
    pp=k
    for i in range(0,len(list)-k+1):
        l=0
        k=pp
       
        for j in range(i,k):
           
            if(j<=n):
                l=max(l,int(list[j]))
            
        pp=pp+1
        p.append(l)
        l=0
   
    print(p)
a=input()
k=int(input())
max_array(a,k)
