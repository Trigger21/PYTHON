"""
Python-6일차(2018.3.7)
"""

# 함수 입력값에 여러개 넣으려고 할 때 list로 한다면 * 빼고 하자(*은 tuple형으로)
from statistics import *
dir()
stdev([1,2,3,4,5])
stddev(1,2,3,4,5)


if __name__ == "__main__":   # 인터프리터에서 작업하는 구문
    print(stddev(1,2,3,4,5))

print(stddev(1,2,3,4,5))
stddev(1,2,3)

# 코드문 확인하는 방법
import inspect
inspect.getsource(stddev)  


'''
[문제69] 프로그램을 생성하세요.

액수입력 : 362
화폐단위를 입력하세요 : 100 50 1
1원 : 12개
50원 : 1개
100원 : 3개
'''
362 = 100x + 50y + 1z
    = 50(2x+y)+1z
-> 2x+y = 7((362-12)/50), z = 12(362%50)
y = 1(7%2), x = 3((7-1)/2)


money = int(input("액수입력 : "))
won = [int(i) for i in input('화폐단위를 입력하세요 : ').split(' ')]
def exchange(money, won):
    won.sort(reverse = True)
    remain = money
    res = {}
    for i in won:
        dvmd = divmod(remain,i)
        res[i] = dvmd[0]
        remain = dvmd[1]
    return res
res = exchange(money,won)
for k,v in res.items():  # items() : key, value
    print('{}원 : {}개' .format(k,v))





362%50
(362-12)/50
62%50
12%1

{10: 1, 50: 1, 100: 3}

100x+50y+10z=360
50(2x+y)+10z=360
10(5(2x+y)+z)=360


gcd(won[0],won[1])


## 6-1. 예외사항 처리

def divide(x,y):
    return x/y
divide(10,2)
divide(10,0)
divide(10,'two') 

try:
    z = divide(10,'two')
    print(z)
except:
    print("오류가 발생했습니다.")

# 각종 except
try:
    z = divide(10,0)
except TypeError:
    print("문자는 안돼~ 숫자로 넣어!!")
except ZeroDivisionError:
    print("0으로 나눌수는 없어!! 빠따맞자")
except:
    print("오류가 발생했네요 쳐맞고 디질래?")
else:     # except 발생 안하면 수행
    print("결과 : {}" .format(z))
finally:  # except 발생 여부에 상관없이 마지막 수행할 것이 있다면 
    print("프로그램 종료")


# raise Exception : 사용자 정의 오류
def func(arg):
    try:
        if arg < 1 or arg > 10:
            raise Exception("유효하지 않은 숫자입니다.: {}" .format(arg))
        else:
            print("입력한 수는 {} 입니다." .format(arg))
    except Exception as error:  # raise Exception -> {} 안으로 쏙!!
        print("오류가 발생했습니다.{}" .format(error))
        
func(9)        
func(11)
        
-32//5
        

x=[1,2,3,4,5]
import numpy as np
x=np.array(x)
x*5   
        
        
'''        
[문제70] 숫자를 입력값으로 받은 후 짝수인지 홀수 인지를 출력한후 그 숫자값을 기준으로
짝수면 짝수형식의 증가값으로 10개 출력, 홀수면 홀수형식의 증가값으로 10개 출력합니다.
만약에 숫자가 들어 오지 않으면 except 처리 하시오

숫자를 입력해주세요 : 10
짝수
10
12
14
16
18
20
22
24
26
28
>>> 

숫자를 입력해주세요 : 11
홀수
11
13
15
17
19
21
23
25
27
29

숫자를 입력해주세요 : 이십
invalid literal for int() with base 10: '이십'
숫자를 입력하세요
'''

def func():
    try:
        n = input("숫자를 입력해주세요 : ")
        m = int(n)
        if m % 2:
            print("홀수")
        else:
            print("짝수")
        [print(i) for i in range(m,m+19,2)]
    except ValueError:
        print("invalid literal for int() with base 10: {}\n숫자를 입력하세요" .format(n))
func()


# 선생님 풀이
try:
    num = int(input("숫자를 입력해주세요 : "))
    if m % 2:
        print("홀수")
    else:
        print("짝수")
    [print(i) for i in range(m,m+19,2)]    
