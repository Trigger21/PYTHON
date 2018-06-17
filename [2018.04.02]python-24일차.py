"""
python-24일차(2018.4.2)
"""
'''
[문제186] 도혜숙의 '밤벚꽃' 시 구절중에 일부분 입니다.
	문장이 도용 되었는지 판별해 주세요.

sentence1 = "해는 이미 져버린 지 오래인데 벚꽃은 피고 있었다"  # 진짜
sentence2 = "벚꽃은 피고 있었다 해는 이미 져버린 지 오래인데"  # 짝퉁


ratio, word = sentence_compare(sentence1, sentence2, 2)
print("두글자 비교 : ", ratio, word)
두글자 비교 :  0.9230769230769231 ['해는', '는 ', ' 이', '이미', '미 ', ' 져', '져버', '버린', '린 ', ' 지', '지 ', ' 오', '오래', '래인', '인데', '벚꽃', '꽃은', '은 ', ' 피', '피고', '고 ', ' 있', '있었', '었다']
'''
sentence1 = "해는 이미 져버린 지 오래인데 벚꽃은 피고 있었다"  # 진짜
sentence2 = "벚꽃은 피고 있었다 해는 이미 져버린 지 오래인데"  # 짝퉁

def sentence_compare(s1,s2,n):
    res1 = []
    res2 = []
    for i in range(len(s1)):
        res1.append(s1[i:i+n])
    for j in range(len(s2)):
        res2.append(s2[j:j+n])
    del res1[-(n-1):]
    del res2[-(n-1):]
    cnt = 0
    for i in res1:
        if i in res2:
            cnt += 1
    return cnt/len(res1), res1
    
ratio, word = sentence_compare(sentence1, sentence2, 2)
print("두글자 비교 : ", ratio, word)


a = ['a','b','c','d']
a[2:5]

def sum_str(arg):
    res = ''
    for i in arg:
        res += i
    return res

sum_str(a[2:5])
res = ''
(lambda *x : x)(a[2:5])

''.join(a[2:5])


# 선생님 풀이 : ngram 논문 참조(유사성 판단하는 알고리즘)
def ngram(s,num):
    res = []
    slen = len(s) - num + 1
    for i in range(slen):
        ss = s[i:i+num]
        res.append(ss)
    return res

def sentence_compare(s1, s2, num):
    x = ngram(s1, num)
    y = ngram(s2, num)
    w = []
    cnt = 0
    for i in x:
        for j in y:
            if i == j:  
                cnt += 1
                w.append(i)
    return cnt / len(x), w


sentence1 = "해는 이미 져버린 지 오래인데 벚꽃은 피고 있었다"
sentence2 = "벚꽃은 피고 있었다 해는 이미 져버린 지 오래인데"

ratio, word = sentence_compare(sentence1, sentence2, 2)
print("두글자 비교 : ", ratio, word)



## 24-1. N-gram
''' 
- 문장의 유사도
- 텍스트에서 이웃한 n개의 문자를 의미
- 서로 다른 2개의 문장을 N-gram으로 비교해서 단어의 종류, 빈도를 확인
- 활용분야 : 논문도용, 작사, 라이센스를 가지고 있는 코드를 복사 등
- 예 : 게시판 크롤링 후 활용 
'''


## 24-2. class

'''
adder(3)
adder(4)

결과는 7이 출력되게 하세요.
'''

res = 0

def adder(n):
    global res  # 전역변수를 내부에서 사용
    res += n
    return res

adder(3)
adder(4)


'''왜 class가 필요할까?
절차(구조적) 지향 프로그램의 제약을 극복하기 위해 아래의 예시를 보고 잘 이해해 보자!
두 사람이 동시에 위 프로그램을 사용하려 한다면 2개를 만들어야 할 것이다. 그런데 굳이 그럴 필요가 있을까?
하나의 프로그램으로는 할 수 없을까?'''

res1 = 0
def adder_1(n):
    global res1  # 전역변수를 내부에서 사용
    res1 += n
    return res1  

res2 = 0
def adder_2(n):
    global res2  # 전역변수를 내부에서 사용
    res2 += n
    return res2  

# 홍길동
adder_1(3)
adder_1(4)

# 박찬호
adder_2(3)
adder_2(4)


# class 생성 : 객체지향 프로그램 
class Calculater:
    def __init__(self):
        self.result = 0  # 초기값
        
    def adder(self,num):  # 메소드
        self.result += num
        return self.result
    
# 홍길동
'''위 class 사용하려면 메모리에 구축 인스턴스화 해야함'''
cal_1 = Calculater()  # cal_1의 이름으로 class를 사용
cal_1.adder(3)
cal_1.adder(4)


# 박찬호
cal_2 = Calculater()
cal_2.adder(3)
cal_2.adder(4)


