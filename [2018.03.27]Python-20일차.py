"""
Python-20일차(2018.3.27)
"""

## 20-1. OS 컨트롤

# 파일의 크기를 확인
from os.path import getsize

getsize('c:/python/emp.csv')  # 8131


# 디렉토리에 있는 파일확인
import os
import glob

folder = 'c:/python'
file_list = os.listdir(folder)  # 해당경로의 파일목록
file_list


# 특정한 파일들의 목록확인
file = 'c:/python/*.csv'
file_list = glob.glob(file)  # 해당경로의 파일목록
file_list


# 현재 디렉토리 확인
import os
dir = os.getcwd()
dir  

os.chdir('..')  # 상위 디렉토리로 감
os.getcwd() 
os.chdir(dir)  # 원래 디렉토리로 감
os.getcwd()


# 디렉토리 생성
import os
from os.path import exists

dir = input("새로 생성할 디렉토리 이름을 입력하세요 : ")
if not exists(dir):  # 존재여부
    os.mkdir(dir)  # dir 생성
    print('[%s] 디렉토리를 생성했습니다.' %dir)
else:
    print('[%s] 디렉토리는 이미 존재합니다.' %dir)

'''exists : sql 서브쿼리 절에서 체크?'''


# 파일 존재여부 확인
file = 'c:/python/emp.csv'
if exists(file):
    print('[{}] 파일이 존재합니다.' .format(file))
else:
    print('[{}] 파일이 없습니다.' .format(file))


'''
[문제185] 중앙일보에서 인공지능에 기사 검색을 한 후 그 내용을  아래와 같이 저장하세요.

Enter the file name and file location : c:/20180327/중앙일보.txt
'''
from bs4 import BeautifulSoup as bs
import urllib.request as req

url = 'http://search.joins.com/JoongangNews?Keyword=%20%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=JoongangNews&PeriodType=All&ScopeType=All&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&TotalCount=0&StartCount=0&IsChosung=False&IssueCategoryType=All&IsDuplicate=True&Page=1&PageSize=10&IsNeedTotalCount=True'
html = req.urlopen(url)
soup = bs(html,'html.parser')
l = soup.findAll('strong',class_='headline mg')
text = ''
for i in l:
    tmp = i.a.get('href')
    res = req.urlopen(tmp)
    sp = bs(res,'html.parser')
    # <div id="article_body" itemprop="articleBody" class="article_body mg fs4">
    txt = sp.find('div',id="article_body")
    text += txt.get_text(strip=True) + '\n'
text = text.replace('\xa0',' ')
text = text.replace('\u2027',' ')

file = 'c:/python/20180327/중앙일보.txt'
if exists(file):
    print('기존 파일에 덮어쓰겠습니다.')
    with open(file,'a') as file:
        file.write(text)
else:
    print('새로 생성하였습니다.')
    with open(file,'w') as file:
        file.write(text)   
        

# 상욱형
import urllib.request
from bs4 import BeautifulSoup
import urllib.request as req
import re 

# c:/20180327/중앙일보.txt

dir = input("Enter the file name and file location : ")

dir[:11]

if not exists(dir[:11]):
    os.mkdir(dir[:11])
    print('[%s] 디렉토리를 생성했습니다.'%dir[:11])
else :
    print('[%s] 디렉토리는 이미 존재합니다.'%dir[:11])
    
url = "http://news.donga.com/search?p=1&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
p = soup.findAll('p',{'class':'tit'})
u2 = []
for link in p:
    for i in link.find_all('a',attrs={'href':re.compile('http://news.donga.com/3/')}):
        u2.append(i.attrs['href'])
u2


b = []
for i in u2:
    res = req.urlopen(i)
    soup= BeautifulSoup(res, "html.parser")
    l = soup.findAll('div',{'class':'article_txt'})
    for j in l:
        text = j.get_text(strip=True)
        text = re.sub('\ufeff',' ',text)
        b.append(text[:text.find('function')])
        b.append('='*90)
        
