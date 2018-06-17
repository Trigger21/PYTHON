"""
Python-18일차(2018.3.23)
"""

## 18-1. sqlite
  별도의 DB 서버가 필요없이 DB파일에 기초하여 데이터베이스 처리하는 엔진이다
  메모리 DB로 tablespace 개념 없음(오라클만 있다)
  
import sqlite3  # 내장된 sqlite 모듈

conn = sqlite3.connect(":memory:")  # 메모리에서 생성할 때
conn = sqlite3.connect("c:/python/insa.db")  # 파일로 저장할 때
c = conn.cursor()  # sql문 실행메모리 영역(작업하는 곳)

'''sql : db-tablespace-table-block
         extend : block 집합
         table : extend 집합'''

c.execute("create table emp(id integer, name text, sal integer)")  # table 생성

c.execute("insert into emp(id,name,sal) values(1,'홍길동',1000)")  # insert 1

c.execute("select * from emp")  # cursor에서 찾아옴
c.fetchone()  # (1, '홍길동', 1000)

c.execute("insert into emp(id,name,sal) values(2,'박찬호',2000)")  # insert 2

c.execute("select * from emp")
c.fetchone()  # 한 행씩 나옴

c.execute("select * from emp")
c.fetchall()  # 다 나옴

conn.rollback()  # 주의!! conn.
conn.commit()  # 주의!! conn.

c.execute("insert into emp(id,name,sal) values(?,?,?)", (3,'나얼',3000))  # insert 3

insert_sql = "insert into emp(id,name,sal) values(?,?,?)"  # insert 4
c.execute(insert_sql,(4,'윤건',5000))

c.execute("select * from emp")
c.fetchall()

conn.commit()

c.close()
conn.close()  # 위에꺼 다 날라감(메모리는)



import sqlite3  
conn = sqlite3.connect("c:/python/insa.db")  # 파일로 저장할 때
c = conn.cursor()  # sql문 실행

c.execute("select name from sqlite_master where type = 'table'")  # table 찾기
c.fetchall()

c.execute("PRAGMA table_info(emp)")  # emp table 구조확인 방법
c.fetchall()

c.execute("select * from emp")
c.fetchall()

c.execute("select * from emp")
c.fetchmany(2)  # 출력할 갯수 지정가능

c.execute("update emp set sal = 6000 where id = 1")  # update
c.execute("select * from emp where id = 1")
c.fetchall()

conn.rollback()
# conn.commit()


c.execute("delete from emp where id = 2")
c.execute("select * from emp")
c.fetchall()

conn.rollback()


c.execute("alter table emp add column deptno integer")  # column 추가
c.execute("PRAGMA table_info(emp)")
c.fetchall()

c.execute("select * from emp")
c.fetchall()

c.execute("update emp set deptno = 10 where id = 1")
c.execute("update emp set deptno = 20 where id = 2")
c.execute("update emp set deptno = 30 where id = 3")
c.execute("update emp set deptno = 40 where id = 4")

conn.commit()

c.execute("select * from emp")
c.fetchall()

c.execute("drop table emp")  # table 삭제
c.fetchall()


c.execute("create table emp(id integer, name text, sal integer, deptno integer)")
c.execute("insert into emp values(1,'홍길동',1000,10)")
c.execute("insert into emp values(2,'박찬호',2000,20)")
c.execute("insert into emp values(3,'나얼',3000,30)")
c.execute("insert into emp values(4,'윤건',4000,40)")
c.execute("select * from emp")
c.fetchall()
conn.commit()

c.execute("create table dept(deptno integer, dname text)")
c.execute("insert into dept(deptno,dname) values(10,'총무부')")
c.execute("insert into dept(deptno,dname) values(20,'영업1')")
c.execute("insert into dept(deptno,dname) values(30,'영업2')")
c.execute("insert into dept(deptno,dname) values(40,'분석팀')")
conn.commit()

c.execute("select * from dept")
c.fetchall()

c.execute("PRAGMA table_info(emp)")
c.execute("PRAGMA table_info(dept)")
c.fetchall()

c.execute("insert into emp(id,name,sal,deptno) values(5,'김건모',9000,null)")
conn.commit()


# inner join
c.execute("""select emp.id,emp.name,emp.deptno,dept.dname 
             from emp inner join dept 
             on emp.deptno = dept.deptno""")
c.fetchall()


# left join
c.execute("""select emp.id,emp.name,emp.deptno,dept.dname 
             from emp left outer join dept 
             on emp.deptno = dept.deptno""")
c.fetchall()

# sqlite에서는 right outer join, full outer join 없음


c.execute("insert into dept(deptno,dname) values(50,'인사팀')")
conn.commit()

c.execute("""select emp.id, emp.name, emp.sal, emp.deptno, dept.dname
             from emp left outer join dept
             on emp.deptno = dept.deptno
             union
             select emp.id, emp.name, emp.sal, dept.deptno, dept.dname
             from dept left outer join emp
             on emp.deptno = dept.deptno""")

c.fetchall()


http://www.sqlitetutorial.net/  # sqlite 사용법
https://sqlitestudio.pl/index.rvt  # sqlitestudio 다운


import sqlite3
conn = sqlite3.connect("c:/python/phonebook.db")
c = conn.cursor()

c.execute("create table phonebook(name txt, pn txt)")
c.execute("""insert into phonebook(name,pn)
             values('홍길동','010-1234-5678')""")
c.execute("select * from phonebook")
c.fetchall()

