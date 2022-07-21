n = int(input())

if n % 400 ==0:
    print("윤년입니다.")
elif n % 100 != 0 and n % 4 == 0 :
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")

