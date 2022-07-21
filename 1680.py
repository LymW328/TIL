f= input().split(",")
print(f)
res= []
for i in f:
    i = i.lower()
    if i[:6] == 'rotten':
        b = i[6:]
        res.append(b)
    else:
        res.append(i)    
    
    print(res)




# def p():
#     fruits = input('무슨 과일인가요? : ')
#     f= fruits.split(',')
    
#     res = []
#     for i in f:
#         i = i.lower()
#         if i[:6] == 'rotten':
#             i = i[6:]
#         res.append(i)
#     print(res)
        

# p()