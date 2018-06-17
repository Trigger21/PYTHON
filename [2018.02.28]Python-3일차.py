"""
Python-3일차(2018.2.28)
"""


# list, tuple, dict 중첩사용 가능

## 3-1. bool 자료형

참(True), 거짓(False)을 나타내는 자료형

x = True
y = False

type(x)  # bool
type(y)  # bool

x == y   # False
x + y    # 1

1 == 1
2 > 1
1 >= 1
1 < 2
1 != 1
1 > 2


not 1   # False
not -1  # False
not 0   # True
not None  # True

-> 0만 False, 나머지는 다 True


# bool() : bool 값 반환하는 함수

bool(1)         # True
bool(-1)        # True
bool('python')  # True
bool([1,2,3])   # True
bool((1,2,3))   # True
bool({1,2})     # True
bool()          # True

bool(0)         # False
bool([])        # False
bool(())        # False
bool({})        # False
bool('')        # False

-> 조건제어문 적용시 참고


## 3-2. 조건제어문, if

 - 들여쓰기 space 4칸
'''
(기본)
if 조건문:
    수행해야할 문장

(옵션)    
if 조건문:
    수행해야할 문장
else:
    수행해야할 문장
'''

ex) x = 11
    
if x == 10:
    print('x는 10입니다.')
    print('행복하자')
else:
    print('x는 10이 아닙니다.')

a = -1
if a:
    print('참')
else:
    print('거짓')

a = []
if a:
    print('참')
else:
    print('거짓')
    
x = 0    
if x > 10 and 1/x:
    print('x는 10보다 크다')
else:
    print('x는 10보다 작다')
    
# 1/0 불능 exception 발생 안하는 이유는 and 앞 절에서 False라서     
    
x = 0    
if x > 10 & 1/x:
    print('x는 10보다 크다')
else:
    print('x는 10보다 작다')    
    
# ZeroDivisionError: division by zero    &로 하면 
    
    
x = 0    
if x < 10 or 1/x:
    print('x는 10보다 크다')
else:
    print('x는 10보다 작다')   
    
# 1/0 불능 exception 발생 안하는 이유는 or 앞 절에서 True라서    


x = 0    
if x < 10 | 1/x:
    print('x는 10보다 크다')
else:
    print('x는 10보다 작다')    

# ZeroDivisionError: division by zero   |로 하면


# input() : 입력값 받고 리턴

num = input('값을 입력해주세요: ')
type(num)  # str(기본값)

num = int(input('값을 입력해주세요: '))
type(num)  # int

num = float(input('값을 입력해주세요: '))
type(num)  # float


# 점수 입력받아서 학점 리턴
score = int(input('점수 입력:'))
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score <70:
    grade = 'D'
else:
    grade = 'F'
print('학점 :'+ grade)

5%2

'''
[문제12] 숫자를 입력값으로 받아서 짝수인지 홀수인지를 출력하는 프로그램을 만드세요.
'''
num = int(input('숫자(정수) 입력: '))
if num % 2:
    print('홀수')
else:
    print('짝수')

'''
[문제13]한글, alphabet만 입력받아야 합니다. 
        만약에 다른 문자가 들어 오면 "한글, alphabet 이외의 문자가 포함되어 있습니다." 
        라는 문구가 출력해야 하고 아니면 입력받은 문자를 출력하세요.
'''
x = input('문자 입력: ')
if x.isalpha():
    print(x)
else:
    print("한글, alphabet 이외의 문자가 포함되어 있습니다.")


'''
[문제14] 숫자를 입력값으로 받습니다. 
         만약 숫자가 이외의 값이 들어 오면 "숫자 이외의 문자가 포함되어 있습니다." 
         아니면 숫자 출력하세요.
'''
x = input('숫자 입력: ')
if x.split('.')[0].isnumeric():
    print(x)
else:
    print("숫자 이외의 문자가 포함되어 있습니다.")


x = [1,2]
y = [2,1]

if x == y:
    print('참')
else:
    print('거짓')


x = (1,2)
y = (2,1)

if x == y:
    print('참')
else:
    print('거짓')


x = {1,2}
y = {2,1}

if x == y:
    print('참')
else:
    print('거짓')


## 3-3. 반복문, while
    반복해서 문장을 수행한다.
'''
while 조건문:
    수행해야할 문장
'''

# 0 ~ 10 까지 출력
i = 0
while i <= 10:
    print(i)
    i += 1


'''
[문제15] 1부터 100까지 합을 구하세요. while문을 이용하세요.
'''
# sol.1
i = 1
s = 0
while i <= 100:
    s += i  
    i += 1
print(s)

# sol.2
i = 0
s = 0
while i < 100:
    i += 1
    s += i
print(s)

# sol.3
n = 100
int(n*(n+1)/2)


