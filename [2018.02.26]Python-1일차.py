"""
Python-1일차(2018.2.26)
"""

print('오늘도 행복하자')


## 1-1. 변수

- 메모리 포인터
- 첫글자는 영문, _(밑줄)
- 두번째 글자부터 영문자, 숫자, _
- 대소문자 구분한다
- 길이 제약없다
- 예약어는 사용할 수 없다

import keyword
keyword.kwlist

x = 10
type(x)


## 1-2. 사칙연산
1+2
2-1
1-2
2*3
7/2 
7//2  # 몫 계산
7%2   # 나머지 계산
2**3  # 2^3

import math
math.pow(2,3)  # 2^3

1+2*3*2**3  # 49(** > * > +)

a = 1
a = a + 1
a


## 1-3. 연산자 축약으로 사용

a += 1  # a = a + 1
a -= 1  # a = a - 1
a *= 2  # a = a * 2
a /= 2  # a = a / 2

type(a)  # float : 실수

type(10)  # int : 정수
type(10.12)  # float : 실수

f = 10.4e-3  # e : 지수표현, 10.4*10**-3
type(f)  # float


## 1-4. 논리연산자

x = 1
y = 2 

y > x   # True
y >= x  # True
y < x   # False
y <= x  # False
x == y  # False
x != y  # True

2 > 1 and 3 > 2  # True
2 > 1 and 3 < 2  # False
2 > 1 or 3 < 2   # True
not 1 > 2  # True

"""
[문제1] x,y 변수에 있는 값을 기준으로 수행한 결과 입니다. 
        x 와 y 변수에 어떤 값이 있어야 하나요.
        또한 결과값이 나오기 위해서 어떤 계산식을 만들어야 하는지 
        계산식을 만들어 보세요.


result_1 =  7
result_2 =  3
result_3 =  -3
result_4 =  10
result_5 =  0.4
result_6 =  0
result_7 =  2
result_8 =  32
result_9 =  7.0
result_10 =  -21
result_11 =  50
result_12 =  29
"""

x = 2
y = 5

result_1 = x + y
result_1

result_2 = y - x
result_2

result_3 = x - y
result_3

result_4 = x * y
result_4

result_5 = x/y
result_5

result_6 = x//y
result_6

result_7 = y//x
result_7

result_8 = x**y
result_8

result_9 = (result_2/result_4 + result_5) * result_4  # float(result_1)
result_9  

result_10 = result_1 * result_3
result_10

result_11 = x * y ** x  # result_4 ** x
result_11

result_12 = (x ** x) + (y ** x)
result_12


## 1-5. 문자열

작은 따옴표 '대한민국'
큰 따옴표 "대한민국"

'''대한민국
대한민국'''

"""대한민국
대한민국"""

escape 문자

\n : 줄바꿈
print('대한민국\n대한민국')

\t : tab key
print('잘하자\t파이썬')

\0 : null
print('잘하자\0파이썬')

\\ : \표시
print('잘하자\\파이썬')

\' : 단일 인용부호
print('잘하자\'파이썬\'')
print("잘하자'파이썬'")

\" : 이중 인용부호
print('잘하자\"파이썬\"')
print('잘하자"파이썬"')


x = '김태효'
y = 'UFC'

type(x)  # str
type(y)  # str

x + y  # '김태효UFC'
(x + y) * 2  # '김태효UFC김태효UFC'

print("=" * 10)  # R : repeat()
print("hello world")
print("=" * 10)

# %s : 문자를 포멧에 넣을 때
s1 = 'R'
s2 = 'PYTHON'
print("나는 %s 전문가입니다. 지금은 %s 공부에 빠져있습니다." %(s1,s2))

# %d : 숫자를 포멧에 넣을 때
n1 = 100
n2 = 200
print('%d + %d = %d' %(n1,n2,n1+n2))

# '%%' : % 넣을 때
print("지금 행복지수는 작년에 비해 %d%% 증가했습니다" %n2) 


## 1-6. 인덱싱 & 슬라이싱

x = "행복한 하루 보내자"
len(x)  # 10

x[:]         # 전체 x[0:len(x)]
x[0]         # '행'
x[1]         # '복'
x[len(x)-1]  # '자'
x[-1]        # '자'
x[-2]        # '내'
x[0:3]       # 0~2 슬라이싱 할 때 마지막은 +1 해줘야 함
x[:3]        # '행복한'
x[3:]        # ' 하루 보내자'
x[4:-4]      # '하루'

※ 1. 인덱스 0부터 시작
   2. x[시작요소번호:끝요소번호-1]


"""
[문제_2] v_str 변수에 이 문자열을 입력하세요. 
"""

v_str = "시간은 멈추지 않습니다. 하루를 유익하게 살아야합니다."



1. "시간은 멈추지 않습니다." 만 출력해주세요
v_str[:13]



2. "하루를 유익하게 살아야합니다." 만 출력해주세요
v_str[14:]



3. "살아야합니다."  만 출력해주세요
v_str[23:]



4. "시추니루하야"  이 글자만 출력해주세요.
v_str[0::5]
v_str[::5]


5. "시간은 멈추지 않습니다. 하루를 유익하게" 만 출력해주세요.
v_str[:-8]



6. v_str 문자열을 뒤순으로 출력해 주세요.
v_str[-1::-1]
v_str[::-1]


"""
[문제_3] 

>>> x = '파리썬'
>>> x
'파리썬'

인덱스를 이용해서 리 -> 이로 변환하세요.
"""

x = '파리썬'
x
x = x[0]+'이'+x[2]  # 부분 재입력
x


"""
[문제_4] 포맷문자를 이용해서 출력하세요.
"""

