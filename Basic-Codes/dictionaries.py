# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])

# thisdict = {
#     "information" : {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# }
# print(thisdict["information"]["brand"])

thisdict = {
    "information" : {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
}
print(thisdict)

for a in thisdict:
    print(a)

for b in thisdict.keys():
    print(b)

# x = thisdict.get("information")
# print(x)
#
# # y= thisdict.keys()
# # print(y)
# # z = thisdict.values()
# # print(z)
#
# thisdict["information"]["brand"] = "bmw"
# print(thisdict)
#
# thisdict.update({"brand": "rr"})
# print(thisdict)
#
#
# # thisdict.pop("brand")
# # print(thisdict)

for c in thisdict.values():
    print(c)