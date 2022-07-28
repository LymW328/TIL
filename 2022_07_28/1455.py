
class Wordrelay():
    # 1. words 리스트를 전달받아 인스턴스 변수로 만드는 생성자를 구현하세요
    # def __init__(self ~~~~ )
    def __init__(self, words):
        self.words =words #?????
        
    # 2. 실패와 성공 여부를 결정하는 함수를 구현하세요
    def check_fail(self):
        past_words = [self.words[0]] #리스트 words의 첫번째 단어
        if len(self.words) == 1: #리스트에 단어가 하나 뿐이라면 
            return -1  # -1을 반환 왜 -1을 반환하는데?
        for i in range(1, len(self.words)): #리스트 words의 단어 수만큼 순환해서
    
            if self
    
    # 3. 결과를 돌려주는 함수를 작성하세요.
    def get_result(self):
        self.get_result = len(res)


if __name__ == '__main__':
    words = ["round","dream","magnet","tweet","tweet","trick","kiwi"]
    wordrelay = Wordrelay(words)
    print(wordrelay.get_result()) # 5번째 참가자가 탈락하였습니다