1. 안녕하세요. {제임스} 입니다. 즐겨듣는 음악은 {클래식} 입니다.
n = '제임스'
m = '클래식'
print("안녕하세요. {%s} 입니다. 즐겨듣는 음악은 {%s} 입니다." %(n,m))
print("안녕하세요. {} 입니다. 즐겨듣는 음악은 {} 입니다." .format(n,m))


2. {996} 를 {8} 나누면 {4} 가 나머지입니다
x = 996
y = 8
print("{%d} 를 {%d} 나누면 {%d} 가 나머지입니다" %(x,y,x%y))
print("{} 를 {} 나누면 {} 가 나머지입니다" .format(x,y,x%y))


3. {996} 를 {8} 나누면 {124}는 몫이고 {4} 나머지입니다
print("{%d} 를 {%d} 나누면 {%d}는 몫이고 {%d} 나머지입니다" %(x,y,x//y,x%y))
print("{} 를 {} 나누면 {}는 몫이고 {} 나머지입니다" .format(x,y,x//y,x%y))


# 몫과 나머지 동시에 구하는 함수
res_1, res_2 = divmod(x,y)
res_1, res_2  # (124,4)
res_1         # 124
res_2         # 4


print("원주율은 %f 입니다." %3.14159)
print("원주율은 {} 입니다." .format(3.14159))


## 1-7. 문자함수

x = 'hellow world'
     
- startswith() : 원본 문자열이 매개변수로 입력한 문자열로 시작되는지를 판단

x.startswith('he')  # x라는 변수에 'he'라는 문자로 시작됩니까? (boolean)
x.startswith('H')   # False

- endswith() : 원본 문자열이 매개변수로 입력한 문자열로 끝나는지를 판단

x.endswith('ld')    # True
x.endswith('D')     # False

- x.find() : 원본 문자열 안에 매개변수로 입력한 문자열이 존재하는 위치를
             앞에서 부터 찾는다. 만약에 존재하지 않으면 -1로 나온다.

x.find('w')         # 5
x.find('W')         # -1
x.find('world')     # 7


- rfind() : 원본 문자열 안에 매개변수로 입력한 문자열이 존재하는 위치를 
            뒤에서 부터 찾는다.

x.rfind('h')        # 0
x.rfind('w')        # 7
x.rfind('d')        # 11


- x.count() : 원본 문자열 안에 매개변수로 입력한 문자열이 몇 번 나오는지에 대한 건수

x.count('l')        # 3
x.count('s')        # 0


x = '        hello         '
x

x.lstrip()          # 'hello          '
x.rstrip()          # '        hello'
x.strip()           # 'hello'


- isalpha() : 원본 문자열이 숫자, 기호를 제외한 알파벳, 한글로 이루어졌는지 확인

x = 'hello'
y = 'hello2018'
z = '안녕하세요'

x.isalpha()         # True
y.isalpha()         # False
z.isalpha()         # True


- isalnum() : 원본 문자열이 알파벳 또는 숫자로 이루어져 있는지 확인

x.isalnum()         # True
y.isalnum()         # True
z.isalnum()         # True


- isnumeric() : 원본 문자열이 수로만 이루어져 있는지 확인

x.isnumeric()       # False
y.isnumeric()       # False
z.isnumeric()       # False

d = '1234'
d.isnumeric()       # True


- replace() : 원본 문자열에서 찾고자 하는 문자열을 치환

x = "hello world"
x = x.replace("world", "python")
x                   # 'hello python'

x = "파리썬"
x = x.replace("리", "이")
x                   # '파이썬'


- split() : 매개변수로 입려한 문자열을 기준으로 원본 문자열을 나눠 리스트로 만든다.

x = "hello, world"
x.split(',')        # ['hello', 'world'] : list type
                      
※ Python에서 list는 배열처럼 사용됨(R과 다름)


- upper() : 원본 문자열을 대문자롤 변환
x.upper()


- lower() : 원본 문자열을 소문자롤 변환
x.lower()


- index() : 원본 문자열 안에 매개변수로 입력한 문자열이 존재하는 위치를 앞에서 부터
            찾는다. 없으면 오류 
            
x.index('o') 
x.index('O')       # ValueError: substring not found


- in 연산자 : 급하게 존재여부만 파악하고 싶을때
'o' in x           # True
'O' in x           # False


"""
[문제5] 
alha = 'aAbBcCdDeEfFgGhHiIjJkK' 변수에 값이 들어 있습니다. 
화면의 결과는  ABCDEFGHIJK 출력하세요.
"""
alha = 'aAbBcCdDeEfFgGhHiIjJkK'
alha = alha.upper()
alha[::2]

alha[1::2]


"""
[문제6] 

a = 'a b c d e f g' 변수에 문자열이 들어 있습니다. 다음을 수행하세요.
"""
a = 'a b c d e f g'

1. a 변수에 있는 문자의 갯수를  구하세요.
len(a)  # 13

2. a 변수에 공백문자 갯수를 구하세요.
a.count(' ')  # 6

3. a 변수 안에 있는 공백문자를 제외한 갯수를 구하세요.
len(a.replace(' ',''))  # 7

4. a 변수에 있는 공백문자를 제거한 후 b 변수에 넣어주세요
b = a.replace(' ','')
b

5. a 변수에 있는 문자를 분리한 후 c 변수에 넣어주세요.
c = a.split(' ')
c

type(c)  # list

※ c는 일반적인 문자변수에서 list형으로 변환됨

# list -> str
c = ','.join(c)
type(c)


x = 'abc'         # 얘를 split 하고 싶다
x = '/'.join(x)   # / 삽입
x












