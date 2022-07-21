password = "1234"
i = 0
def iden():
    n = input()
    
    while i < 3:
        if n != password:
            i += 1
            iden()
        else:
            break
iden()
