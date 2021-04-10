#!/usr/bin/env python
# coding: utf-8

# In[3]:


## 1차원 배열
# 10818번 : 최소, 최대(1차원 배열)

N = int(input())
B = list(map(int, input().split()))

if len(B)==N:
    print(min(B), max(B))


# In[6]:


# 2562번 : 최댓값
i=0; number=[]
while i<9:
    a = int(input())
    number.append(a)
    i+=1
max_num = max(number)
print(max_num)
print(number.index(max_num)) ## 수정 필요 

