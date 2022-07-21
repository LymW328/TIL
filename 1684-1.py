# water = []
# salts = []
# while 1:
    
#     w, p = map(str, input().split())
#     salt = int(w) * 0.01 * int(p)
#     salts.append(salt)
#     water.append(int(w))
#     if  w  == "DONE" and p == None:
#         ww = sum(salts)
#         ss = sum(salts)
#         print(ss / ww)
#         False





# def pp():
#     while 1:
#         water = []
#         salts = []
#         w, p = map(str, input().split())
        
#         salt = int(w) * 0.01 * int(p)
#         salts.append(salt)
#         water.append(int(w))
#         ww = sum(salts)
#         ss = sum(salts)
#         if  w  == "DONE" and p == 1:
            
#             print(ss / ww)
#             break

# PP()






# water = []
# salts = []
# w, p = map(str, input().split())
# salt = int(w) * 0.01 * int(p)
# salts.append(float(salt))
# water.append(float(w))
# ww = sum(water)
# ss = sum(salts)
# if  w  == "DONE" and p == 1:
    
#     print(ss / ww)
# else:
#     pass


# 조건
# 최대 5개의 소금물을 입력
# 출력된 혼합물의 퍼센트 농도를 반올림하여 소수2자리까지 표현

def pro() :
    dns = []
    wat = []

    while True:
        menu = input(f"{len(dns) + 1} : 농도와 소금물의 양을 띄어쓰기로 구분하여 입력하시오.(DONE 입력 시 종료 : ")
        if menu == "DONE":
            break
        dns.append(float(menu.split()[0]))
        wat.append(float(menu.split()[1]))


        if len(dns) == 5:
            break

    slt = []
    for index in range(len(dns)):
        salt = dns[index] * wat[index] / 100
        slt.append(salt)

    res_dns = sum(dns) / sum(wat) * 100
    print(f"농도 : {round(res_dns),2}% 소금물 양 : {round(sum(wat)),2}")

pro()
    