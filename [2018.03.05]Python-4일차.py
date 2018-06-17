"""
Python-4일차(2018.3.5)
"""

'''
[문제26] 여러 값을 동일한 변수에 순차적으로 저장할수 있는 용도의 변수 타입과 부호는 ?
# list []


[문제27] x 리스트 변수에 1, 3, 5, 7, 9 를 입력하세요
x = [1,3,5,7,9]  


[문제28] x 변수에 타입을 확인하세요.
type(x)


[문제29] x변수에 첫번째값을 확인해주세요
x[0]


[문제30] x변수에 제일뒤에 값을 확인해주세요
x[-1] 


[문제31] x변수에 10를 제일 뒤에 추가해주세요.
x.append(10)
x


[문제32] x변수에 있는 값들중에 10을 삭제해주세요
x.pop()  # x.remove(10)
x 


[문제33] x변수에 1번색인위치에 2를 입력하세요.
x.insert(1,2)
x

[문제34] x변수에 1번색인값을 제거해주세요.
del x[1]  # x.pop(1)
x

[문제35] x 변수에 첫번째 부터  세번째까지 값을 출력해주세요.
x[0:3]  # x[:3]


[문제36] x 변수에 제일뒤에서 두개 값을 출력해주세요.
x[len(x)-2:len(x)]  # x[-2:]


[문제37] x 변수를 y변수에 대입한 후 y변수에 11을 추가한 후 x값도 확인 한 후 분석해주세요.
y = x[:]
y.append(11)
x is y  # False

# 변수를 선언해도 실제값은 메모리에 있음
# (변수에 들어가는 것이 아님, 메모리에 대한 포인터만 가지고 있음)
# id() : 주소값 확인하는 함수
# method만 적용되고 + 는 상관없음


[문제38] x변수를 z변수에 복사하지만 고유한 변수로 생성해주시고 z변수에 13을 추가 해주세요.
z = x[:]
z.append(13)
z is x  # False

import copy
c = copy.deepcopy(x)  # 위와 동일한 기능
id(x)
id(c)

pl/sql package 기능도 동일


[문제39] 
    x = [1,2,3]
    y = [4,5,6]
    y변수에 값을 x 변수에 넣어주세요.
x += y  # x.extend(y)
x


[문제40] x 변수에 1번 인덱스의 값을 제거해주세요.
del x[1]
x
# x.pop(1)


[문제41] x변수에 1번 부터 3번 인덱스를 제거해주세요.
del x[1:4]
x  


[문제42] 중첩리스트를 이용할때 첫번째 항목의 첫번째 항목의 값을 추출해주세요.
ex) 
x  # 중첩리스트
x[0][0]


[문제43] 리스트형과 비슷하지만 요소의 값을 변경 할 수 없는 타입과 부호는 ?
# tuple ()

    
[문제44] 키, 값을 저장하는 데이터 타입과 부호는 ?
# dictionary {}
 
    
[문제45]  아래와 같은 내용을 변수에 입력해주세요. 변수이름은 dict

           이름 : '홍길동'
           나이 : 30
           직업 : '파이썬개발자'
dict = {'이름':'홍길동','나이':30,'직업':'파이썬개발자'}    
dict
       
  
[문제46] dict변수 키를 출력하세요.
dict.keys()  # dict_keys(['이름', '나이', '직업'])


[문제47] dict변수 값을 출력하세요.
dict.values()  # dict_values(['홍길동', 30, '파이썬개발자'])


[문제48] dict변수의 키, 값을 출력해주세요.
dict.items()  # dict_items([('이름', '홍길동'), ('나이', 30), ('직업', '파이썬개발자')])
 

[문제49] dict변수의 이름만 출력해주세요.
dict['이름']  # '홍길동'


[문제50] dict변수의 주소 = '서울' 추가해주세요
dict['주소'] = '서울'
dict

    
[문제51]  dict변수의 나이값을 32 수정하세요.
dict['나이'] = 32
dict
'''

'''
[문제52] 구구단을 만드세요. 

2단에서 9단까지만 입력하세요, [0은 구구단 전부를 출력합니다.]: 
    1단이 들어오면 저문장 다시 출력
'''

