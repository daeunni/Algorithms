#!/usr/bin/env python
# coding: utf-8

# In[23]:


# 1330번 
a, b = map(int, input().split())  # 입력 받고 공백으로 구분
if a>b:
    print('>')
elif a<b:
    print('<')
elif a==b:
    print('==')


# In[26]:


# 9498번
a = int(input())
if 90<=a<=100:
    print('A')
elif 80<=a<=89:
    print('B')
elif 70<=a<=79:
    print('C')
elif 60<=a<=69:
    print('D')
else:
    print('F')


# In[31]:


# 2753번
y = int(input())
if y%4==0 and y%100!=0:
    print(1)
elif y%400==0:
    print(1)
else:
    print(0)        


# In[64]:


# 14681번 : 사분면 고르기
a, b = map(int, input().split())
if a>0 and b>0:
    print(1)
elif a>0 and b<0:
    print(4)
elif a<0 and b>0:
    print(2)
else:
    print(4)


# In[38]:


# 14681번 : 사분면 고르기
a = int(input())
b = int(input())
if a>0 and b>0:
    print(1)
elif a>0 and b<0:
    print(4)
elif a<0 and b>0:
    print(2)
elif a<0 and b<0:
    print(3)


# In[54]:


# 2884번 : 알람 시계
h, m = map(int, input().split())
if 0<h<=12:
    hour = (h*60+m) -45
    print(hour//60, hour%60)
    
elif 13<=h<24:
    h-=12  # 12빼고 저장
    hour = (h*60+m) -45
    print(hour//60+12, hour%60)

elif h==0:
    h+=12
    hour = (h*60+m) -45
    if m>=45:
        print(hour//60-12, hour%60)
    else:
        print(hour//60+12, hour%60)  # 고려해야할 반례 : 0시 45분


# In[55]:


# 2884번 더 쉽게....
a, b= map(int, input().split())
x = a*60+b-45
print(x//60%24, x%60)   # 하아....난 멀었다 멀었어....


# In[75]:


# 10871번 : x보다 작은 수
n, x = map(int, input().split())
a = list(map(int, input().split()));b=[]

for i in list(a):
    if i<x:
        b.append(str(i))
print(" ".join(b), end="")  # join 함수 사용!


# In[77]:


# 10952번 : A+B-5    
while 1:
    a, b = map(int, input().split())
    if a+b>0:
        print(a+b)
    else:
        break
        
#### 런타임 에러가 나는 코드>>> input이 조건절 뒤에 위치하기 때문인듯!
while (a!=0 and b!=0):
    a, b = map(int, input().split())
    print(a+b)