name = '박찬호'
pn = '010-1000-2000'
c.execute("insert into phonebook(name,pn) values(?,?)",(name,pn))

name = '나얼'
pn = '010-2000-3000'
c.execute("insert into phonebook(name,pn) values(:a,:b),{'a':name,'b':pn})

conn.commit()
c.execute("select * from phonebook")
c.fetchall()

c.execute("insert into phonebook(name,pn) values('김태효','010-6802-3828')")
c.execute("select * from phonebook")
c.fetchall()


# Gernerator로 data를 반환하는 함수
def dataGenerator():
    datalist = {('윤건','010-7777-8888'),
                ('김건모','010-9999-0000')}
    for i in datalist:
        yield i  # return 대신 

dataGenerator()

c.executemany("insert into phonebook(name,pn) values(?,?)", dataGenerator())  # 여러개 한번에 처리하려면
c.execute("select * from phonebook")
c.fetchall()
conn.commit()


# literable : 리스트에 있는 값들을 순환하며 하나씩 꺼내서 사용한다.
lst = [1,2,3]
for i in lst:
    print(i)


lst = [x*x for x in range(5)]
for i in lst:
    print(i)
    
''' 리스트 변수를 가지고 순환할 때 계속 메모리에 값을 가지고 있다. 즉, 크기가 크면
    부하가 발생할 가능성이 높아진다.'''    


# generator : 리스트에 있는 값들을 순환하며 하나씩 꺼내서 사용한다.
#             0을 계산해서 반환한 후 0에 대해서는 가지고 있지 않고 1을 계산한다.
lst = (x*x for x in range(5))
for i in lst:
    print(i)
    
type(lst)  
    
''' 순환을 하고 수행하면 버린다.(가지고 있지 않음) 많은 데이터 사용시 메모리 부하 방지
    다른언어에도 이런 기능이 있다.'''


def dataGenerator():
    lst = range(5)
    for i in lst:
        yield i*i  # yield로 인해 generator가 된다 
    
y = dataGenerator()
print(y)    

for i in y:
    print(i)    
    
    
## 18-2. generator 왜 사용하나? (번외연구)
    
[1] 메모리를 효율적으로 사용한다

'''메모리 사용상태 확인'''
import sys

sys.getsizeof( [i for i in range(100) if i % 2] )  # 528
sys.getsizeof( [i for i in range(1000) if i % 2] )  # 4272

sys.getsizeof( (i for i in range(100) if i % 2) )  # 88
sys.getsizeof( (i for i in range(1000) if i % 2) )  # 88

'''
list 의 경우 사이즈가 커질 수록 그만큼 메모리 사용량이 늘어나게 된다. 
하지만, generator 의 경우는 사이즈가 커진다 해도 차지하는 메모리 사이즈는 동일하다. 
이는 list 와 generator의 동작 방식의 차이에 기인한다.

list 는 list 안에 속한 모든 데이터를 메모리에 적재하기 때문에 list의 크기 만큼 
차지하는 메모리 사이즈가 늘어나게 된다. 하지만 generator 의 경우 데이터 값을 한꺼번에 
메모리에 적재 하는 것이 아니라 next() 메소드를 통해 차례로 값에 접근할 때마다 
메모리에 적재하는 방식이다. 

따라서 list 의 규모가 큰 값을 다룰 수록 generator의 효율성은 더욱 높아지게 된다. 
'''

[2] 계산 결과값이 필요할 때까지 계산을 늦추는 효과(Lazy evaluation)

# 1초간 sleep, x를 반환하는 함수
def sleep_func(x):
    import time
    print("sleep...")
    time.sleep(1)
    return x

# list 생성
lst = [sleep_func(x) for x in range(5)]
for i in lst:
    print(i)

# generator 생성
gen = (sleep_func(x) for x in range(5))
for i in gen:
    print(i)

'''
list 의 경우 list comprehension 을 수행 할때, list의 모든 값을 먼저 수행하기 때문에 
sleep_func() 함수를 range() 값 만큼 한번에 수행하게 된다. 만약 sleep_func() 에서 
수행하는 시간이 길거나 list 값이 매우 큰 경우 처음 수행 할때 그만큼 부담으로 작용된다. 

하지만 generator 의 경우 generator 를 생성할 때는 실제 값을 로딩하지 않고, 
for 문이 수행 될때 하나씩 sleep_func()을 수행하며 값을 불러오게 된다. 
수행 시간이 긴 연산을 필요한 순간까지 늦출 수 있다는 점이 특징이다.

이러한 특징을 이용하면, fibonacci 수열과 같은 작업을 간결한 문법과 더불어 
매우 효율적으로 코드를 작성할 수 있다.
'''

def fibonacci_func(n):
    a, b = 1, 1
    i = 1
    while True:
        if i > n:  # n : 범위
            return  # n항 이상이면 종료
        yield a
        a, b = b, a+b  # definition of fibonacci sequence
        i += 1

fib = fibonacci_func(10)
for x in fib:
    print(x)


# yield example
    
def gen():
    yield 'one'
    yield 'two'
    yield 'three'

g = gen()
print(next(g))  # one
print(next(g))  # two
print(next(g))  # three
print(next(g))  # raise StopIteration


def gen():
    val = 111111
    while True:
        val = (yield val) * 111111

g = gen()
print(next(g))  # 111111
print(g.send(2))  # 222222
print(g.send(3))  # 333333
print(g.send(4))
    