from itertools import permutations 
# import itertools
def permutation_subarray(a,k):
    # print(k)
    list  = a.split()
    sum=0
    p=[]
    n=len(list)
    pp=k
    for i in range(0,len(list)):
        if(i<pp):
            p.append(list[i])
        else:
            
            p1=permutations(p)
            p=[]
            # i=i-1;
            pp=pp+k;
            for num in p1: 
                print(num)
            p.append(list[i])    
        
    p1=permutations(p)
    p=[]
    for num in p1: 
        print(num)
            
        
        
            # l = list(permutations(list,range(i, k)))
            # i=i+k
            # k=i+k;
            # print(l)
        
   
    
a=input()
k=int(input())
permutation_subarray(a,k)