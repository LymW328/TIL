import requests
from pprint import pprint

def recommendation(title):
    BASE_ULR = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
            'api_key' : "a6cf97bd4b454c941b8d86091ec398b5",
            'language' : 'ko',
            'region' : 'KR',
            'query' : title #왜 문법오류가? 
    }   
    try:
        response = requests.get(BASE_ULR + path, params=params).json() 
        results = response.get('results')
        

        res = results[0] #res는 딕셔너리 기생충, result는 리스트
        # try:
        #     id = (res["id"])
        # except:
        #     print("None")
        id = (res["id"])
    except:
        return("None1")
        
        
    
#이제 얻은  id값으로 추천목록을 얻어보자!


    


    BASE_ULR = 'https://api.themoviedb.org/3'
    path2 = f'/movie/{id}/recommendations'
    params2 = {
            'api_key' : "a6cf97bd4b454c941b8d86091ec398b5",
            'language' : 'ko',
            'region' : 'KR',
            'query' : id
    }
    try:

        response2 = requests.get(BASE_ULR + path2, params=params2).json() 
        results2 = response2.get('results')
        if results2 == []:
            print('[]')
        
        for i in results2:
            print(i["title"])
    except:
        pass



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
