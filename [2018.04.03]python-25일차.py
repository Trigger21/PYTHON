"""
python-25일차(2018.4.3)
"""

class Person:
    def __init__(self,name): # 클래스가 인스턴스화 될 때 처음으로 호출하는 매소드
        self.name = name  # name과 self.name 다름 
    
    def say(self):
        print("내 이름은",self.name)


p1 = Person("홍길동")  # Person class의 객체 p1
p1.say()

'''
[문제 187] 생성자에 이름, 핸드폰번호, 메일, 주소 변수를 생성합니다. 
print_info 메소드를 생성한 후  출력하는 Contact 클래스를 생성하세요.
인스턴스는 set_contact 함수를 이용해서 만드시고 이름, 핸드폰번호,메일, 주소는 입력값으로 받아서 출력하세요.

이름을 입력하세요 : 홍길동

핸드폰번호를 입력하세요 : 010-1000-1004

메일을 입력하세요 : hong@aaa.com

주소를 입력하세요 : 서울시 강남구 삼성로

이름 : 홍길동 
핸드폰번호 : 010-1000-1004 
메일 : hong@aaa.com 
주소 : 서울시 강남구 삼성로
'''

class Contact:
    def __init__(self,name,phone,mail,addr):
        self.name = name
        self.phone = phone
        self.mail = mail
        self.addr = addr
    
    def print_info(self):
        print("이름 :",self.name)
        print("핸드폰번호 :",self.phone)
        print("메일 :",self.mail)
        print("주소 :",self.addr)

def set_contact(self):
    self.name = input("이름을 입력하세요 : ")
    self.phone = input("핸드폰번호를 입력하세요 : ")
    self.mail = input("메일을 입력하세요 : ")
    self.addr = input("주소를 입력하세요 : ")
    c = Contact(name, phone, mail, addr)  # 인스턴스화
    c.print_info()  # 출력
    
set_contact()
c = Contact()
c.set_contact()
c.print_info()

b = Contact()
b.name = "test"
b.phone = "010-1234-1234"
b.mail = "dkdkd"
b.addr = "서울"

b.print_info()


'''
[문제188] Contact 클래스 이용해서 입력 들어 온 값들을 c:/data/contact.db 에
	     저장해서 관리하세요.
'''
import sqlite3
conn = sqlite3.connect("/Users/hbk/data/contact.db")
cur = conn.cursor()