while True:
    dan = int(input('2단에서 9단까지만 입력하세요, [0은 구구단 전부를 출력합니다.]:'))

    if dan == 0:
        for i in range(2,10):
            print('\n====%d단====' %(i))
            for j in range(1,10):
                print('%d × %d = %d' %(i,j,i*j))
    elif 2 <= dan <= 9:
        print('\n====%d단====' %(dan))
        for j in range(1,10):
            print('%d × %d = %d' %(dan,j,i*j))
    else:
        print('\n2단에서 9단까지만 입력하세요')
    
    ans = input('\n계속하시겠습니까?(yes or no) : ')
    if ans == 'no':
        break
    elif ans == 'yes':
        continue
    else:
        print('yes or no가 아니라서 종료')
        break

'''
[문제53]lst 변수에 a,b,c,d값이 있습니다. for문을 이용하여 아래화면과 같이 출력하세요.

0번 a값이 있습니다.
1번 b값이 있습니다.
2번 c값이 있습니다.
3번 d값이 있습니다.
'''
lst = ['a','b','c','d']
type(lst)

for i in lst:
    print('%d번 %s값이 있습니다.' %(lst.index(i),i))


# 선생님 풀이
for i in range(len(lst)):
    print('{}번 {}값이 있습니다.' .format(i, lst[i]))

for i, name in enumerate(lst):  # enumerate : index, value 둘 다 return
    print('{}번 {}값이 있습니다.' .format(i,name))


'''
[문제54] 1부터 9까지 x 리스트 변수에 넣어주시고
         y변수는 x 변수의 값을 2곱한 값으로 넣어 주세요.
'''
x = [1,2,3,4,5,6,7,8,9]
x

y = []
for i in range(len(x)):
    y.append(x[i] * 2)
y


# 선생님 풀이
x = range(1,10)
y = []
for i in x:
    y.append(i*2)
y


## 4-1. 리스트 내포(list comprehension), 리스트 내장객체

[표현식 for 항목 in 반복가능한 객체]

x = range(1,10)
y = [i*2 for i in x]
type(y)


'''
[문제55] apple, banana, orange 리스트 변수에 값을 입력하시고
         이 값들의 길이를 출력해주세요.
'''
x = ['apple','banana','orange']
for i in x:
    print(len(i))

[len(i) for i in x]


'''
[문제56] 변수에 값이 들어 있습니다.

lst1 = [1,2,3]
lst2 = [4,5,6]
[4,5,6,8,10,12,12,15,18]
'''
lst1 = [1,2,3]
lst2 = [4,5,6]

[i*j for i in lst1 for j in lst2]  # [4, 5, 6, 8, 10, 12, 12, 15, 18]


# 선생님 풀이
for x in lst1:
    for y in lst2:
        print(x*y, end = ',')

lst3 = []
for x in lst1:
    for y in lst2:
        lst3.append(x*y)
lst3


'''
[문제57]  1부터 100까지 값중에 짝수만 x 변수에 넣어 주세요.
'''
x = [i for i in range(2,101,2)]
type(x)  # list
len(x)   # 50

i = 0
while i < 100:
    i += 2
    x.append(i)
x


# 선생님 풀이
x = [i for i in range(1,101) if i % 2 == 0]
x

[표현식 for 항목변수 in 반복가능한 객체]

[표현식 for 항목변수1 in 반복가능한 객체
        for 항목변수2 in 반복가능한 객체
        ...........
        for 항목변수n in 반복가능한 객체]

[표현식 for 항목변수1 in 반복가능한 객체 if 조건1
        for 항목변수2 in 반복가능한 객체 if 조건2
        ...........
        for 항목변수n in 반복가능한 객체 if 조건n]


'''
[문제58] 튜플변수에 사과, 귤, 오렌지, 배, 포도, 바나나, 자몽, 키위, 
         딸기, 블루베리, 망고를 입력하시고 과일이름중에 세글자 이상인 
         과일 fruit_lst변수에 입력해주세요.
'''

fruit = '사과','귤','오렌지','배','포도','바나나','자몽','키위','딸기','블루베리','망고'
type(fruit)  # tuple

fruit_lst = [i for i in fruit if len(i) >= 3]
fruit_lst


'''
[문제59] dictionary 변수에 값이 들어 있습니다. 과일이름을 대문자로 출력해주세요.
dict = {100:"apple",200:"banana",300:"orange"}
'''
dict = {100:"apple",200:"banana",300:"orange"}

