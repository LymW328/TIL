# 탑승객 수(passengers) 와 요금(fare)를 받는다.
class PublicTransport():
    current_ps = 0
    acc_ps = 0
    # 탑승객 수와 요금을 입력받아 초기화하는 메서드
    # def __init__~~~
    def __init__(self, ps, fee): #ps 말고 passenger로 써야되나?
        self.ps = ps
        self.fee =fee


    # 탑승 메서드
    # passenger 를 파라미터로 받음
    # 새로 탄 승객에 따라 총 요금에 추가
    def get_in(self, ps):
        PublicTransport.current_ps += int(ps)
        PublicTransport.acc_ps += int(ps)

    # 내리는 메서드
    # 승객 수만 감소
    def get_off(self, ps):
        PublicTransport.current_ps -= int(ps)
        
    # 현재 탑승중인 인원과 최종 수익을 출력
    def profit(self):
        print(f'탑승인원 : {self.current_ps} / 총 수익 : {self.current_ps * self.fee}') #버스도 쓰게 하려면-PublicTransport.acc_ps 가 아니라 self.acc_ps로 바꿔야 한다!

#버스 클래스를 만드는 곳

class Bus(PublicTransport):
    current_ps = 0 
    acc_ps = 0

    def __init__(self, ps, fee, limit): 
        self.ps = ps
        self.fee =fee
        # 위 2 줄은 이걸로 대체 가능 =  super().__init__(ps, fee)
        self.limit = limit

    # 메쏘오드 오버 라이드~~~~!
    def get_in(self, ps): #limit보다 많은 인원이 타려고 할떄, 가령 limit은 10인데 11명이 타려고 하면..? 그냥 리미트....??
        if self.limit < Bus.current_ps + ps: # self.ps(인스턴스) 가 아니라 ps(매개변수)가 와야한다! - 왜? - self.ps는 인스턴스 변수!(_init__의 ps 인 0이 대입된다!)
            print("더 이상 탑승할 수 없습니다.")
        else:
                                                        
            Bus.current_ps += int(ps)
            Bus.acc_ps += int(ps)
            


if __name__ == '__main__':
    transport = PublicTransport(0, 100)
    transport.get_in(20)
    transport.get_in(10)
    transport.get_in(40)
    transport.get_off(30)
    transport.profit() # 탑승인원 : 40 / 총 수익 : 7000
    bus1 = Bus(0, 150, 20)
    bus1.get_in(10)
    bus1.get_in(5)
    bus1.get_in(6)
    bus1.get_in(4)
    bus1.profit()
