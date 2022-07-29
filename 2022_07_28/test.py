words = ["kiwi", "intergral", "leader", "bool","lead", "done"] #done 을 넣어 해봤습니다.

lose = []
res = []

for i , word in enumerate(words):
    a = i-1
    
    
    
    
    if word == "done":
        print(f"탈락한 사람은  {lose}번 입니다.") #틀린 것들 리스트로 모아서 출력해보자

        
    elif i == 0:
        res.append(word[-1]) #첫번쨰 단어라면 res에 첫번쨰 단어 마지막 글자를 더한다.
        
        
    
    #     continue
    elif res[a] != word[0]: #res의 마지막 글자가 다음 word의 첫글자가 다르면?  #오류가 나는 이유를 모르겠다 ㅠㅠ... - i-1을 if 문 밖 for문 안에 a로 지정하고 했더니 작동한다! 왜지?
        lose.append(i+1)
        res.append(word[-1])
    else:
        res.append(word[-1]) # 같으면 res에 word 마지막 글자를 더해준다.
    
