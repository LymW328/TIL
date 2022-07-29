import random

class Students():
    # 초기화 인스턴스 메서드
    def __init__(self, lst):  #초기화 메서드는 인자로 학생이름으로 구성된 리스트를 받는다.
        
        self.lst = students_list

   

    def pick(self, lst, n):
        return random.sample(self.lst, self.n)

    def match_pair(self):
        if len(students) % 2 == 1: #학생들 명단이 홀수라면
            ?
        return 


    # 2. 학생들 인자에서 인자 n 명 만큼 랜덤으로 추출하여 return 하는 pick 함수 작성
    # 참고 - random.sample 함수를 검색해보세요.

    # 3. 랜덤으로 2명(명단의 수가 홀수면 한 팀은 3명) 매칭하여 리스트로 반환하는 함수 match_pair 작성


if __name__ == '__main__':
    students_list = ['김싸피', '금해피', '테스트', '철수킴', '박영희']
    students = Students(students_list)
    # print(students.match_pair())
    print(students.pick(,2))