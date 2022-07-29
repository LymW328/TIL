#KOSPI_now 코스피 숫자를 copy selector 해서 가져온 것
import requests
from bs4 import BeautifulSoup
#요청을 보내는 주소
url = "https://finance.naver.com/sise/"
#요청을 보내고 받음(텍스트 데이터를 받음)
response = requests.get(url).text #get 하면 Respons 200반환, .txt 붙이면 txt형식으로 불러온다.

#리스폰스를 변환(텍스트 데이터를 HTML구조로 변환)
data = BeautifulSoup(response)

#원하는 정보 출력
kospi = data.select_one ('#KOSPI_now')#select_one 이라는 함수 사용


print(kospi.text)  #id가 KOSPI_now인 span의 정보를 가져온다.

