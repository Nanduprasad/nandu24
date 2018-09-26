string1,string2=raw_input().split()
count1=0
count2=0
for i in string1:
      count1=count1+1
for j in string2:
      count2=count2+1
if(count1<count2):
      print(string2)
elif(count1==count2):
      print(string1 or string2)
else:
      print(string1)

      
      