cur.execute("create )


# 선생님 풀이
class Contact:
    def __init__(self,name, pn, email, addr):
        self.name = name
        self.pn = pn
        self.email = email
        self.addr = addr

    def print_info(self):
        print("이름 : {} ".format(self.name))
        print("핸드폰번호 : {} ".format(self.pn))
        print("메일 : {} ".format(self.email))
        print("주소 : {} ".format(self.addr))

    def input(self):
        c.execute("insert into contact(name, pn, mail, addr) values(?,?,?,?)",(self.name,self.pn,self.email,self.addr))
        

def set_contact():
    name = input("이름을 입력하세요 : ")
    pn = input("핸드폰번호를 입력하세요 : ")
    email = input("메일을 입력하세요 : ")
    addr = input("주소를 입력하세요 : ")
    conIns = Contact(name, pn, email, addr)  # 인스턴스화
    conIns.print_info()  # 출력
    conIns.input()  # 테이블에 추가



import sqlite3

#conn = sqlite3.connect(':memory:')  
conn = sqlite3.connect('/Users/hbk/data/contact.db')

c = conn.cursor()
#c.execute('drop table contact')
c.execute('create table contact (name text,pn text, mail text,addr text)')
    
set_contact()  # 컬럼별 입력

c.execute('select * from contact')
print(c.fetchall())  # 위 내용 출력

conn.commit()
# conn.rollback()
c.close()
conn.close()



-------------------------------------------------------------------------------

class Person:
    hobbys = []  # 클래스 변수 : 객체간의 값을 공유(주의해서 선언해야 함)
    
    def __init__(self,name): # name : local
        self.name = name  # self.name : global
    
    def add_hobby(self,hobby):
        self.hobbys.append(hobby)


hyo = Person("홍길동")
hyo.add_hobby("부시크래프트")
print(hyo.hobbys)


park = Person("박찬호")
park.add_hobby("글쓰기")
park.add_hobby("사진")
print(park.hobbys)

'''hyo.hobbys = park.hobbys 공유되버림
(공유되진 않고 구분해야 하는건 클래스변수 사용하면 안됨)'''


class Person:
        
    def __init__(self,name): # 초기 생성자
        self.name = name  
        self.hobbys = []  # 인스턴스 변수 : 객체단위로 변경되는 변수
        
    def add_hobby(self,hobby):
        self.hobbys.append(hobby)

hyo = Person("홍길동")
hyo.add_hobby("부시크래프트")
print(hyo.hobbys)


park = Person("박찬호")
park.add_hobby("글쓰기")
park.add_hobby("사진")
print(park.hobbys)

'''hyo.hobbys != park.hobbys 공유안됨'''


class Person:
    country = "한국"  # 클래스 변수
    
    def __init__(self,name):
        self.name = name
    
    def myPrint(self):
        print(self.name + "은 " + self.country + "사람이다.")

p1 = Person("홍길동")
p1.myPrint()

p2 = Person("제임스")
p2.country = '핀란드'
p2.myPrint()

'''클래스 변수라도 자료형에 따라 공유가 안 되는 경우도 있다'''


class Person:
    __country = "한국"  # 클래스 변수(__ : 이름장식)
    
    def __init__(self,name):
        self.name = name
    
    def myPrint(self):
        print(self.name + "은 " + self.__country + "사람이다.")

p1 = Person("홍길동")
p1.myPrint()

p2 = Person("제임스")
p2.__country = '핀란드'
p2.myPrint() # 변경안됨

'''클래스 변수에 이름장식을 하면 추후변경 안됨(마치 상수값처럼 작동)'''


-------------------------------------------------------------------------------


class Test:
    num = 0
    def add(x,y):
        return x + y + num

t1 = Test()
print(t1.add(1,2))  # num 때문에 오류


class Test:
    num = 0
    def add(self,x,y):
        return x + y + self.num

t1 = Test()
print(t1.add(1,2)) 


t2 = Test()
t2.num = 20
t2.add(1,2)  # 23

t1.add(1,2)

t3 = Test()
print(t3.add(1,2))

Test.num = 30  # 이렇게도 가능(주의해야 된다)
print(Test.num)
print(t3.add(1,2))  # 33
print(t1.add(1,2))  # 예도 33?? 하지만 t2는 그대로(주의하자)


Test.add(1,2)  # 정적인 메소드를 써야한다면 어떻게하나?(예는 오류남)


class Test:
    num = 10
    
    @staticmethod  # 정적인 메소드 : 클래스에서 직접 접근해서 객체간의 공유가 된다
    def add(x,y):
        return x + y + Test.num
    
t1 = Test()
print(t1.add(1,2))

Test.add(1,2)

Test.num = 100
Test.add(1,2)  # 103
print(t1.add(1,2))  # 103


t2 = Test()
print(t2.add(1,2))  # 103


t2.num = 3 
t2.add(1,2)  # 103


class iCount:
    iCnt = 0
    
    def __init__(self):
        self.iCnt += 1

    def printCount(self):
        print("인스턴스 갯수 : ",self.iCnt)
        

a,b,c = iCount(),iCount(),iCount()

a.printCount()
b.printCount()
c.printCount()


iCount.printCount()  # 클래스를 통해 메소드 바라보기 안됨(해결하는 방법은 ?)
iCount.iCnt  # 변수는 오류 안남



class iCount:
    iCnt = 0
    
    def __init__(self):
        iCount.iCnt += 1

    def printCount():  # 클래스를 통해 바라보는 메소드
        print("인스턴스 갯수 : ",iCount.iCnt)  
        
iCount.printCount()
a,b,c = iCount(),iCount(),iCount()

a.printCount()
b.printCount()
c.printCount()

'''인스턴스 없이 '''

# 인스턴스 접근가능
class iCount:
    iCnt = 0
    
    def __init__(self):
        iCount.iCnt += 1

    def printCount(self):  # 객체를 통해 바라보는 메소드
        print("인스턴스 갯수 : ",iCount.iCnt)  
        

a,b,c = iCount(),iCount(),iCount()

a.printCount()  # 3
b.printCount()  # 3
c.printCount()  # 3
iCount.printCount()  #   


# 클래스 & 인스턴스 둘다 접근가능
class iCount:
    iCnt = 0
    
    def __init__(self):
        iCount.iCnt += 1
    
    @staticmethod
    def printCount():
        print("인스턴스 갯수 : ",iCount.iCnt)  
        

a,b,c = iCount(),iCount(),iCount()

a.printCount()  # 3
b.printCount()  # 3
c.printCount()  # 3
iCount.printCount()  # 3  


# 클래스로만 접근가능
class iCount:
    iCnt = 0
    
    def __init__(self):
        iCount.iCnt += 1
    
    def printCount():
        print("인스턴스 갯수 : ",iCount.iCnt)  
    
    s_printCount = staticmethod(printCount)  # 정적메소드를 등록

a,b,c = iCount(),iCount(),iCount()

a.printCount()  # error
b.printCount()  # error
c.printCount()  # error
iCount.s_printCount() # 3
iCount.printCount()  # 3


# 클래스 & 인스턴스 둘다 접근가능
class iCount:
    iCnt = 0
    
    def __init__(self):
        iCount.iCnt += 1
    
    def printCount():
        print("인스턴스 갯수 : ",iCount.iCnt)  
    
    def cm_printCount(cls):  # 정적메소드를 만들면서 인스턴스를 통해서도 바라보고 싶다
        print("인스턴스 갯수 : ",cls.iCnt)  
        
    c_printCount = classmethod(cm_printCount)  # 정적메소드를 등록

a,b,c = iCount(),iCount(),iCount()

a.printCount()  # error
a.c_printCount() # error

a.cm_printCount() # 3 
b.cm_printCount() # 3 
c.cm_printCount() # 3 


iCount.c_printCount() # 3
iCount.printCount() # 3

iCount.cm_printCount() # error : 클래스를 통해서는 바라볼 수 없다 'cls' 없음


-------------------------------------------------------------------------------


## 상속 : 메소드 속성을 물려 받는다. 공통된 내용을 하나로 묶어서 관리

class Parents:
    def __init__(self,name,pn):
        self.Name = name
        self.Pn = pn
        
    def PrintInfo(self):
        print("클래스 정보 (이름 : {0}, 전화번호 : {1})" .format(self.Name,self.Pn))
    
    def PersonalData(self):
        print("개인정보 (이름 : {0}, 전화번호 : {1})" .format(self.Name,self.Pn))
        

class Child(Parents):  # 상속의 순간
    def __init__(self,name,pn,address,sn):
        self.Name = name
        self.Pn = pn
        self.Address = address
        self.Sn = sn


p = Parents("홍길동","010-1000-2000")
c = Child("홍아들","010-1234-5678","서울","00000-00000")

p.PrintInfo()
p.PersonalData()

c.PrintInfo()
c.PersonalData()  # 주소, 주민번호는 출력안됨


print(p.__dict__)  # 초기생성자 인자값 확인하려면 이렇게
print(c.__dict__) 


print(Child.__bases__)  # Child 클래스의 부모 확인



class Parents:
    def __init__(self,name,pn):
        self.Name = name
        self.Pn = pn
        
    def PrintInfo(self):
        print("클래스 정보 (이름 : {0}, 전화번호 : {1})" .format(self.Name,self.Pn))
    
    def PersonalData(self):
        print("개인정보 (이름 : {0}, 전화번호 : {1})" .format(self.Name,self.Pn))
        

class Child(Parents):  # 상속의 순간
    def __init__(self,name,pn,address,sn):
        Parents.__init__(self,name,pn)  # 부모의 초기생성자를 상속받는다(__init__ 쓸게여)
        self.Address = address
        self.Sn = sn


p = Parents("홍길동","010-1000-2000")
c = Child("홍아들","010-1234-5678","서울","00000-00000")

p.PrintInfo()
p.PersonalData()

c.PrintInfo()
c.PersonalData()  # 주소, 주민번호는 출력안됨


print(p.__dict__)  # 초기생성자 인자값 확인하려면 이렇게
print(c.__dict__) 


print(Child.__bases__)  # Child 클래스의 부모 확인 (<class '__main__.Parents'>,)

