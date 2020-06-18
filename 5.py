def without_consonants(s):
    n=len(s)
    p=""
    for i in range(n):
        if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o'or s[i]=='u':
            p+=s[i]
    print(p)

s=input()
without_consonants(s)
