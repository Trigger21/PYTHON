"""
python-26일차(2018.4.4)
"""

'''
[문제189]초기 생성자에는 이름, 주소, 급여를 입력값으로 받고, 아래와 같이 출력되는 클래스를 생성하세요. 
        인스턴스 생성될때 마다 건수를 출력해주세요.

사원수 : 1
이름 : 홍길동 , 주소 : 덴마크,  급여 : 1000

사원수 : 2
이름 : 홍아들 , 주소 : 노르웨이,  급여 : 2000
'''

클래스 변수 : 인스터스 간 값 공유
정적 메소드 / self 대신 cls

# sol.1
class Emp:
    cnt = 1
    
    def __init__(self,name,addr,sal):
        self.name = name
        self.addr = addr
        self.sal = sal
    
    def printCnt():
        print('\n사원수 :',Emp.cnt)
        Emp.cnt += 1
    
    def printEmp(self):
        print('이름 : '+self.name+' , '+'주소 : '+self.addr+' , '+'급여 : '+self.sal)

def InputEmp():
    name = input("이름 입력 : ")
    addr = input("주소 입력 : ")
    sal = input("급여 입력 : ")
    Emp.printCnt()
    e = Emp(name,addr,sal)
    e.printEmp()
    
InputEmp()


# sol.2
class Emp:
    cnt = 1
    
    def __init__(self,name,addr,sal):
        self.name = name
        self.addr = addr
        self.sal = sal
        Emp.cnt += 1
        
    def printCnt():
        print('\n사원수 :',Emp.cnt)  # 인스턴스 수
            
    def printEmp(self):
        print('이름 : '+self.name+' , '+'주소 : '+self.addr+' , '+'급여 : '+self.sal)

def InputEmp():  # 입력값 받은다음 위 클래스 활용하는 함수
    name = input("이름 입력 : ")
    addr = input("주소 입력 : ")
    sal = input("급여 입력 : ")
    Emp.printCnt()
    e = Emp(name,addr,sal)
    e.printEmp()
    
InputEmp()


# 선생님 풀이
class Employee:
   
   empCn = 0

   def __init__(self, name, addr, salary):
      self.name = name
      self.addr = addr
      self.salary = salary
      Employee.empCn += 1
   
   def printCount(self):
     print("사원수 : %d" %Employee.empCn)

   def printEmployee(self):
      print( "이름 : {} , 주소 : {},  급여 : {}".format(self.name, self.addr, self.salary))


emp1 = Employee("홍길동","덴마크", 1000)
emp1.printCount()
emp1.printEmployee()


emp2 = Employee("홍아들","노르웨이", 2000)
emp2.printCount()
emp2.printEmployee()


'''
[문제190] Person 클래스를 생성하세요. 생성자는 이름, 나이, 성별을 만드세요.
Person 클래스 에는 printMe 메소드를 생성하셔서 이름, 나이 성별을 출력합니다.


Employees클래스를 생성한후 Person상속받습니다.
생성자는 이름, 나이, 성별, 주소, 생일입니다.
단 이름, 나이, 성별은 person에서 상속받으세요.
Employees 클래스에 printMe를 재구성하셔서 주소, 생일을 출력하세요.


myPerson = Person("홍길동","10", "남")
myPerson.printMe()

myEmployee = Employee("송준기", "2", "남", "서울", "2016년 01월 01일")
myEmployee.printMe()



이름은 홍길동 ,  나이는 10살 이고, 성별은 남 입니다.
이름은 송준기 ,  나이는 2살 이고, 성별은 남 입니다.
집 주소는  서울  생일은  2016년 01월 01일 입니다. 
'''
부모 : Person
자식 : Employee

class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def printMe(self):
        print('이름은 {name}, 나이는 {age}살이고, 성별은 {sex}입니다.' .format(name=self.name,age=self.age,sex=self.sex))
    
    
class Employee(Person):
    def __init__(self,name,age,sex,addr,birth):
        Person.__init__(self,name,age,sex)
        self.addr = addr
        self.birth = birth
    
    def printMe(self):
        Person.printMe(self)  # 부모의 메소드도 상속
        print('집 주소는 %s 생일은 %s 입니다.' %(self.addr,self.birth))


myPerson = Person("홍길동","10", "남")
myPerson.printMe()

myEmployee = Employee("송준기", "2", "남", "서울", "2016년 01월 01일")
myEmployee.printMe()


