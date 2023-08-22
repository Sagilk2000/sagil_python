import json

""""
storing and exchange of data
"""

# x={'name':'sagil','age':23,'course':'python'}
# print(type(x))
# y=json.dumps(x)   #python to json
# print(y)
# print(type(y))
#
# a='{"name": "sagil", "age": 23, "course": "python"}'
# print(type(a))
# b=json.loads(a)  #json to python
# print(b)
# print(type(b))
# print(b["age"])
#
# json functions
# func = dir(json)
# print(func)


# samplejason="""{
#     "company":{
#         "employee":{
#             "name":"emma",
#             "payable":{
#                 "salary":7000,
#                 "bonus":800
#             }
#         }
#     }
# }"""
# x=json.loads(samplejason)
# print(x)
# print(x['company']['employee']['payable']['salary'])

#
# sampledict="""{"class":{
#     "student":{
#         "name":"sagil",
#         "course":{
#             "python":2023,
#             "angular":2028,
#         "marks":{
#             "physics":70,
#             "english":80
#         }
#         }
#     }
# }
# }"""
# x=json.loads(sampledict)
# print(x)
# print(x['class']['student']['course']['marks']['english'])
