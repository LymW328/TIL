
class Wordrelay():
    lose = []                                                                                       # 1. words 리스트를 전달받아 인스턴스 변수로 만드는 생성자를 구현하세요
                                                                                                # def __init__(self ~~~~ )
    def __init__(self, words):
        self.words =words  #list words를 초기화 하는 생성자 words라는 리스트를 인스턴스 변수로 지정해서 새로 인스턴스 메소드를 만들때마다 참조되도록
        # self.lose = [] #진 사람을 넣어놓는 lose 리스트는 초기화 되면 안된다... 왜냐면 계속 누적되어야 하기 때문에 - 그렇다면 clss 변수로 써볼까?
    # 2. 실패와 성공 여부를 결정하는 함수를 구현하세요
    def check_fail(self):
        first_word = [self.words[0]] #리스트 words의 첫번째 단어
        while len(self.words) == 1: #리스트에 단어가 하나 뿐이라면 
            print('끝말잇기는 혼자서 할 순 없습니다...')
            break



    # 3. 결과를 돌려주는 함수를 작성하세요.
    def get_result(self):
        res = check.fail()
        return f'탈락한 사람은 {lose}입니다.' #lose를 클래스 매소드로 해야하나?


if __name__ == '__main__':
    words = ["round","dream","magnet","tweet","tweet","trick","kiwi"]
    wordrelay = Wordrelay(words)
    print(wordrelay.get_result()) # 5번째 참가자가 탈락하였습니다