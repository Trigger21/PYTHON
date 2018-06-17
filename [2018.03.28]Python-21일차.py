"""
Python-21일차(2018.3.28)
"""

from bs4 import BeautifulSoup

html = """
<ul id = '조선왕'>
<li id = '태조'>'이성계'</li>
<li id = '정종'>'이방과'</li>
<li id = '태종'>'이방원'</li>
<li id = '세종'>'이도'</li>
<li id = '문종'>'이향'</li>
</ul>"""

soup = BeautifulSoup(html,'html.parser')

soup.select_one('li#세종').string
soup.select_one('li#세종').text
soup.select_one('li[id="세종"]').text

soup.select_one('#세종').text
soup.find(id='세종').text
soup.select_one('ul > li#세종').string
soup.select_one('#조선왕 #세종').text
soup.select_one('#조선왕 #문종').text
soup.select_one('ul#조선왕 > li#태종').text

soup.select_one('li:nth-of-type(1)').text
soup.select_one('li:nth-of-type(2)').text
soup.select_one('li:nth-of-type(3)').text
soup.select_one('li:nth-of-type(4)').text
soup.select_one('li:nth-of-type(5)').text

lst = soup.select('li')
for i in lst:
    print(i.text)


soup.select('li')[0].string
soup.select('li')[1].string
soup.select('li')[2].string
soup.select('li')[3].string
soup.select('li')[4].string


soup.find_all('li')[0].string
soup.find_all('li')[1].string
soup.find_all('li')[2].string
soup.find_all('li')[3].string
soup.find_all('li')[4].string



## 21-1. 과일 채소 html 문서작성
'''
<html>
<body>
<div id = "goods">
<h1>과일 야채 상품 리스트</h1>
<ul id = "fruits">
<li class = "red green">사과</li>
<li class = "purple">포도</li>
<li class = "yellow">레몬</li>
<li class = "yellow">귤</li>
</ul>

<ul id = "vegetable">
<li class = "white green" data-lo = "ko">무우</li>
<li class = "red green" data-lo = "us">파프리카</li>
<li class = "black purple" data-lo = "ko">가지</li>
<li class = "white" data-lo = "cn">연근</li>
<li class = "black" data-lo = "us">올리브</li>
</ul>
</div>
</body>
</html>
'''

file = open("c:/python/fv.html", encoding = "utf-8")  
soup = BeautifulSoup(file,"html.parser")

soup.select_one("li:nth-of-type(6)").string
soup.select_one('#vegetable > li:nth-of-type(2)').text
soup.select_one('#vegetable > li.red.green').text
soup.select_one('#vegetable > li.green').text
soup.select('#vegetable > li.green')[1].string

soup.select_one("li:nth-of-type(4)").string
soup.select("#fruits > li.yellow")[0].string
soup.select("#fruits > li.yellow")[1].string

            
soup.select("li.yellow")[1].string     
soup.select("li.green")  # 사과, 무우, 파프리카
soup.select("li.green")[2].string        
            

# 두가지 이상 조건 만족 찾기           
condition = {"data-lo":"us","class":"red"}  # us & red          
soup.find('li',condition).text  # 파프리카            
            
soup.find(id = "vegetable").find("li",condition).string            
            


## 21-2. https://ko.wikisource.org            

import urllib.request as req

url = 'https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%ED%95%9C%EC%9A%A9%EC%9A%B4'            
html = req.urlopen(url)
soup = BeautifulSoup(html,'html.parser')

soup.select_one('#mw-content-text > div > ul:nth-child(9) > li:nth-child(1) > a')  # error : nth-child 안됨         
            
lst = soup.select('#mw-content-text > div > ul > li > a')    

for i in lst:
    print(i.string)            



## 21-3. 한겨례 신문사
from urllib.request import urlopen

url = 'http://img.hani.co.kr/imgdb/resize/2018/0328/152214693895_20180328.JPG'

'''
이 이름으로 pc에 저장을 하고 싶다.
'''
imgname = url.split('/')[-1]
imgname

with urlopen(url) as f:  # url
    with open("c:/python/"+imgname,'wb') as w:  # wb : binary로 write
        img = f.read()
        w.write(img)




## 21-4. Selenium

'''웹브라우저를 컨트롤하여 웹 UI(User Interface)를 지정하는 도구'''
'''웹 자동화 도구'''
 - 써야되는 이유 : 로그인하면서 크롤링을 한번에 하려면 동적으로 해야됨

# 1.설치
pip3 install selenium

# 2.selenium 드라이버 설치
http://phantomjs.org

webdriver.Firefox
webdriver.Chrome
webdriver.le
webdriver.Opera
webdriver.PhantomJS(CLI : Command Line Interface 형식의 브라우저)

# 사용할 webdriver를 import 함
from selenium import webdriver

# 캡쳐할 사이트 
url = "http://www.hani.co.kr/"  

# PhantomJS 드라이버 : 전체 스캔
driver = webdriver.PhantomJS("c:/python/phantomjs.exe")
driver

# 드라이버를 초기화 될 때까지 3초간 대기
driver.implicitly_wait(3)

