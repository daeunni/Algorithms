#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 1. 왕실의 나이트 : 현재 위치를 0으로 놓고 이동 방향 8개 정의

place = input()  # 처음 위치를 잡기
column = int(ord(place[0]))- int(ord('a')) + 1  # 아스키코드 반환 함수
row = int(place[1])

# 나이트가 이동할 수 있는 8가지 방향 (현재 위치를 0으로 놓기)
steps = [(-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for i in steps:                # 각 경우의수를 for문으로 하나씩 판단 
    next_row = row + i[0]
    next_col = column + i[1]
    
    if next_row >=1 & next_row<=8 & next_col >=1 & next_col<=8:
        result += 1

print(result)


# In[10]:


# 2. 럭키 스트레이트 : 그냥 좌우가 같은지 판단하면 되는 단순한 문제 

num = input()
length = len(num)
print(length)
first = 0 ; second= 0 
mid = length/2 -1 

for i in range(len(num)):
    if i<= mid :
        first += int(num[i])
        
    else:
        second += int(num[i])   
        
if first == second:
    print('Lucky')
else:
    print('Ready')


# In[ ]:


## 다른풀이 : 더했다가 빼서 0 나오게 하기도 가능!!! 

for i in range(length//2):   # 왼쪽 부분의 자릿수 합
    summary += int(num[i])

for i in range(length//2, length):  # 오른쪽 부분의 자릿수 합 다시 빼기
    summary -= int(num[i])

if summary == 0:      # 왼쪽, 오른쪽 합이 상쇄되면 출력! 
    print('LUCKY')  
else:
    print('READY')
    
### 이렇게 하면 더했다가 빼니까 메모리 절약을 할 수 있을 것 같다..!! 


# In[37]:


# 3. 문자열 재정렬 : 아스키코드 ord(), chr() 함수 이용 

# a = input()
a = 'AJKDLSI412K4JSJ9D'

asc = [];num = 0
result = ""

for i in range(len(a)):             # 숫자, 문자 판단
    if a[i].isalpha():              # isalpha() : 문자열 판단 함수
        asc.append(ord(a[i]))
    else:
        num += int(a[i])
        
asc.sort() 
for i in range(len(asc)):   # 문자열 추가
    result += chr(asc[i])
    
result += str(num)
print(result)


# In[ ]:


## 아 근데 sort 함수 특성상 굳이 아스키코드 변환을 안써도 됐음,,,,
## >> 이중 for문이라 비효율적이다!

for i in data:
    if x.isalpha():
        result.append(x)
    
    else:
        value += int(x)
result.sort()

if value!=0:
    result.append(str(value))