b

with open(dir,"w") as file:
    for i in b:
        file.write(i+'\n')

# 선생님 풀이
import urllib.request
from bs4 import BeautifulSoup
import os
from os.path import exists

def get_save_path():  # 입력값으로 크롤링한 결과를 저장
    save_path = input("Enter the file name and file location : " )
    save_path = save_path.replace("\\", "/")
    if not exists(os.path.split(save_path)[0]):  # ('디렉토리', '파일') 분리
        os.mkdir(os.path.split(save_path)[0])
    return save_path


def fetch_list_url():
    params = []

    for i in range(1,3):
        list_url = " http://search.joins.com/JoongangNews?page=" + str(i) + "&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=JoongangNews"
    
        url = urllib.request.Request(list_url)
        res = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(res, "html.parser")
        for j in range(0,10):
            soup2 = soup.find_all('div',class_="text")[j]  # page당 url 담으려고
            soup3 = soup2.find('a')['href']
            params.append(soup3)
    return params  # url list


def fetch_list_url2():
    params2 = fetch_list_url()  # url list
    f = open(get_save_path(),'w',encoding="utf-8")  # 입력한 경로(파일)에 생성
    for i in params2:
        list_url2 = i
        url2 = urllib.request.Request(list_url2) 
        res2 = urllib.request.urlopen(url2).read().decode("utf-8")  
        soup = BeautifulSoup(res2, "html.parser")

        result = soup.find_all('div',id="article_body")[0]
        final = result.get_text(strip=True, separator='\n')  # 마지막줄에 '\n'
        f.write(final+"\n\n")  # 게시글 간의 간격부여
    f.close()  # 필수


fetch_list_url2()
        
        
# 강현주 학우님의 면접 후기
t-value 어린아이에게 설명할 수 있을 정도로 해라
머신러닝 질문
강화학습
알고리즘 설명 / 사용법
도메인(domain) : 문자로 표시한 인터넷 주소
기업 및 산업군의 필요 다름
통계학 석사
책 추천 : 예측마케팅


## 20-2. css(cascading stylesheets) 선택자

from bs4 import BeautifulSoup

html = """
<html>
<body>
<div id = "lecture1">
    <h1>데이터 과학</h1>
</div>
<div id = "lecture2">
    <h1>빅데이터 분석</h1>
    <ul class = "subject">
        <li>SQL 강좌</li>
        <li>R 강좌</li>
        <li>PYTHON 강좌</li>
    </ul>
</div>
</body>
</html>"""

soup = BeautifulSoup(html,'html.parser')

soup.h1.string  # '데이터 과학'
soup.find('h1').string
soup.find('h1').get_text()

# select_one은 css 선택자 요소 하나를 추출
soup.select_one('div > h1').string  # '데이터 과학'

soup.select_one('div#lecture1 > h1').string  # id 대신 #을 사용

soup.select_one('div#lecture2 > h1').string 

subject = soup.select('div#lecture2 > ul.subject > li')  # select : 2개 이상, .이 class
                
for i in subject:
    print(i.string)

# 네이버 환율에서 미국꺼 크롤링
<div class="head_info point_dn">
							<span class="value">1,070.30</span>
							<span class="txt_krw"><span class="blind">원</span></span>
							<span class="change"> 9.20</span>
							<span class="blind">하락</span>
						</div>

from bs4 import BeautifulSoup as bs 
import urllib.request as req

url = 'http://info.finance.naver.com/marketindex/'
res = req.urlopen(url)
soup = bs(res,'html.parser')
dollar = soup.select_one('div.head_info > span.value').string
change = soup.select_one('div.head_info > span.change').string
print('USD/KRW',dollar,change)


#우클릭 - copy - copy selector
soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').string
jpy = soup.select_one('a.head.jpy > div.head_info > span.value').string
print('JPY/KRW', jpy)



soup.find('span',class_='value')


