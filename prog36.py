import re
z=raw_input()
new=re.sub('[\w]+','',z)
print(len(new))
