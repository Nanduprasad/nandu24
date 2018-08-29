x=int(raw_input())
list=[int(n) for n in raw_input().split()]
list.sort()
print" ".join(map(str,list))
