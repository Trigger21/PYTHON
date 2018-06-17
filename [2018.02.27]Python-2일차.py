"""
Python-2일차(2018.2.27)
"""

"""
[문제7] 아래와 같은 문자데이터가 있습니다. 
"""
url = 'http://www.python.org'

1. http:// 제거한 후 url 변수에 넣어 주세요.
url = url.replace('http://','')  # 치환
url.lstrip('http://')            # 제거
url[7:]                          # 인덱스  

2. url변수에 있는 문자 데이터에 '.'을 기준으로 분리하세요.
url = url.split('.')

3. url변수에 있는 문자데이터를 www.python.org 모양으로 만드세요.
url = '.'.join(url)

4. url변수에 있는 문자데이터를 대문자로 변환하세요.
url.upper()

5. url변수에 있는 문자데이터를 소문자로 변환하세요.
url.lower()

url.capitalize()  # 첫글자는 대문자, 나머지 소문자 ~ initcap
"""
[문제8] 반복문을 사용하지 않고  * 를 가로 100개 출력
"""
print('*'*100)
len('*'*100)  # 100


"""
[문제9] 반복문을 사용하지 않고  * 를 세로 10개 출력
"""
print('*\n'*10)
len('*\n'*10)  # 20 = 10(*) + 10(\n)


## 복습. R의 자료형

"""
1. vector : 같은 데이터 타입을 갖는 1차원 배열구조(R의 기본 데이터 구조)
2. matrix : 같은 데이터 타입을 갖는 2차원 배열구조
3. array : 같은 데이터 타입을 갖는 3차원 배열구조
4. list : 서로 다른 데이터 타입을 갖는 vector 들을 저장하거나 또는 다른 list 저장 가능
5. data.frame : 서로 다른 데이터 타입을 갖는 컬럼으로 이루어진 2차원 테이블 구조
"""

## 2-1. Python의 자료형

## list
  : 서로 다른 데이터 타입을 갖는 1차원 배열구조
    데이터의 목록을 다루는 자료형
    
x = [10,20,30]  
x
len(x)     # 4
type(x)    # list

# 리스트 인덱싱 
x[0]
x[1]
x[2]
x[3]
x[-1]
x[-2]

# 리스트 슬라이싱 : [시작:끝-1]
x[0:2]
x[1:]
x[:-1]  # [10, 20]
x[-1:]  # [30]

# 리스트 값을 수정
x[0] = 100           # 단일값 수정
x[1:3] = [200,300]   # 범위적 수정
x

# 리스트 변수에 끝에 값을 추가
x.append(400)
x

# 기존 리스트 변수에 다른 리스트 변수를 이어 붙이는 방법
x
x1 = [600,700]

x.extend(x1)  # x += x1
x

# 인덱스를 사용하여 특정위치에 값을 입력하는 방법
x.insert(4,500)
x

# +를 이용해서 리스트 변수를 결합하는 방법
x2 = [800,900,1000]
x += x2
x

# 리스트 변수에 있는 값들 중 마지막 값을 제거하는 방법
x
x.pop()  # 1000(마지막 값)
x

# 인덱스 번호에 해당하는 값을 제거하는 방법
x.pop(2)  # 300 제거
x


"""
[문제10] x.pop을 이용해서 다른 리스트 변수에 값을 넣어주세요.
"""
pop = []  # list 미리 선언
x

pop += [x.pop()]
pop

pop.append(x.pop())
pop


# del 함수 사용해서 리스트 인덱스 값을 삭제하는 방법

del x[3]
x


drink = ['콜라','사이다','오렌지주스','사과주스','콜라','사이다','콜라']
drink
type(drink) # list
len(drink)  # 7

drink.count('콜라')   # 3
drink.index('콜라')   # 0
drink.index('콜라',1) # 4
drink.index('콜라',5) # 6

# 리스트 변수에 값을 기준으로 삭제하는 방법 주의사항은 콜라가 3개가 있으면 remove() 3번 수행

drink.remove('콜라')
drink

# 중첩 리스트
x = [1,2,3,['a','b','c'],4,5]
x

x[2:5]
x[3]
x[3][0]
x[3][1]
x[3][2]
x[3][1:3]
x[3][-1]
x[3][:2]

x[3].append('d')  # 내부 리스트에 값 추가
x

del x[3][3]       # 값 제거
x
x[3].remove()

# 중첩 리스트 값 수정
x[3][0] = x[3][0].upper()
x[3][1] = x[3][1].upper()
x[3][2] = x[3][2].upper()
x

# 리스트에 값 수정
x[0] = x[0] * 10
x[1] = x[1] * 10
x[2] = x[2] * 10
x

x[3][0] = x[3][0] * 2
x

※ R과 다르게 한번에 처리는 제한(Python은 프로그램 작성해서 구현해야 함)

# 초기화 하는 방법(변수형은 유지)
x.clear() 
x
type(x)
len(x)


# sort : 리스트 내의 값을 기준으로 정렬

x = [1,5,3,4,2]
x.sort()
x

x.sort(reverse = True)
x

# reverse : 리스트 인덱스 순서를 반대로 뒤집을 때 사용

x = [1,5,3,4,2]
x.reverse()
x


