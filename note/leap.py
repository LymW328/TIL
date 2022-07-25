def leap_year(n):
    if n % 400 ==0:
        return f"{n}년은 윤년입니다."
    elif n % 4 == 0 and n % 100 != 0:
        return f"{n}년은 윤년입니다."
    else:
        return f"{n}년은 윤년이 아입니데이."