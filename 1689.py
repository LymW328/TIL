a = [1,1,3,3,0,1,1]
res = []
for i in range(len(a)-1):
    
    if a[i] == a[i+1]:
        res.append(a[i])
print(res)
