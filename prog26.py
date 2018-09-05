n=raw_input()
list=[int(n) for n in raw_input().split()]
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] > list[j]:
           list[i], list[j] = list[j], list[i]
print list
