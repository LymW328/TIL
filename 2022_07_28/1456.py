class Calculator(): #왜 괄호가 존재하는가
    # def __init__(self,a,b): #생성자는 도대체 왜 쓰는건가. 안쓰면 또 왜 안쓰는 건가. - add같은 인스턴스 메서드들은 애초에 지역변수만을 참조하기에 인스턴스 변수를 초기화할 필요 없다...
    #     self.a = a #인스턴스 변수 정의
    #     self.b = b
    def add(self, a,b):
        return a + b 
        
    def sub(self, a,b):
        return a - b

    def mul(self, a,b):
        return a * b

    def div(self, a,b):
        try:
            return a / b
        except:
            return "0으로 나눌 수 없습니다."

res = Calculator()
print(res.add(1,5)) #!
print(res.add(3,5)) 





# 혹은 

class Calculator(): #왜 괄호가 존재하는가
    def __init__(self,a,b): #생성자는 도대체 왜 쓰는건가. 안쓰면 또 왜 안쓰는 건가.
        self.a = a #인스턴스 변수 정의
        self.b = b

    def add(self,a):
        return self.a + self.b +a
        
    def sub(self, a,b):
        return self.a - self.b

    def mul(self, a,b):
        return self.a * self.b

    def div(self, a,b):
        try:
            return self.a / self.b
        except:
            return "0으로 나눌 수 없습니다."
res = Calculator(1, 2) #!
print(res.add(3))