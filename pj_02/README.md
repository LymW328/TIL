# b
딕셔너리의 키인 vote_average가 8이 넘어야 하는데 어떻게 구현해야 하는지 고민한다.
해결 - 딕셔너리 형대의 정보를 가진 리스트 요소에서 vote_average가 8 이상인 것만 가져오도록 한다!

# c
여러 딕셔너리를 특정 키의 밸류 값으로 정렬하는 방법을 찾는다. 
해결 - 딕셔너리 리스트를 정렬하는 방법을 인터넷에서 찾았다. lambda함수를 쓰는데 잘 모르겠다.

# d
1.새로은 패스를 사용하는데 자꾸 none을 반환한다... 도대체 왜 이러는걸까
2.id 값이 없으면 none 반환
해결
1. 먼저 search/movie 를 통해 id를 찾은 다음, 그 id를 다시 recomandation에 대입해야한다...
2. res[] 대신 res.get() 사용
3. 전제적으로 딕셔너리리스트를 활용하는 방법을 숙지해야한다.


# e
1. api 문서를 보고 crew 와 cast 의 분리와 사용이 중요했다.
2. 봉준호는 직합이 4개라 명세서의 조건대로 해야 잘 나온다.
