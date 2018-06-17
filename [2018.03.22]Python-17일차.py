"""
Python-17일차(2018.3.22)
"""

## 17-1. 그래프

import numpy as np
import pandas as pd
import matplotlib as mpl  # 그래프
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc  # 한글패치
font_name = font_manager.FontProperties(fname = 'c:/Windows/Fonts/malgun.ttf').get_name()  # 한글패치
rc('font',family = font_name)  # 한글패치
%matplotlib inline  # .show() 이용 안해도 plot만으로 바로 출력될 수 있도록


plt.plot([1,2,3,4,5,6,7,8,9,4,5,4,6,5,7,5,7,6,9])

x = np.arange(0,23,0.01)  # 0 ~ 23까지 0.01 간격으로 데이터를 생성
y = np.sin(x)

plt.figure(figsize = (10,5))  # 그래프의 크기(가로, 세로)
plt.plot(x,y)
#plt.show()

plt.grid()  # 마방진처럼 선 그어짐
plt.plot(x,y)
plt.xlabel('시간')  # x축 시간
plt.ylabel('진폭')  # y축 진폭
plt.title('sinewave')
plt.show()


plt.figure(figsize = (10,8))
plt.plot(x,np.sin(x), label = 'sin')  # label = '범례'
plt.plot(x,np.cos(x), label = 'cos')
plt.legend()
plt.grid()
plt.xlabel('시간')  # x축 이름
plt.ylabel('진폭')  # y축 이름
plt.title('sinewave')  # 그래프 이름
plt.show()


x = [1,2,3,4,5,6,7,8,9]
plt.grid()
plt.plot(x, color = "red", linestyle = "dashed", marker = "o",
         markerfacecolor = "yellow", markersize = 5)  # 직선


x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([9,8,7,9,8,3,2,4,3,4])
plt.figure(figsize = (10,8))
plt.scatter(x,y, marker = '>')  # 산점도


colormap = x
plt.scatter(x,y,s=50,c=colormap,marker='>')
plt.colorbar()  # 우측에 x축에 따른 색깔변화를 보여줌


from pandas import DataFrame
data = {"홍길동":[15,13,11], "윤건":[13,14,15], "나얼":[10,9,12]}  # 100m 달리기 시간
df = DataFrame(data, index = [2015,2016,2017])
df.rank()

ad = df.rank()
plt.plot(ad)


plt.plot(ad.ix[:,0], label = '나얼', linestyle = "-.", color = "r")
plt.plot(ad.ix[:,1], label = '윤건', linestyle = "--", color = "b")
plt.plot(ad.ix[:,2], label = '홍길동', linestyle = ":", color = "y")
plt.title("기록 순위 비교 그래프", fontsize = 15)
plt.xlabel("연도",fontsize = 10)
plt.ylabel("순위",fontsize = 10)
plt.xlim([2014.9,2017.1])
plt.ylim([0.9,3])
plt.xticks([2015,2016,2017],['2015년','2016년','2017년'])
plt.yticks([1,2,3])
plt.legend(loc = 2)  # 범례(기본값 : 자동으로 적절한 위치에 들어감) : 1 ~ 10


# DataFrame에서 바로 그리기
df.plot(kind = 'bar', alpha = .5)  # 막대(수직)
df.plot(kind = 'barh')  # 막대(수평)
df.plot(kind = 'bar', stacked = True)
df.plot(kind = 'barh', stacked = True, legend = False)
df.rank(axis = 0)
df.rank(axis = 1, method = 'dense')


'''
[문제178] yob2016.txt 데이터셋을 이용해서 상위 5위 까지 여자 아기 이름 출생수를 막대그래프로 그리세요.
'''
with open('c:/python/yob2016.txt','r') as file:
    ee = pd.read_table(file, sep = ',', names = ['name','sex','cnt'])

ee

# 상위 5위
childF = ee[ee['sex']=='F'].sort_values(by = 'cnt', ascending = False)
df = childF[childF.rank(ascending = False)['cnt'] <= 5]  
df = df.set_index('name')
df
df.plot(kind = 'bar', color = 'orange')


# 선생님 풀이
yob2016 = pd.read_csv("c:/python/yob2016.txt", names = ['name','sex','birth'])

def top(df, n=5, column='birth'):
    return df.sort_values(by=column, ascending=False)[:n]

data = yob2016.groupby('sex').apply(top)
fdata = data.loc['F'][['name','birth']]
fdata.plot(kind = 'bar')

fdata = fdata.set_index(fdata['name'])
fdata.plot(kind = 'bar', color = 'orange')


plt.clf()  # 그래프 연속으로 그릴때 곂치지 않게 clear해주는 기능


file = "c:/python/stats_104102.xlsx"  # exel
sheet_name = "stats_104102"

data = pd.read_excel(file, sheet_name, header = 1)  # file 2번째 줄이 header = 1
data