# 웹페이지 읽어 들인다.
driver.get(url)

# 스크린샷을 저장
driver.save_screenshot("c:/python/hani.png")

# 드라이버 종료 브라우저를 닫는다
driver.quit()

''' phantom은 숨어서 조작'''

selenium으로 캡쳐할때 화면 background가 transparent이면 검은색이 디폴트로 돼서 보기 별로 안좋은 것 같더라고요
driver.execute_script("var body = document.getElementsByTagName('body')[0]; body.setAttribute('background-color', 'white')")
driver.execute_script('document.body.style.background = "white"')
driver.save_screenshot("desktop/python/hani.png")


# chromedriver 드라이버 : 보여지는 것만 스캔
driver = webdriver.Chrome("c:/python/chromedriver.exe")
driver.get(url)
driver.save_screenshot("c:/python/hani1.png")
driver.quit()


## 21-5. 네이버 로그인 화면(프로그램으로 로그인 하기)
from selenium import webdriver
user = "hbk3828"
mypass = "*******"
driver = webdriver.PhantomJS("c:/python/phantomjs.exe")
driver.implicitly_wait(3)
url = 'https://nid.naver.com/nidlogin.login'
driver.get(url)
inputid = driver.find_element_by_id("id")  # input요소를 찾는 method, id값 찾는 method
inputid.clear()  # 입력박스에 있는 텍스트 지우기
inputid.send_keys(user)  # 입력박스에 아이디 입력

inputpw = driver.find_element_by_id("pw")  # 비밀번호 입력하는 input요소 찾기
inputpw.clear()  # 입력박스에 있는 텍스트 지우기
inputpw.send_keys(mypass)  # 입력박스에 비번 입력

# 로그인 버튼
#<input type="submit" title="로그인" alt="로그인" tabindex="12" value="로그인" 
#class="btn_global" onclick="nclks('log.login',this,event)">

loginbtn = driver.find_element_by_css_selector("input.btn_global[type = submit]")  # 로그인 버튼 찾기
loginbtn.submit()  # 아이디 비번 전송
print("로그인 성공")

driver.get("https://order.pay.naver.com/home/search?serviceGroup=SHOPPING&range.fromDate=2017.01.01&range.toDate=2018.03.28&tabMenu=SHOPPING")
html = driver.page_source

'''여기까지 selenium'''

soup = BeautifulSoup(html,'html.parser')
lst = soup.select('div.p_info > a > span')

for i in lst:
    print(i.get_text(strip=True))


from selenium import webdriver

driver = webdriver.PhantomJS("c:/python/phantomjs.exe")
driver = webdriver.Chrome("c:/python/chromedriver.exe")
driver.implicitly_wait(3)
driver.get("http://google.com")
#res = driver.execute_script("return 10+20")
#print(res) # 30 : javascript 돌아간 것

driver.execute_script("window.alert('구글에 오신걸 환영합니다')")  # 알림창


## 21-6. selenium으로 DOM요소를 선택하는 방법
'''DOM(Document Object Model)은 html/xml 문서를 처리하는 API'''

# DOM내부 최초값 단일로 추출하는 메소드(find)
find_element_by_id("id") : id속성으로 요소를 하나 추출
find_element_by_name("name") : name 속성으로 요소를 하나 추출
find_element_by_css_selector(query) : css선택자로 요소 하나를 추출
find_element_by_xpath(query) : xpth를 지정해서 요소 하나를 추출
find_element_by_tag_name(name) : tag name을 지정해서 요소하나 추출
find_element_by_link_text(text) : 링크 텍스트로 요소 하나를 추출
find_element_by_partial_link_text(text) : 링크의 자식요소에 포함되어 있는 텍스트로 요소 하나를 추출
find_element_by_class_name(name) : 클래스 이름에 해당하는 요소 하나를 추출

# DOM내부 여러개 모두 추출하는 메소드
find_elements_by_css_selector(query)
find_elements_by_xpath(query)
find_elements_by_tag_name(name)
find_elements_by_link_text(text)
find_elements_by_partial_link_text(text)
find_elements_by_class_name(name)


# DOM요소에 적용 할 수 있는 메소드
clear() : 글자를 입력할 수 있는 요소의 글자를 지운다.
click() : 요소를 클릭
get_attribute(name) : 요소의 속성중에 name에 해당되는 속성의 값을 추출
screenshot(filename) : 화면을 캡쳐해서 이미지 파일로 저장
send_keys(value) : 키를 입력해서 보낸다.(텍스트 데이터로 보낸다)

  * value가 텍스트 데이터가 아닌경우(특수키, 함수키, enter, tab, ctrl) 아래를 쳐라

from selenium.webdriver.common.keys import Keys

ARROW_DOWN / ARROW_LEFT / ARROW_RIGHT / ARROW_UP
BACKSPACE / DELETE / HOME / END / INSERT
ALT / COMMAND / CONTROL / SHIFT / ENTER / ESCAPE / SPACE / TAB
F1 ~ F12

submit() : 입력 양식을 전송 
value_of_css_property(name) : name 해당하는 css 속성 값을 추출



