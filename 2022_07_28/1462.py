class Person():
    # 생성자로 만들때
    def __init__(self, name, age):
        self.name = name
        self.age = age

 


    #클래스 메소드로 만들때
    @classmethod
    def detail(cls, name, year):
        age = 2022 - int(year) + 1 #지역변수이다!
        return cls(name, age)


    def check_age(self):
        if self.age > 19:
            return  False #'성인' 
        else:
            return True #'미성년자'

        

p1 = Person('아유타', 10)
print(p1.check_age())
p2 = Person.detail("가람", 2020)
print(p2.check_age())