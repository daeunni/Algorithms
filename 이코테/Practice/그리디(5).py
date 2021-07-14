#!/usr/bin/env python
# coding: utf-8

# # 그리디 실전문제 
# - 최적의 해 찾기
# - 그리디 정당성 찾기
# - 아이디어 !!!!!!!!!

# In[51]:


# 1) 모험가 길드 : 정렬 후 작은 수 부터 그 수만큼 묶고, 개수를 세자 + 노답인 수는 버리기 !!!!11

n = int(input())
scare = list(map(int, input().split()))  # 공포도
scare.sort()  # 정렬
group_num = 0
n = n-1             # 인덱스때문

while n>0:
    b = int(scare[0])  
    n = n-b
    if len(scare)>scare[n]:    #  맨 뒤 조건 추가(버릴 애 결정 여부)
        while b!=0:          
            scare.pop(0)  # 앞에서부터 버림 
            b = b-1
        group_num +=1
print(group_num)    


# **조건을 잘보자!!!!!!!!!!!** 

# In[70]:


# 2) 곱하기 혹은 더하기 : 무조건 큰 수만 만들자 (누적해서 연산할 수 있도록! )

num = input()  # input은 string을 input으로 받는다
result = int(num[0])  # 이걸 0대신 초깃값으로 주자

for i in range(len(num)-1):
    b = int(num[i+1])
    if result+b > result*b:
        result = (result+b)   
    else:
        result = (result*b)  # 누적해서 연산할 수 있도록
print(result)


# In[3]:


# 5) 볼링공 고르기 : 가능한 조합을 itertools로 구한 후 조건에 안맞는건 빼기! 

n, m = map(int, input().split())
k = list(map(int, input().split()))   # 각 볼링공의 무게 
result = []

from itertools import combinations   # 조합 출력 
com = list(combinations(k, 2))
for i in range(len(com)):
    if com[i][0] != com[i][1]:
        result.append(com[i])
print(len(result))


# **다른 방법** : 무게마다 볼링공이 몇 개 있는지를 계산 후 A가 선택할 수 있는 경우를 리스트 위치로 지정. 그 후 B가 선택하는 경우의 수와 곱하기
# > 리스트 위치로 계산 !! 

# In[11]:


n=8 ; m=5
data = [1, 5, 4, 3, 2, 4, 5, 2]
result = 0

# 1부터 10까지 무게를 담을 수 있는 리스트
weight = [0] * 11

# 각 무게에 해당하는 볼링공 개수 카운트
for x in data:
    weight[x] += 1  
    print(weight)
    
for i in range(1, m+1):
    n -= weight[i]         # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += weight[i] * n   # B가 선택하는 경우의 수와 곱하기

print(result)


# In[8]:


weight


# In[ ]:





# In[ ]:





# In[ ]:




