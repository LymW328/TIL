
class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0
    
    def __init__(self, name, spec):
        self.name = name
        self.spec = spec
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1
        

    def bark(self):
        print(f"{self.name}가 짖습니다.")
    
    @classmethod
    def get_status(cls):
        print(f"현재 강아지 수는 {cls.num_of_dogs}이고 오늘까지 {cls.birth_of_dogs}마리가 태어났습니다.")

    @classmethod #w죽으면 모든 강아지의 카운트 수가 줄어드니까
    def dead(cls):
        Doggy.num_of_dogs -= 1
        # print(f"{cls.name}가 죽었습니다. 현재{cls.num_of_dogs}남았습니다." )
        print(f"누군가 죽었습니다...현재{cls.num_of_dogs}마리 남았습니다." )
        

    # @classmethod #소멸자를 사용한 dead카운트

dog1 = Doggy("말복이", "말티즈")
dog2 = Doggy("중복이", "말티즈")
dog3 = Doggy("초복이", "말티즈")
print(dog1.name)
print(dog1.spec)
dog1.bark()
dog1.get_status()
dog1.dead()
dog4 = Doggy("다복이", "말티즈")
dog1.get_status()
