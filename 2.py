def palindrome(s):
    s1 = "".join(reversed(s))
    f=0
    for i in range(len(s)):
        if s1[i]!=s[i]:
            f=1
        
    if f==0:
        print("is palindrome")
    else:
        print("not palindrome")

s=input()
palindrome(s)
