import requests
from pprint import pprint
#https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=<<api_key>>&language=en-US

def credits(title):
    BASE_ULR = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
            'api_key' : "a6cf97bd4b454c941b8d86091ec398b5",
            'language' : 'ko',
            'region' : 'KR',
            'query' : title #왜 문법오류가? 
    }   
    response = requests.get(BASE_ULR + path, params=params).json() 
    results = response.get('results')
    

    res = results[0] #res는 딕셔너리 기생충
    try:
        id = (res["id"])
    except:
        print("None")


        BASE_ULR = 'https://api.themoviedb.org/3'
    path2 = f'/movie/{id}/credits'
    params2 = {
            'api_key' : "a6cf97bd4b454c941b8d86091ec398b5",
            'language' : 'ko',
            'region' : 'KR',
            'query' : id
    }
    response2 = requests.get(BASE_ULR + path2, params=params2).json() 
    crews = response2.get('crew') #배우이름
    casts = response2.get('cast') #디렉터 이름
    cr =[]
    cs = []
    for i in casts:
        if int(i['cast_id']) < 10:
            cs.append(i['name'])

    for i in crews:
        if i['department'] == 'Directing':
            cr.append(i['name'])

    res = {'cast' : cs, 'directing' : cr}
    return(res)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    
    # None
