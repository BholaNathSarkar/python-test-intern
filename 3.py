from collections import Counter 
  
def Remove(s):
    s=s.split(" ") 
    # print(s)
    for i in range(0, len(s)): 
        s[i] = "".join(s[i]) 
    # print(s)    
    p=Counter(s)
   
    s = " ".join(p.keys()) 
    print (s) 
if __name__ == "__main__": 
    s=input()
    Remove(s)
