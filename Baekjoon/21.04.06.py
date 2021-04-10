#!/usr/bin/env python
# coding: utf-8

# In[8]:


# 10951번 : A+B-4
while 1:
    try:
        a, b = map(int, input().split())
        if 0<a and b<10:
            print(a+b) ## 런타임에러(a, b 입력이 들어오지 않았을 때 예외처리를 해줘야함.....!)            
    except:
        break


# In[39]:


# 1110번 : 더하기 사이클
n = str(input())
ori = n
i=0        # 사이클 횟수
while 1 : 
    if len(n)==1:  # 들어온 수가 한자리수일 때 예외처리
        n = '0' + n
        ori = '0' + ori
    ss = str(eval('+'.join(n)))  # 들어온 수 각 자리숫자의 합
    if len(ss)==1:  # 자릿수 합이 한자리수일 때 예외처리
        ss = '0'+ ss
        
    new = str(n)[1] + str(ss)[1]
    n = new
    
    i +=1
    
    if new==ori:   # 한자리수일 때 이 break를 해결해야함
        break
print(i)


# In[40]:


# 1110번 쉽게풀기...
N = int(input())
n = -1
t =  0  # 횟수
while n != N:
    if n==-1:
        n=N
        
    n = (n//10 + n%10)%10 + (n%10)*10   # 이부분이 히트네요
    print(n)
    t+=1
    
print(t)