[i.upper() for i in dict.values()]



## 4-2. 함수 
   반복되는 코드를 하나로 묶어서 처리하는 방법
   기능의 프로그램을 작성하기 위해 


def 함수이름(인수,인수,...):
    수행할 문장1
    수행할 문장2
    .....
    [return 값]

함수이름()


def message():
    print("오늘하루도 행복하자")

message()


def message():
    print("오늘하루도 행복하자")
    return "happy"

word = message()
print(word)  # happy


'''
[문제60] 함수에 두 개의 숫자를 인수값으로 받아서 값을 비교하는 프로그램을 
         작성하세요.
'''
def func(x,y):
    if x > y :
        print("%d > %d" %(x,y))
    elif x < y :
        print("%d < %d" %(x,y))
    elif x is y :
        print("%d = %d" %(x,y))
 
func(0,1)       
func(1,1)  
func(1,0)


'''
[문제61] 두 인수값을 받아서 합한 값을 리턴해주는 함수를 작성하세요
'''
def sigma(x,y):
    return x + y

sigma(1,2)    # 3
sigma(-1,2)   # 1
sigma(-2,-1)  # -3



# 인수값이 여러개일 경우 

def 함수이름(*인수):
    수행할 문장
    
def sum(*arg):  # 가변변수 : 인수 여러개 지정
    total = 0
    for i in arg:
        total += i
    return total

sum(10,2,3,4,5)  # 24
sum(10,20,40)  # 70

'''
[문제62] 
cal("sum", 1,2,3,4,5)       # 15
cal("multiply", 1,2,3,4,5)  # 120
'''
def cal(arg1,*arg2):
    if arg1 == "sum":
        total = 0
        for i in arg2:
            total += i
    elif arg1 == "multiply":
        total = 1
        for i in arg2:
            total *= i
    return total


'''
[문제63] 여러 숫자를 인수값으로 받아서 합과 평균을 출력하는
         aggF 함수를 생성하세요.
         aggF(1,2,3,4,5,6,7,8,9,10)
         합 : 55
         평균 : 5.5
'''
def aggF(*arg):
    total = 0
    for i in arg:
        total += i
    print("합 : {}\n평균 : {}" .format(total,total/len(arg)))
    
aggF(1,2,3,4,5,6,7,8,9,10)



def f1(a,b):
    return a + b
    return a - b
x = f1(1,2) 
x   # 3

# return 여러번 사용가능하나 첫번째만 나옴


def f1(a,b):
    return a + b, a - b
x = f1(1,2) 
x   # (3, -1)
type(x)  # tuple

x, y = f1(1,2) 
x  # 3
y  # -1

type(x)
type(y)


def f2(arg):
    if arg == 0:
        return  # 값이 없는 return문은 종료기능
    print(arg,"값입니다")
    
f2(0)
f2(2)


def f3(name, age, gender = "M"):  # gender = "M", defualt 처리
    print("이름은 ", name)
    print("나이는 ", age)
    if gender == "M":
        print("남자")
    else:
        print("여자")

f3("홍길동", 30)
f3("김영미", 20, "F")



def f3(name, gender = "M", age):  # SyntaxError: defualt 처리는 무조건 뒤에  
    print("이름은 ", name)
    print("나이는 ", age)
    if gender == "M":
        print("남자")
    else:
        print("여자")


x = 10  # 전역변수(global), 변수는 프로그램이 종료될 때까지 어디서든 사용

def f4(x):
    print('x변수값은', x)
    x = 20  # 지역변수(local), 함수 안에서만 사용
    print('x변수값은', x)

f4(x)
# x변수값은 10
# x변수값은 20

print(x)
# 10


x = 10  # 전역변수(global), 변수는 프로그램이 종료될 때까지 어디서든 사용

def f4():
    global x   # x 전역변수를 사용하겠습니다.
    x = 20  
    print('x변수값은', x)

f4()  # x변수값은 20
print(x)  # 20


x = 10  # 전역변수(global), 변수는 프로그램이 종료될 때까지 어디서든 사용

def f4(arg):
    global x  # x 전역변수를 사용하겠습니다.
    x = 20  
    print('x변수값은', x)

f4(x)  # x변수값은 20
print(x)  # 20