'''
[문제16] 1부터 100까지의 3의 배수를 출력, 합을 구하세요. while문을 이용하세요.
'''
# sol.1
i = 1
s = 0
while i <= 100:
    if i % 3:
        exit
    else:
        print(i)
        s += i
    i += 1
print('\n합: %d' %s)

# sol.2
i = 0
while i < 33:
    i += 1
    print(3 * i)
print(int(3*i*(i+1)/2))


# 선생님 풀이
i = 0
res = 0
while i < 100:
    i += 3
    if i > 100:
        break    # loop 탈출
    else:
        print(i)
        res += i
print(res)


'''
[문제17] 1부터 10까지 홀수값만 출력하세요.
'''
# sol.1
i = 1
while i < 10:
    print(i)
    i += 2

# sol.2
i = 1
while i < 10:
    if i % 2:
        print(i)
    i += 1

# sol.3
i = 0
while i < 5:
    print(2*i+1)
    i += 1


# 선생님 풀이
a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue   # 아래 logic 미실행, 다시 while로 올려보내기
    print(a)


'''
[문제18] 단을 입력값으로 받아서 구구단을 출력하세요.
'''
n = int(input('몇 단?: '))
i = 1
print('===%d 단===' %n)
while i < 10:
    print('%d × %d = %d' %(n,i,n*i))
    i += 1

n = int(input('몇 단?: '))
i = 1
print('===%d 단===' %n)
while i < 10:
    print('{단} × {수} = {곱}' .format(단 = n, 수 = i, 곱 = n*i))
    i += 1


'''
[문제19] 구구단을 생성하세요
'''
i = 2
while i < 10:
    print('\n====%d단====' %i)
    j = 1
    while j < 10:
        print('{단} × {수} = {곱}' .format(단 = i, 수 = j, 곱 = i*j))
        j += 1
    i += 1    


print(i,'*',j,'=',i*j)


'''
[문제20] 반복횟수를 입력해서 화면처럼 출력하세요.
'''        

반복횟수를 입력하세요: 5

     ★
    ★★
   ★★★
  ★★★★
 ★★★★★

# sol.1
n = int(input('반복횟수를 입력하세요: '))
i = 0
s = n
while i <= n:
    print('{}{}' .format(' '*s, '★'*i))
    s -= 1
    i += 1

# sol.2
n = int(input('반복횟수를 입력하세요: '))
i = 1
while i <= n:
    print(' '*(n-i) + '★'*i)
    i += 1


# 선생님 풀이
n = int(input('반복횟수를 입력하세요: '))
cnt = 0   
while cnt < n:
    cnt = cnt + 1
    print(' '*(n-cnt) + '★'*cnt)


## for문
'''
for 변수 in (리스트, 튜플, 문자열):
    반복수행해야 할 문장
'''

ex)
x = ['sql','plsql','r','python']    

for i in x:
    print(i)

for i in 'python':
    print(i)
    
    
x = [(1,2),(3,4),(5,6)]

for (a,b) in x:
    print(a+b)
# 3
# 7
# 11


'''
[문제21] 학생들의 점수가 90,55,63,78,80 점이 있습니다.
         60점 이상이면 합격, 60점 미만이면 불합격 출력해 주세요.
'''
score = [90,55,63,78,80]
for i in score:
    if i >= 60:
        print('합격')
    else:
        print('불합격')


# range(시작, 끝-1, 증가분)

range(100)  # 0 ~ 99

list(range(100)) # 출력해서 보고 싶을 때

list(range(1,101))  # 1 ~ 100

list(range(0,101,10))  # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


'''
[문제22] 1부터 100까지 합을 구하세요.(for 이용)
'''
s = 0
for i in range(1,101):
    s += i
print(s)    

# odd
s = 0
for i in range(1,101,2):
    s += i
print(s)

# even
s = 0
for i in range(2,101,2):
    s += i
print(s)


'''
[문제23] 1부터 10까지 출력하세요. 단 4, 8은 제외(for 이용)
'''
for i in range(1,11):
    if i in [4,8]:
        continue
    else:
        print(i)


'''
[문제24] 화면과 같이 출력하세요.(for 이용)

가로의 숫자를 입력하세요 : 5
세로의 숫자를 입력하세요 : 5
★ ★ ★ ★ ★ 
★ ★ ★ ★ ★ 
★ ★ ★ ★ ★ 
★ ★ ★ ★ ★ 
★ ★ ★ ★ ★ 
'''
rowNum = int(input('가로의 숫자를 입력하세요 : '))
colNum = int(input('세로의 숫자를 입력하세요 : '))
for i in range(0,colNum):
    print('★' * rowNum)



'''
[문제25] 구구단을 출력하세요.(for 이용)
'''
for i in range(2,10):
    print('\n==== %d단 ====' %i)
    for j in range(1,10):
        print(i,' × ',j,' = ',i*j)


    
    