data.index
data.columns
data.values

data.ix[['서울','경기']].plot(kind = 'bar', figsize = (10,8))


yob = pd.read_table('c:/python/yob2016.txt', sep = ',', names = ['name','sex','birth'])
yob
yob.count()

yobF = yob[yob.sex == 'F']
yobF.count()

yobM = yob[yob.sex == 'M']
yobM.count()

yobM = yobM.set_index('name')

yobM.head().plot(kind = 'bar')


plt.plot(yobM)


import glob
import time as t
import pandas as pd
file = 'c:/python/yob/yob*.txt'
file_lst = glob.glob(file)
for i in file_lst:
    a = pd.read_csv(i, names = ['name','sex','birth'])
    aF = a[a.sex == 'F'].set_index('name')
    aM = a[a.sex == 'M'].set_index('name')
    aF.head().plot(kind = 'bar', color = 'purple', figsize = (10,9))
    
    t.sleep(.5)
    plt.clf()    
    aM.head().plot(kind = 'bar', color = 'purple', figsize = (10,9)) 


aF['birth'].sum()



## 애니메이션 만들기 최종버전?
# y1년부터 y2년까지 해별 상위 n개 이름 그래프로 저장하는 name이라는 함수 만듬. 
# 성별은 M, F 이외를 입력하면 전체로 만듬.
def Name(y1, y2, n, g):
    import pandas as pd
    from numpy import array
    import matplotlib.pyplot as plt
    import time as t
    from matplotlib import font_manager, rc
    rc('font', family='AppleGothic')
    plt.rcParams['axes.unicode_minus'] = False
    
    for y in range(y1, y2+1):
        df = pd.read_csv('desktop/python/names/yob'+str(y)+'.txt', names=['name','gender','birth'])
        if g in ["M","F"]:
            if g=="M":
                gender="남자 이름 1~"+str(n)+"위"
            else:
                gender="여자 이름 1~"+str(n)+"위"
            df = df[df['gender']==g]
        else:
            gender="전체 이름 1~"+str(n)+"위"
        a = df.sort_values(by="birth", ascending=False)[:n]
        a = a.set_index("name").loc[:,"birth"]
        a.plot(kind="bar", alpha=.5)
        plt.title(str(y)+'년 '+gender)
        # savefig : 사진저장
        plt.savefig('desktop/python/'+str(y)+str(g)+'.png', format="png",
                    bbox_inches="tight")
        plt.clf()
        t.sleep(.02)

#위 함수 이용해서 그림 저장        
Name(1880, 2016, 10, "M")

#저장시킨 그림으로 애니메이션 만듬
import imageio
files=[]
for i in range(1880, 2017):
    files.append(str(i)+"M.png")
files
png_dir = "desktop/python/"
images = []
for i in files:
    file_path=png_dir+i
    images.append(imageio.imread(file_path))
imageio.mimsave(png_dir+'movie.gif', images, duration=.5)


'''
[문제179] 2010 ~ 2016  년도까지 성별 출생 현황을 그래프를 그리세요.
'''
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
%matplotlib inline

yobT = DataFrame()
for i in range(2010,2017):
    yob = pd.read_csv("c:/python/yob/yob"+str(i)+".txt", names=['name','sex','birth'])
    yobF = yob[yob['sex'] == 'F']['birth'].sum()
    yobM = yob[yob['sex'] == 'M']['birth'].sum()
    yobT = yobT.append(DataFrame([[yobF,yobM]],index=[i],columns=['F','M']))
yobT # index : 년도, column : 성별, value : 출생수

maxF = yobT.max()[0]
maxM = yobT.max()[1]

yobT['F'][yobT['F']==maxF].index[0]
yobT['M'][yobT['M']==maxM].index[0]


yobT.plot()
plt.grid()
plt.xlabel('year')
plt.ylabel('birth')
plt.annotate("최고", color = 'r',
             xy=(yobT['F'][yobT['F']==maxF].index[0], maxF), # 최대값 좌표
             xytext=(-90, -50), # 주석
             textcoords='offset points', # 꼭 해야함
             fontsize=10, arrowprops=dict(arrowstyle="->")) # 화살촉
plt.annotate("최고", color = 'r',
             xy=(yobT['M'][yobT['M']==maxM].index[0], maxM), # 최대값 좌표
             xytext=(-90, -50), # 주석
             textcoords='offset points', # 꼭 해야함
             fontsize=10, arrowprops=dict(arrowstyle="->")) # 화살촉


# 선생님 풀이
import csv
import os
from pandas import Series,DataFrame
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
%matplotlib inline