"""
[문제11] food 변수를 생성하시고 아래 문제를 풀어보세요.

>>> food[0]
['김밥', '라면', '오뎅']
>>> food[1]
['비빔밥', '김치찌게']
>>> food[2]
['자장면', '짬뽕']
"""
food = [['김밥','라면','오뎅'],['비빔밥','김치찌게'],['자장면','짬뽕']]
food[0]
food[1]
food[2]


1. 1번 index에 청국장 추가 하세요
food[1].append('청국장')
food[1]


2. 2번 index에 탕수육 추가하세요.
food[2].append('탕수육')
food[2]


3. 0번 index에 있는 오뎅 삭제하세요.
del food[0][2]
food[0]
# food[0].remove('오뎅')
# food[0].pop('오뎅')


4. 0번 index에 튀김, 튀김, 떡복이 한꺼번에 추가하세요
food[0] += ['튀김','튀김','떡복이']
food[0]
# food[0].extend(['튀김','튀김','떡복이'])


5. 2번 index에 2번 위치에 유산슬 추가하세요
food[2].append('유산슬')
food[2]
# food[2].insert(2,'유산슬')


6. 튀김 갯수를 세어주세요
food[0].count('튀김')  # 2
food[1].count('튀김')  # 0
food[2].count('튀김')  # 0


7. 0번 index만 정렬해주세요
food[0].sort()
food[0]
# food.sort(), 중첩 리스트는 한번에 하면 안됨(주의!!), 개별 리스트 먼저 해야함 
# 한변에 하면 각 리스트의 첫번째 값의 순서에 따라 정렬이 됨


8. 0번 index에 마지막 데이터 삭제하세요
food[0].pop()
food[0]



## tuple(튜플) 자료형
   : 리스트와 유사하지만 틀린점은 수정, 삭제, 추가 안 된다.
     리스트 [], 튜플 () 
     * 처리속도 더 빠름 / 읽기전용
     * ex. 색상
     
list1 = []    
type(list1)     

tuple1 = ()
type(tuple1)

tuple2 = 10,20   # tuple로 자동생성
type(tuple2)

tuple3 = (1,)
tuple4 = (1,2,3,4,5)
tuple5 = ('a','b',('ab','cd'))
type(tuple5)

tuple5[0]
tuple5[1]
tuple5[0:2]   # ('a', 'b')
tuple5[2][1]  # 'cd'

a = (1,2,3)
b = (4,5,6)
c = a + b
type(c)


a[0]
a[0] = 10     # 수정불가


del a[0]      # 삭제불가
a          


a.append(4)   # 추가불가
a

# tuple 가능한 method 단 2가지
a.index(1)  # 0
a.count(1)  # 1


# 값 따로 저장(길이가 일치)

a = 1,2,3
type(a)     # tuple

one, two, three = a  # one ← 1, two ← 2, three ← 3

one
two
three


## dictionary
   : key ~ value 
     (R에서 list형 ex. 이름 = 홍길동, 전화번호 = 010-1234-5678, 주소 = 서울)

dic = {'name':'홍길동', 'phone':'01012341234', 'addr':'서울시'}
dic
type(dic)  # dict
len(dic)   # 3

sports = {'축구':'매시', '농구':'커리', '야구':'박찬호'}
sports
type(sports)  # dict
len(sports)   # 3

sports['축구']
sports['컬링'] = '김영미'  # new key & value insert
sports

sports['컬링'] = ['김은정','김경애','김영미','김선영','김초희']
sports  # 중복없음

sports.keys()   # key만 보고 싶을때
sports.values() # values만 보고 싶을때
sports.items()  # key & values 다 볼때

sports['봅슬레이']      # 없는 키 조회시 오류
sports.get('봅슬레이')  # 오류 발생 안함(none return)
-> exception 처리시 사용됨 다음주에 배운다


'컬링' in sports.keys()  # True
'김영미' in sports.values()  # False : 중첩이라서
'매시' in sports.values()  # True

['김은정','김경애','김영미','김선영','김초희'] in sports.values()  # True

del sports['야구']  # 야구 삭제
sports

sports['축구'] = []  # key는 유지하면서 해당 value만 초기화
sports

sports['축구'] = '손흥민'
sports

sports.clear()  # dict 전체 초기화
sports

※ dictionary : R data.frame과 다르다(오개념 금지)


## set type
   : list type 비슷하다. 차이는 index 순서가 없다.
     중복을 허용하지 않는다. 

a = {1,1,1,2,3,3,2}
a
type(a)  # set
len(a)   # 3 : a = {1,2,3}

b = {2,3,4,5}
b

# 합집합

a.union(b)  # {1, 2, 3, 4, 5}
a|b


# 교집합

a.intersection(b)  # {2,3}
a&b


# 차집합

a.difference(b)  # {1}
a-b

b.difference(a)  # {4,5}
b-a


1 in a  # True
6 in b  # False

a[0]    # error
a[1]    # error
a[2]    # error

a.remove(1)  # a에서 1이라는 원소를 삭제
a

a.add(1)     # 1개씩 추가
a.add(4)
a

a.update([5,6,7])  # 여러개 추가
a

x = []      # list
y = ()      # tuple
z = {}      # dict

type(x)
type(y)
type(z)

s = set()   # dict과 기호가 곁쳐서 set은 이렇게 선언
type(s)