except Exception as error:
    print(error)
    print("숫자를 입력하세요")



## 6-2. 날짜(datetime module)

import datetime
datetime.date.today()  # 오늘 날짜 정보
d = datetime.date.today()  # module.class.function
d

d.year
d.month
d.day

datetime.date(2018,3,7)  # date형 설정
datetime.date(2018,12,5)

type(d)
d1 = d.replace(year = 2019,month = 3,day = 7)  # 년도, 월, 일 변경
d1

dt = datetime.datetime.now()  # 시분초 마이크로세컨드까지 출력
dt

dt.year
dt.month
dt.day
dt.hour
dt.minute
dt.second
dt.microsecond
dt.date()
dt.time()
dt.weekday() # 0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일


'''
[문제71] 오늘이 무슨 요일인지 출력해주세요.
'''
import datetime
dt = datetime.datetime.now()
days = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
print(days[dt.weekday()])


# python도 언어에 종속을 받는다

# date -> str
dt.strftime("%Y %m %d %H %M %S %A %a %B %b %h")

 "%Y  %m %d %H %M %S    %A     %a   %B   %b  %h"
'2018 03 07 15 38 36 Wednesday Wed March Mar Mar'


# str -> date
datetime.datetime.strptime('2018-03-07 15:48:00', '%Y-%m-%d %H:%M:%S')


from datetime import date, time
d = date(2018,3,7)
t = time(15,53,00)

datetime.datetime.combine(d,t)

from datetime import timedelta, date
d = date.today()             # 오늘날짜
td = timedelta(days = 100)   # 100일 추가
td          
d + td                       # 오늘날짜에 100일 이후 날짜
d - td                       # 오늘날짜에 100일 이전 날짜


'''
[문제72] 함수에 인수값으로 현재날짜, 일수 정보를 입력하면 더한 
         날짜정보가 리턴하는 next_day함수를 생성하세요.
'''
from datetime import timedelta, date
def next_day(arg1,arg2):
    return arg1 + timedelta(days = arg2)
print(next_day(date.today(),100))



import datetime
dt1 = datetime.datetime(2018,3,7,16)
dt2 = datetime.datetime(2018,2,7,12)

td = dt1 - dt2   # 일수차이 구하기
td               # datetime.timedelta(28, 14400)
td.days
td.seconds
td.microseconds
td.total_seconds()  # 모든단위를 초단위로 모아서 변환


'''
[문제73] 아래와 같은 결과가 출력될수 있도록 프로그램을 생성하세요


1에서 천만까지 짝수합, 홀수합 구합니다
1에서 천만까지 짝수합: 24999995000000
1에서 천만까지 홀수합: 25000000000000
처리시간 : 0:00:01.950003
처리시간 millisecond(1/1000)  : 1950ms
'''
print("1에서 천만까지 짝수합, 홀수합 구합니다")


5000000*5000001  # even
5000000*5000000  # odd

10000002*2500000  # even
10000000*2500000  # odd

from datetime import datetime
a = datetime.now()
print("1에서 천만까지 짝수합, 홀수합 구합니다")
print("1에서 천만까지 짝수합: %d" %(5000000*5000001))  # even
print("1에서 천만까지 홀수합: %d" %(5000000*5000000))  # odd
b = datetime.now()
print("처리시간 : ",b-a)
delta_ms = int((b-a).total_seconds() * 1000)
print("처리시간 millisecond(1/1000)  : %dms"%delta_ms)


# 선생님 풀이
from datetime import datetime
start = datetime.now()
print('1에서 천만까지 짝수합, 홀수합 구합니다')
even_result = 0
odd_result = 0
for i in range(1,10000001):
    if i % 2 == 0:
        even_result += i
    else:
        odd_result += i
print('1에서 천만까지 짝수합: %d'%even_result)
print('1에서 천만까지 홀수합: %d'%odd_result)
end = datetime.now()
delta = end - start
print("처리시간 : ",delta)
delta_ms = int(delta.total_seconds() * 1000)
print("처리시간 millisecond(1/1000)  : %dms"%delta_ms)











