from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# pip install beautifulsoup4 : 해당 패키지 설치, --upgrade 옵션을 붙히면 최신 버전으로 설치
# pip list : 설치된 패키지 리스트 출력
# pip show beautifulsoup4 : 해당 패키지 정보 출력
# pip uninstall beautifulsoup4 : 해당 패키지 삭제