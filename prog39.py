alist=[int(n, 10) for n in raw_input().split()]
largest=alist[0]
for large in alist:
    if large > largest:
        largest=large
print(largest)
