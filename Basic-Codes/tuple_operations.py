thistuple =("A","B","C","D")
a = list(thistuple)
a.append("E")
thistuple=tuple(a)
print(a)

abtuple = ("A","B","C","D")
i = 0
while i< len(abtuple):
    print(abtuple[i])
    i=i+1

#tuplemethod

thistuple = ("A","B","C","D","A")
i = thistuple.count("A")
print(i)

B=thistuple.index("C")
print(B)