def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return (a / b)
    except:
        return ("0으로 나눌 수 없습니다.")
        #return 대신 print 하면 터미널에 none이 같이 떠버린다!

    

