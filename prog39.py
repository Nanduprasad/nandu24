a=raw_input().split()
largest=a[0]
for large in a:
    if large > largest:
        largest=large
print(largest)
