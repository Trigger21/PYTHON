"""
Python-5일차(2018.3.6)
"""

'''
[문제64] 입력값을 더하는 함수를 작성하세요.

>>> print(add(2))
2

>>> print(add(8))
10
'''
total = 0
def add(x):
    global total
    total += x
    return total
print(add(2))  # 2
print(add(8))  # 10

dir()
del total


# 선생님 추가설명

total = 0
def add(arg):
    total = arg
    return total

print(add(2))  # 2
print(total)   # 0


total = [0]
def add(arg):
    total[0] = arg
    return total[0]

print(add(2))
print(total)  # list변수는 global로 작동되므로 주의해야 한다


'''
[문제65] 아래와 같이 변수에 값이 들어 있습니다. 
exchang함수에 x변수에 값을 넣으면 y로 변환하는 함수를 만드세요.

x = ["귀도","반","로섬"]
y = ["Guido","van", "Rossum"]
'''

x = ["귀도","반","로섬"]
y = ["Guido","van", "Rossum"]

def exchang(arg):
    arg = arg[:]  # copy 하지 않으면 x = ['Guido', 'van', 'Rossum']로 됨
    for i in range(len(arg)):
        arg[i] = y[i]
    print(arg)

exchang(x)
print(x)   
print(y)


'''
[문제66]약수를 구하는 divisor 함수를 생성하세요.

1이상의 숫자를 입력하세요: 100
[100, 50, 25, 20, 10, 5, 4, 2, 1]
'''
def divisor(num):
    x = []
    for i in range(1,num+1):
        if num % i == 0:
            x.append(i)
    x.sort(reverse = True)
    return x
num = int(input("1이상의 숫자를 입력하세요: "))
divisor(num)


def divisor(num):
    x = [num]
    n = int(num/2)
    for i in range(n,0,-1):
        if num % i == 0:
            x.append(i)
    return x

divisor(num)


# 선생님 풀이
num = int(input("1이상의 숫자를 입력하세요: "))
def divisor(num):
    num1 = int(num/2)
    num2 = []
    num2.append(num)
    while num1 >= 1:
        if num % num1 == 0:
            num2.append(num1)
        num1 -= 1
    return(sorted(num2))
    # return(sorted(num2, reverse = False))
print(divisor(num))


# 재귀호출 = 자기 자신을 다시 호출한다.
#          = 반복문 + stack(스택)

def cn(n):
    if n <= 0:
        print("종료")
    else:
        print(n)
        cn(n-1)
cn(5)
    
    
'''
[문제67] 펙토리얼 
'''
num = int(input("숫자를 입력하시오 : "))
def factorial(n):
    res = 1
    if n >= 0: 
        for i in range(1,n+1):
            res *= i
    else:
        print("양의 부호만 입력하시오")
        return
    return res
factorial(num)


num = int(input("숫자를 입력하시오 : "))
def factorial(n):
    if n == 0:
        return(1)
    elif n < 0:
        print("양의 부호만 입력하시오")
        return
    else:
        return(n*factorial(n-1))
factorial(num)


import math
math.factorial(9)


from math import gamma
a = -1
gamma(a+1)


# 선생님 풀이
def factorial(arg):
    if arg in [0,1]:
        return 1
    return factorial(arg-1) * arg

factorial(0)


# 유클리드 호제법(최대공약수)

def gcd(m,n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)
gcd(45,30)


def gcd(m,n):
    while n != 0:
       t = m % n
       (m,n) = (n,t)
    return abs(m)
gcd(166,196)


def gcd(m,n):
    while n != 0:
        if m < n:
            m, n = n, m
        if n == 0:
            return m
        if m % n == 0:
		       return n
gcd(30,45)


# 선생님 풀이
def gcdFn(x,y):
    if y == 0:
        return x
    return gcdFn(x, y%x)
gcd(30,45)



'''
[문제68] stddev(2,3,1,7) 표준편차를 구하세요. stddev함수를 생성하세요.
'''
편차 = 관측값 - 평균
편차 제곱의 합 = ∑(편차**2)
분산 = 편차제곱합 / 데이터수(자유도)
표준편차 = math.sqrt(분산)
평균 = ∑ 관측값 / 데이터수

sum(인수)
len(인수)

import math
def stddev(*arg):
    def var(arg):
        def avg(arg):
            return sum(arg)/len(arg)
        avg = avg(arg)
        d = 0
        for i in arg:
            d += (i - avg)**2
        return d/(len(arg)-1)
    return math.sqrt(var(arg))

stddev(2,3,1,7)


# 선생님 풀이
def stddev(*arg):
    def mean():
        return sum(arg)/len(arg)
    def var(m):
        total = 0
        for i in arg:
            total += (i-m)**2
        return total/(len(arg)-1)
    v = var(mean())                # 호출
    return math.sqrt(v)

round(stddev(2,3,1,7), 5)          # trunc 제공 안함


# 작성한 함수를 모듈형식으로 저장해서 호출해서 사용하기

import sys  # system 본다
sys.path.append('C:\\python')     # path에 내가 만든 경로 추가
sys.path

# stddev.py  (module 이름은 py 파일 이름명)
import stddev 
stddev.stddev(2,3,1,7)  # 모듈이름.함수이름

from stddev import *    # 함수 전부다는 * 특정함수는 작성
round(stddev(2,3,1,7), 6)


dir()  # 내가 만든 것들 조회

더 편하게 하려면 환경변수에서 잡아주면됨
PYTHONPATH  C:\python


# 숙제
평균함수 만들어라
분산함수 만들어라

stats 모듈을 만들어라 (즉, stats.py 안에 함수 다 넣어버리자)

import sys
sys.path

from stats import mean,var,stddev
mean(1,2,3,4)
var(1,2,3,4)
stddev(1,2,3,4)
dir()
