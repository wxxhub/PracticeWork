s = input()
s1 = "ab"
#print(s.find(s1))
for n in range(0,len(s)):
    if s.find(s1)!= -1:
        s = s.replace("ab", "AB", 1)
        pass
    pass
print(s)