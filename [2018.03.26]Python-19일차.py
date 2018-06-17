"""
Python-19일차(2018.3.26)
"""

## 19-1. 크롤링(BeautifulSoup)

pip install beautifulsoup4

from bs4 import BeautifulSoup

html = """
<html>
<body>
<h1> 스크래핑 </h1>
<p> 웹페이지 분석하기 </p>
<p> 데이터 정제작업하기 </p>
</body>
</html>"""

# html 분석
soup = BeautifulSoup(html, "html.parser")  

# 원하는 태그 내용 가지고 오기(단계별 써줌)
h1 = soup.html.body.h1
h1.string  # 태그를 제외한 내용만 출력
h1.string.strip()

p1 = soup.html.body.p
p1.string
p1.string.strip()

# p 형제를 찾아 나서자
p1.next_sibling  # '\n'
p1.next_sibling.next_sibling  # <p> 데이터 정제작업하기 </p>

p2 = p1.next_sibling.next_sibling
p2.string
p2.string.strip()


---------


html = """
<html>
<body>
<h1 id = 'title'> beautifulsoup </h1>
<p id = 'subtitle'> 스크래핑 </p>
<p> 데이터 추출하기 </p>
</body>
</html>"""


# find method : 조건에 맞는 제일 첫번째만 찾고 끝나는 녀석
soup = BeautifulSoup(html,"html.parser")
soup.find(id = 'title').string  # html에서 id가 title인 부분의 속성만 보기

title = soup.find(id = 'title')
title.string  # ' beautifulsoup '

soup.find(id = 'subtitle').string

soup.find('h1').string
soup.find('p').string


soup.find('title').string

----------

html = """
<html>
<body>
<ul>
<li><a href = "http://www.itwill.co.kr">아이티윌</a></li>
<li><a href = "http://www.naver.com">네이버</a></li>
</body>
</html>"""


# 순서대로 찾기
soup = BeautifulSoup(html,"html.parser")
a1 = soup.html.body.ul.li.a
a1.string

a1

soup.find('li').next_sibling.next_sibling.a


link = soup.find_all('a')  # find_all : 다 찾음
link

for i in link:
    print(i.attrs['href'])  # url 보기
    print(i.string)

    

# a.html 간단한 거 만듬
 - utf-8로 메모장으로 저장.
'''
<html>
<head>
<title> 나의 홈페이지 </title>
</head>
<body>
<p align = 'center'> 환영합니다. </p>
<p align = 'left'> 이름: 홍길동 <br> 나이 : 20
<br> 취미: 노래하기 </p>
<p align = 'right'> 오늘 하루도 많이 많이 행복하세요 </p>
<a href = 'https://www.itwill.co.kr' class='cafe1' id='link1'> 아이티윌 </a>
<a href = 'https://www.naver.com' class='cafe2' id='link2'> 네이버 </a>
<a href = 'https://www.google.com' class='cafe3' id='link3'> 구글 </a>
</body>
</html>
'''

with open('c:/python/a.html', encoding = 'UTF8') as html:
    soup = BeautifulSoup(html,'html.parser')    
    
soup.prettify  # html 이상유무 검증
    
soup.find('title').string
soup.find('body')
soup.find('p').string    
    
l = soup.findAll('p')  # p tag 전부다 가져온다
for i in l:
    print(i.get_text()) # get_text() : text만 가져옴   
    
    
soup.find('body').get_text()   
soup.find('body').get_text(strip=True)  # '/n' 사라지고 한줄로 보기
soup.find('body').string  # X
 

l = soup.find('body')  # error
for i in l:
    print(i.string)    
    
    
l = soup.findAll('body')  # good
for i in l:
    print(i.get_text())  # 줄별로 보기
    

soup.find('a')
l = soup.findAll('a')

# 문자값만
for i in l:
    print(i.get_text())

# url만
for i in l:
    print(i.attrs['href'])

# class만
for i in l:
    print(i.attrs['class'])


soup.findAll('a',{'class':'cafe1'})  # a 중 class가 cafe1 만 보기

l = soup.findAll('a',{'class':'cafe3'}) 
for i in l:
    print(i.get_text())


l = soup.findAll('',{'class':'cafe1'}) 
for i in l:
    print(i.get_text())


l = soup.findAll('a',{'id':'link1'}) 
for i in l:
    print(i.get_text())


soup.findAll(class_='cafe1')  # soup.findAll('',{'class':'cafe1'}) 
for link in soup.findAll('a'):
    print(link.get('href'))
    # print(link.attrs['href'])


soup.find(['a','p'])

l = soup.findAll(['a','p'])
for i in l:
    print(i.get_text())

# 원하는 문자가 있는지 찾을때
    
soup.findAll(text='환영합니다.')

import re  # like 연산자,  grep 함수처럼 문자패턴
soup.findAll(text=re.compile('환영'))

soup.findAll('p')
soup.findAll('p',limit=1)  # limit : 출력 갯수 제한

# https:// 인 것들만 골라서 출력
for link in soup.findAll('a', attrs = {'href':re.compile('https://')}):
    print(link.get('href'))


http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp
beautifulsoup에서 분석만 가능하고 가져오는 기능은 없다

from bs4 import BeautifulSoup # 내용을 뽑아내는 기능
import urllib.request as req  # 웹사이트에서 가져오는 기능

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
res = req.urlopen(url) 
soup = BeautifulSoup(res,'html.parser')

soup.find('title').string  # title 내용
soup.find('wf').string  # wf 내용


'''
[문제180]이 주소로 접속하셔서 게시글을 출력하세요.

http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106
'''
from bs4 import BeautifulSoup as bs
import urllib.request as req

url = 'http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106'
res = req.urlopen(url)
soup = bs(res, 'html.parser')

l = soup.findAll('p',{'class':'con'})
for i in l:
    print(i.get_text(strip=True))


http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=1&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&

for i in range(1,17):
    url = 'http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page='+str(i)+'&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&'
    res = req.urlopen(url)
    soup = bs(res, 'html.parser')
    l = soup.findAll('p',{'class':'con'})
    for j in l:
        print(j.get_text(strip=True))


# 선생님 풀이
from bs4 import BeautifulSoup
import urllib.request as req

url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
res = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser")
result = soup.find_all('p', class_="con")
for i in result:
    print(i.get_text(strip=True))



url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url = urllib.request.Request(url)
res = urllib.request.urlopen(url).read().decode("utf-8")  # utf-8이 아닌 거 대비
soup = BeautifulSoup(res,"html.parser")
result = soup.find_all('p', class_="con")
for i in result:
    print(i.get_text(strip=True))
    

'''
[문제181] 게시글 뿐만 아니라 게시날짜 정보도 같이 출력하시오 !

2017.04.12 19:48 레이디버그 3기나오면 좋은사람 손~~
'''
for i in range(1,17):
    url = 'http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page='+str(i)+'&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&'
    res = req.urlopen(url)
    soup = bs(res, 'html.parser')
    l = soup.findAll('li',{'class':'spot_'})  # span, p의 상위
    for j in l:
        print(j.find('span',{'class':'date'}).string+' '+j.find('p',{'class':'con'}).get_text(strip=True))


for i in soup.findAll("", {'class':['con', 'date']}):
    print(i.get_text(strip = True))


# 선생님 풀이
from bs4 import BeautifulSoup
import urllib.request as req
url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
res = req.urlopen(url)
soup= BeautifulSoup(res, "html.parser")
a = soup.find_all('p',class_="con")  # 게시글
b = soup.find_all('span',class_="date")  # 날짜정보
print(b[0].get_text())
print(b[0].text)

cnt= 0
for i in a:
    print(b[cnt].text,i.get_text(strip=True))
    cnt += 1

print(cnt)


'''
[문제182] 게시판에 게시글 전부를 수집해주세요.
'''
text = []
for i in range(1,17):
    url = 'http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page='+str(i)+'&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&'
    res = req.urlopen(url)
    soup = bs(res, 'html.parser')
    l = soup.findAll('p',{'class':'con'})
    for j in l:
        text.append(j.get_text(strip=True))
text


'''
[문제183] 게시판에 게시글 전부를 수집한 후 공백문자를 기준으로 분리한후 빈도수를 체크해 주세요.
'''
dict = {}
for i in text:
    tmp = i.replace('\r\n',' ').split()
    for j in tmp:
        if j not in dict:
            dict[j] = 1
        else:
            dict[j] += 1
dict['레이디버그']  # 69
sorted(dict.items(), reverse = True, key = lambda x : x[1])[:10]



# 동아일보 - 인공지능 관련 기사 크롤링
for i in range(1,1000,15):
    print(i)

from bs4 import BeautifulSoup as bs
import urllib.request as req

url = 'http://news.donga.com/search?p=1&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1'
res = req.urlopen(url)
soup = bs(res,'html.parser')
l = soup.findAll('p', class_='tit')
for i in l:
    url1 = i.a.get('href')
    # print(url1)
    res = req.urlopen(url1)
    soup = bs(res,'html.parser')
    h = soup.find('div', class_='article_txt')
    print(h.get_text(strip=True).split('function')[0])
    # print(h.get_text(strip=True)[:h.get_text(strip=True).find('function')])


url = 'http://news.donga.com/BestClick/3/all/20180326/89298642/1'
res = req.urlopen(url)
soup = bs(res,'html.parser')
l = soup.find('div', class_='article_txt')
print(l.get_text(strip=True)[:h.get_text(strip=True).find('function')])
for i in l:
    url1 = i.a.get('href')
    res = req.urlopen(url1)
    soup = bs(res,'html.parser')
    h = soup.find('div', class_='article_txt')
    print(h.get_text(strip=True).split('function')[0])


# 쿠루쿠루 버스
from urllib.request import Request, urlopen
contentt =[]
def abc(x):    
    req = Request('http://www.kurukurubus.com/front/community/travelreview/main?currentPage='+x, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = BeautifulSoup(html, "html.parser")
    for i in soup.findAll(class_='txt-l'):
        req = Request("http://www.kurukurubus.com/"+i.attrs['onclick'][16:69], headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(req).read()
        soup = BeautifulSoup(html, "html.parser")
        contentt.append(soup.find(class_='ask_text').get_text(strip=True))
        print(soup.find(class_='ask_text').get_text(strip=True))
        
for i in range(1, 50):
    abc(str(i))

len(contentt)
cnt = 0

for i in contentt:
    cnt += i.find('가성비')

cnt