with open('c:/python/yob/yob_total.csv','w') as f:  # 파일생성
    writer = csv.writer(f, delimiter=',')
    for y in range(2010,2017):
        filename='c:\python\yob\yob%d.txt' %y
        name = os.path.basename(filename)
        name = name.split('.')[0]
        df = pd.read_csv(filename, names=['name','gender','birth'])
        gender_cn = df['birth'].groupby(df['gender']).sum()
        f_cn = str(gender_cn.loc['F'])
        m_cn = str(gender_cn.loc['M'])
        writer.writerow([name[3:],f_cn, m_cn])
      


df = pd.read_csv("c:/python/yob/yob_total.csv", names=['년도','여자','남자'])

df = df.set_index("년도")

df.ix[:,0]

df.plot()
df.plot(kind="bar")
df.plot(kind="barh")

plt.plot(df.ix[:,0], label="여자", color="r", linestyle="--")
plt.plot(df.ix[:,1], label="남자", color="b", linestyle=":")
plt.title("성별 출생 현황", fontsize=15)
plt.xlabel("년도",fontsize=10)
plt.ylabel("출생수",fontsize=10)
plt.legend()
plt.grid()
plt.annotate("최고", 
             xy=(df[df['여자'] == df['여자'].max()].index.values, df['여자'].max()), # 최대값 좌표
             xytext=(-90, -50), # 주석
             textcoords='offset points', # 꼭 해야함
             fontsize=10, arrowprops=dict(arrowstyle="->")) # 화살촉
plt.annotate("최고", 
             xy=(df[df['남자'] == df['남자'].max()].index.values, df['남자'].max()),
             xytext=(-90, -50),
             textcoords='offset points', 
             fontsize=10, arrowprops=dict(arrowstyle="->"))


'''[wordcloud 해결방법]
https://github.com/amueller/word_cloud
아나콘다 프롬프트 > conda install -c conda-forge wordcloud'''

from wordcloud import WordCloud,STOPWORDS  # wordcloud
import matplotlib.pyplot as plt  # 그래프
from scipy.misc import imread # 사진파일

with open('c:/python/문재인대통령취임사.txt') as file:
    text = file.read()
text

heart_mask = imread('c:/python/heart.jpg', flatten = True)  # 사진파일 테두리 좌표만 가져옴

wordcloud = WordCloud(font_path = 'c:/Windows/Fonts/malgunbd.ttf',
                      stopwords = STOPWORDS,
                      background_color = 'white',
                      width = 1000,
                      height = 800,
                      mask = heart_mask).generate(text)  # 모양 heart로 나옴

plt.figure(figsize = (10,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()


good_mask = imread('c:/python/h.jpg', flatten = True)
wordcloud = WordCloud(font_path = 'c:/Windows/Fonts/malgunbd.ttf',
                      stopwords = STOPWORDS,
                      background_color = 'white',
                      width = 1000,
                      height = 800,
                      mask = good_mask).generate(text) 
plt.figure(figsize = (10,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()


bat_mask = imread('c:/python/bat.jpg', flatten = True)
wordcloud = WordCloud(font_path = 'c:/Windows/Fonts/malgunbd.ttf',
                      stopwords = STOPWORDS,
                      background_color = 'white',
                      width = 1000,
                      height = 800,
                      mask = bat_mask).generate(text) 
plt.figure(figsize = (10,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()



star_mask = imread('c:/python/star.jpg', flatten = True)
wordcloud = WordCloud(font_path = 'c:/Windows/Fonts/malgunbd.ttf',
                      stopwords = STOPWORDS,
                      background_color = 'white',
                      width = 1000,
                      height = 800,
                      mask = star_mask).generate(text) 
plt.figure(figsize = (10,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()


jordan_mask = imread('c:/python/jordan.jpg', flatten = True)
wordcloud = WordCloud(font_path = 'c:/Windows/Fonts/malgunbd.ttf',
                      stopwords = STOPWORDS,
                      background_color = 'white',
                      width = 1000,
                      height = 800,
                      mask = jordan_mask).generate(text) 
plt.figure(figsize = (10,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()


che_mask = imread('c:/python/che.jpg', flatten = True)
wordcloud = WordCloud(font_path = 'c:/Windows/Fonts/malgunbd.ttf',
                      stopwords = STOPWORDS,
                      background_color = 'white',
                      width = 1000,
                      height = 800,
                      mask = che_mask).generate(text) 
plt.figure(figsize = (10,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()


ghost_mask = imread('c:/python/ghost.jpg', flatten = True)
wordcloud = WordCloud(font_path = 'c:/Windows/Fonts/malgunbd.ttf',
                      stopwords = STOPWORDS,
                      background_color = 'white',
                      width = 1000,
                      height = 800,
                      mask = ghost_mask).generate(text) 
plt.figure(figsize = (10,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()




# 예쁘게 한다능 : https://github.com/matplotlib/matplotlib/issues/8012
plt.figure(figsize=(10,10))
plt.imshow(wordcloud, interpolation="gaussian")
plt.axis("off")
plt.show()



