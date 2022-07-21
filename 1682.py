# infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
# res = 0
# for i in infos:
    
#     for key, value  in i.items():
#         if key == 'age' :
#             res += value

# print(res)



def pos():
    infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
    res = 0
    for i in infos:
        res += i['age']

    print(res)
pos()