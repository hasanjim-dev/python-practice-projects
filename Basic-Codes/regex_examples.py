# import re
# txt = "The rain in Spain"
# x = re.findall("[a-z]", txt)
# print(x)

import re
text = "1 is speacial character"
pattern = "^1"
a = re.findall(pattern,text)
print(a)

if a :
    print("yes,1 is a speacial character")
else :
    print("no,1 is not a speacial character")