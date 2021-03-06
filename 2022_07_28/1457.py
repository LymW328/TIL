# words = ["round","dream","magnet","tweet","tweet","trick","kiwi"]
# print(wordrelay(words)) # 5번째 참가자가 탈락하였습니다.



class Fee():
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance


    # 렌탈 비용 계산
    def get_total_rental(self):
        return self.time / 10 * 1200


    # 보험료 계산
    def get_total_insurance(self):
        if self.time == 50:
            self.time = 60
        else:
            pass
        return self.time / 30 * 525

    
    # 주행 요금 계산
    def get_total_drive(self):
        if self.distance > 100:
            self.distance = (self.distance-100) + (self.distance-100)* 0.5
        return self.distance * 170


    def get_fee(self): #이렇게 매직 메서드를 작성하거나
        return self.get_total_rental() + self.get_total_insurance() + self.get_total_drive()


if __name__ == '__main__':
    time, distance = map(int, input('렌탈비용과 주행거리를 띄워쓰기로 구분하여 입력하세요 : ').split())
    fee_instance = Fee(time, distance)
    print(fee_instance) # 이것 대신 print(fee_instance.get_fee())사용