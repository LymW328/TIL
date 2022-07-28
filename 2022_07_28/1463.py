# 탑승객 수(passengers) 와 요금(fare)를 받는다.
class PublicTransport():
    current_ps = 0
    acc_ps = 0
    # 탑승객 수와 요금을 입력받아 초기화하는 메서드
    # def __init__~~~
    def __init__(self, ps, fee):
        self.ps = ps
        self.fee =fee


    # 탑승 메서드
    # passenger 를 파라미터로 받음
    # 새로 탄 승객에 따라 총 요금에 추가
    def get_in(self, passenger):
        PublicTransport.current_ps += int(passenger)
        PublicTransport.acc_ps += int(passenger)

    # 내리는 메서드
    # 승객 수만 감소
    def get_off(self, passenger):
        PublicTransport.current_ps -= int(passenger)
        
    # 현재 탑승중인 인원과 최종 수익을 출력
    def profit(self):
        print(f'탑승인원 : {PublicTransport.current_ps} / 총 수익 : { PublicTransport.acc_ps* self.fee}')





if __name__ == '__main__':
    transport = PublicTransport(0, 100)
    transport.get_in(20)
    transport.get_in(10)
    transport.get_in(40)
    transport.get_off(30)
    transport.profit() # 탑승인원 : 40 / 총 수익 : 7000