# 선생님 풀이
class Person:

    def __init__(self, name, age, gender):
        self.Name = name
        self.Age = age
        self.Gender = gender

    def printMe(self):
        print("이름은 "+self.Name+",  나이는 "+self.Age+ "살, 성별은 "+self.Gender+"자 입니다.")

         

class Employee(Person):

    def __init__(self, name, age, gender, addr, birthday):
        Person.__init__(self, name, age, gender) # 상속
        self.Addr = addr
        self.Birthday = birthday

    def printMe(self):
        Person.printMe(self) # 상속
        print("집 주소는  "+self.Addr+"  생일은  "+self.Birthday+" 입니다.")

 
myPerson = Person("홍길동","10", "남")
myPerson.printMe()

myEmployee = Employee("송준기", "2", "남", "서울", "2016년 01월 01일")
myEmployee.printMe()


'''
[문제191] Add 클래스에 두수를 더하는 값을 리턴하는 add 메소드 생성
        Multiply 클래스에 두수를 곱한값을 리턴하는 multiply 메소드 생성
        Divide 클래스에 두수를 나눈값을 리턴하는 divide메소드 생성
        Calculator클래스에는 Add, Multiply, Divide 상속받고 두수를 뺀값을 리턴하는 sub 메소드 생성하세요.
'''
class Add:    
    def add(self,num1,num2):
        return num1 + num2

class Multiply:
    def multiply(self,num1,num2):
        return num1 * num2

class Divide:  # 분모에 0이 오는 경우를 대비해서 예외처리 하였음
    def divide(self,num1,num2):
        try:
            if num2 != 0:
                return num1/num2
            else:
                raise Exception
        except Exception:
            print('0으로 나눌 수는 없습니다. 다른 숫자를 입력해 주십시오')

    
class Calculator(Add,Multiply,Divide):
    def sub(self,num1,num2):
        return num1 - num2

c = Calculator()
c.add(1,2)
c.multiply(1,2)
c.divide(6,3)
c.sub(6,4)


# 선생님 풀이
class Add:
    def add(self, x, y):
        return x + y
class Multiply:
    def multiply(self, x, y):
        return x * y
class Divide:
    def divide(self, x, y):
        return x/y
    
class Calculator(Add,Multiply,Divide):
    def sub(self, x, y):
        return x - y

cal = Calculator()
print(cal.add(10,20))
print(cal.multiply(10,20))
print(cal.divide(10,2))
print(cal.sub(10,8))



# 저장하기(클래스 이름과 동일하게) - Calculator.py : 모듈식 - python Calculator.py(terminal)
class Add:
    def add(self, x, y):
        return x + y
class Multiply:
    def multiply(self, x, y):
        return x * y
class Divide:
    def divide(self, x, y):
        return x/y
    
class Calculator(Add,Multiply,Divide):
    def sub(self, x, y):
        return x - y

if __name__ == "__main__": # script 할때만 import는 안 돌아감(코드 이상유무 테스트용)
    cal = Calculator()
    print(cal.add(10,20))
    print(cal.multiply(10,20))
    print(cal.divide(10,2))
    print(cal.sub(10,8))


'''곽상욱 형 면접
- 통계전공 원한다
- R로 문제 풀어라
- 토토 승율 
- 파이썬 질문 : 파이썬이 어떤 것이라고 생각하나?(태효 왈 : "컴퓨터와 하는 펜팔")
- 통계 수학 질문 많이 받음
- 타 통계프로그램도 할 수있나?'''

'''선생님 말씀
- 실력 & 사람됨 중요'''


import Calculator  # 파이썬에게 해당파일의 경로를 알려주지 않으면 오류남
dir(Calculator)  # 모듈 내부 클래스 보임


import sys
sys.path # 파이썬이 인지하고 있는 경로(list로 나옴)
sys.path.append('/Users/hbk/data/')  # 경로만 새로 추가


from Calculator import *  # Cal모듈 안 모든 것을 import
dir(Calculator)  # 모듈안 메소드 다보임 (단, __ 얘내들은 파이썬 내재된 것)

cal = Calculator()
cal.add(2,4)
cal.multiply(2,3)
cal.sub(2,4)

#import numpy
#len(dir(numpy))


'''
[문제192] 한주간 걸음걸이 그래프 그리기
step = []
labels = ['월','화','수','목','금','토','일']
create_bar_chart(step,lables,2)
'''

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc #한글설정 1
rc('font', family='AppleGothic') #한글설정 2
plt.rcParams['axes.unicode_minus'] = False #한글설정 3

