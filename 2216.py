a,b,c = map(int, input().split())
if a == b ==c :
    print("정삼각형")
elif a == b != c or a != b == c or a == c != b :
    print("이등변 삼각형")
elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 ==  a**2 + c**2:
    print("직각 삼각형")
elif  a + b < c or a + c < b or b + c < a:
    print("삼각형")
else :
    print("삼각형이 아닙니다.")