import attridict
# from attrdict import AttrDict as attridict

a = {"aa": 11, "bb": 22}
# att = attridict(a)
att = attridict(a, bb=33)


print(att)
# # att = attridict.from_nested_dicts(a)
# att.aa.bb = "22"
# print(att)


# data = {
#     "a": "aval",
#     "b": {
#         "b1": {
#             "b2b": "b2bval",
#             "b2a": {
#                 "b3a": "b3aval",
#                 "b3b": "b3bval"
#             }
#         }
#     }
# }

# # att = attridict.from_nested_dicts(data)
# att = attridict(data)
# print(att.b.b1.b2a.b3b)  # -> b3bval