#인기 영화의 목록 수를 출력


import requests
def popular_count():
    #1. url 정보 설정
    BASE_ULR = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
            'api_key' : "a6cf97bd4b454c941b8d86091ec398b5",
            'language' : 'ko',
            'region' : 'KR'
    }

    #2. 요청 및 응답
    response = requests.get(BASE_ULR + path, params=params).json()
    #path까지가 url이고, params변수에 해당하는 정보를 가져온다.
    results = response.get('results')
    return(len(results))
print(popular_count())
