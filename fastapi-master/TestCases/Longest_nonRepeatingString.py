# Task 2: Problem 2
def lcp(s, t):
    n = min(len(s),len(t))
    for i in range(0,n):
        if(s[i] != t[i]):
            return s[0:i]
    else:
        return s[0:n]

str = "abdgoalputabdtypeabd"
lrs=""
n = len(str)
for i in range(0,n):
    for j in range(i+1,n):
        x = lcp(str[i:n],str[j:n])
        if(len(x) > len(lrs)):
            lrs=x
print("Longest repeating sequence: "+lrs)