import pandas as pd
from pandas import Series, DataFrame


def create_bar_chart(step,labels,num):
    data = DataFrame(step,labels)
    if num == 1:
        bar = data.plot(kind = 'bar', grid = True)
    elif num == 2:
        bar = data.plot(kind = 'barh',grid = True)
    elif num == 3:
        data1 = data.sort_values(0,ascending = True)
        bar = data1.plot(kind = 'barh',grid = True)
    return bar

step = [3854,7014,5526,7779,6725,36,11480]
labels = ['월','화','수','목','금','토','일']

create_bar_chart(step,labels,1)
create_bar_chart(step,labels,2)
create_bar_chart(step,labels,3)


data1 = data.sort_values(0, ascending = True)
data1.plot(kind = 'barh', grid = True)

print(plt.style.available)



# 선생님 풀이
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
#font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
#rc('font', family=font_name)
rc('font', family='AppleGothic') 
plt.rcParams['axes.unicode_minus'] = False 


def create_bar_chart(data,labels,bar):

    num_bars = len(data)
    positions = range(1, num_bars+1)
    
    if bar == 1:        
        plt.bar(positions, data, align='center')  # 세로 막대
        plt.xticks(positions, labels)
        plt.xlabel('요일')
        plt.ylabel('걸음수')
       
    else:
         plt.barh(positions, data, align='center')  # 가로 막대
         plt.yticks(positions, labels)
         plt.xlabel('걸음수')
         plt.ylabel('요일')
    

    plt.title('한주간 동안 걸음수') 
    plt.grid()
    plt.show()
    
if __name__=='__main__':
    step = [1090,2000,3000,4000,10000,50000,2000]
    labels = ['월','화','수','목','금','토','일']
    create_bar_chart(step,labels,2)


'''
[문제193] 위 문제를 클래스화 -> 모듈화
'''

class walkGragh:
    
    def create_bar_chart(self,data,labels,bar):

        num_bars = len(data)
        positions = range(1, num_bars+1)
        
        if bar == 1:        
            plt.bar(positions, data, align='center')
            plt.xticks(positions, labels)
            plt.xlabel('요일')
            plt.ylabel('걸음수')
            
        else:
            plt.barh(positions, data, align='center')
            plt.yticks(positions, labels)
            plt.xlabel('걸음수')
            plt.ylabel('요일')
        plt.title('한주간 동안 걸음수') 
        plt.grid()
        plt.show()

w = walkGragh()
w.create_bar_chart(step,labels,2)

if __name__=='__main__':
    step = [1090,2000,3000,4000,10000,50000,2000]
    labels = ['월','화','수','목','금','토','일']
    create_bar_chart(step,labels,2)
    
    

plt.grid()
plt.barh(range(1,6), range(1,6))


'''import 실습'''
import sys
sys.path  # /Users/hbk/data/ 존재여부 확인(스파이더 재부팅시 사라짐)
sys.path.append('/Users/hbk/data/')

from walkGragh import walkGragh
w = walkGragh()
w.create_bar_chart(step,labels,2)

from walkGragh import *
w = walkGragh()
w.create_bar_chart(step,labels,2)


# 선생님 풀이
import matplotlib.pylab as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

class create_bar_chart:
    def __init__(self,data, labels, bar):
        self.data = data
        self.labels = labels
        self.bar = bar
        
    def create_bar_chart(self):
    
        num_bars = len(self.data)
    
        positions = range(1, num_bars+1)
        if self.bar == 1:
            plt.bar(positions, self.data, align='center')
            plt.xticks(positions, self.labels)
            plt.xlabel('요일')
            plt.ylabel('걸음수')
           
        else:
            plt.barh(positions, self.data, align='center')
            plt.yticks(positions, self.labels)
            plt.xlabel('걸음수')
            plt.ylabel('요일')
        
    
        plt.title('한주간 동안 걸음수') 
        plt.grid()
        plt.show()
    
if __name__=='__main__':
    step = [5000,6000,7500,10000,10000,20000,2000]
    labels = ['월','화','수','목','금','토','일']
    cbc = create_bar_chart(step,labels,2)
    cbc.create_bar_chart()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''혹시나 영문 이외의 다국문자를 수행할 시 utf-8 오류가 나면 이걸 제일 위에 주석으로 넣어라'''