''' 서로 다른 결과를 얻을 수 있다. 즉 하나의 프로그램으로 성공, 재활용 재사용성이 좋음'''

def person(name,age):
    info = "이름:" + name + "," + "나이:" + str(age)
    return info

person("홍길동",30)
person("송혜교",20)


info = ''
def person(name,age):
    global info
    info += "이름:" + name + "," + "나이:" + str(age) + '\n'
    return info

person("홍길동",30)
person("송혜교",20)

print(info)


m_info = ''
def person_m(name,age):
    global m_info
    m_info += "이름:" + name + "," + "나이:" + str(age) + '\n'
    return m_info

w_info = ''
def person_w(name,age):
    global w_info
    w_info += "이름:" + name + "," + "나이:" + str(age) + '\n'
    return w_info

print(person_m("홍길동",30))
print(person_w("홍길",30))


''' 만약에 핸드폰 번호까지 추가해야 한다면 2개 프로그램에 같은 작업을 반복해야 한다. 유지보수 힘듬'''

class Insa:
    def __init__(self):
        self.info = ''
    def person(self,name,age):
        self.info += "이름:" + name + ', ' + "나이:" + str(age) + '\n'
        # return self.info


a = Insa()
a.person('홍길동',30)
a.person('박찬호',20)
print(a.info)


b = Insa()
b.person('순둥이',20)
b.person('끼순이',22)
print(b.info)


# 객체 지향 프로그래밍
'''
- 객체 : 사물, 개념 중에서 명사로 표현할 수 있는 것들을 의미한다.
   예) 사람, 건물, 학생, 마피아 등

- 클래스 : 객체를 설명해 놓은 것(객체의 설계도, 틀)
   예) 붕어빵 기계, 
    
- 인스턴스 : 클래스를 메모리에 만들어서 사용하도록 하는 의미

ex) 사람
속성 : 팔, 다리, 머리, 눈, 코, 입, 이름, 키, 나이, 주민번호, 학번, 성적, 성격
    -> 수치, 값으로 표현

메소드 = 함수 : 기능의 프로그램, 속성처리, 동작하는 것들 의미, 속성의 값을 변경시키는 기능

* 클래스 안에는 변수와 메소드가 들어있다.
'''

class myClass:
    pass # 함수, 클래스에서 아무 작업하지 않을 떄 사용

# class 선언(설계도)    
class Person:
    name = '홍길동'  # 속성(사람을 표현하는 수치적인 값)
    age = 10  # 속성(사람을 표현하는 수치적인 값)
    
    def myPrint(self):  # 메소드(self 자기자신의 클래스를 의미)
        print('이름은 {}' .format(self.name))
        print('나이는 {}' .format(self.age))

# 클래스를 기반으로 하는 인스턴스 생성(실체화)
pinstance = Person()
pinstance.myPrint()

# 똑같은 클래스를 가지고 여러개의 인스턴스를 생성할 수 있다(재사용)
pinstance2 = Person()
pinstance2.myPrint()


class Person:
    name = '홍길동'
    age = 10
    def myPrint(self):
        print('이름은 {}' .format(self.name))
    def myAge(self):
        print('나이는 {}' .format(self.age))


p1 = Person()
p1.myAge()
p1.myPrint()

p2 = Person()
p2.name = '박찬호'
p2.age = 20

p2.myPrint() # 변경된 속성값으로 나옴(마치 global 변수와 같다)
p2.myAge()

'''도서관에서 책 하나 빌려서 처음부터 끝까지 가상코딩 돌려라(일종의 마이드맵, 문제답문제답)'''

# 새속성 추가
p2.job = '프로그래머' # 새로운 속성을 인스턴스 내에서 추가가능
print('직업은',p2.job)



name = '손흥민'
class myName:
    def mySet(self, setname):
        self.name = setname  # 입력값 이름에 저장
    def myPrint(self):
        print(name)  # self 미사용, 클래스 밖에 있는 변수를(속성) 사용
        print(self.name)  # 자신의 클래스에 있는 변수 사용
        
p1 = myName()
p1.mySet('홍길동')
p1.myPrint()


class myClass:
    def __init__(self,value):
        self.value = value
        print("인스터스가 만들어 졌습니다.", self.value)
    def __del__(self):
        print("인스턴스가 소멸되었습니다.")
        
        
def myFunc():
    myC = myClass(1004)  # 함수안에서 클래스를 인스턴스 생성 가능

myFunc()

 
# 자동으로 작동해야 하는 프로그램은 대부분 

'''
__init__ (생성자) : 클래스를 인스턴스화 될 때 자동으로 생성자가 실행, 자동으로 초기화 해준다.(선택옵션)

 * 인스턴스화 ~ 트리거 
 * init 변수 value 값만큼 더 넣어줘야함(즉, 1004)

__del__ (소멸자) : 인스턴스가 종료될 때 자동으로 실행
'''









