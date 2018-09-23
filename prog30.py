from datetime import datetime
s1 = raw_input()
s2 = raw_input()
FMT = '%H %M'
tdelta = datetime.strptime(s1, FMT) - datetime.strptime(s2, FMT)
print(tdelta)
