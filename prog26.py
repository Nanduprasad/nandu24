n=raw_input()
l=[int(n) for n in raw_input().split()]
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]
print l
