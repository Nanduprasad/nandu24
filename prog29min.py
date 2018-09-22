MINUTES_PER_HOUR=60
minutes=int(input())
hours=minutes/MINUTES_PER_HOUR
minutes=minutes%MINUTES_PER_HOUR
print("%2d %2d"%(hours,minutes))
