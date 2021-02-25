# -*- coding: utf-8 -*-
# Problem 9 : a + b + c = 1000 인 피타고라스 수 a, b, c를 구하자!

for a in range(1, 1000):
  for b in range(1, 1000):
    c = 1000-b-a
    sum = a*a + b*b
    if c*c == sum:
      print(a*b *c)

# Problem 10 : 200만이하 소수의 합
from tqdm.notebook import tqdm

sum = 0

for i in tqdm(range(2, 2000001)):   # i : 소수 후보
  yaksu = 0
  for j in range(1, i+1):
    if i%j == 0:
      yaksu += 1   # i까지 선형탐색이라 굉장히 오래걸림(1시간 넘게) >> 알고리즘 개선 필요
  
  if yaksu==2 :
    sum += i
sum

# 에라토스테네스의 체 이용

n = 2000000
a = [False, False] + [True] * (n-1)   # False 두번, True가 n-1번 등장
sum = 0

for i in range(2, n+1):
  if a[i] == True:
    sum += i 
    
    for j in range(2*i, n+1, i):   # 소수의 배수를 지워간다 
      a[j] = False

print(sum)  ## 빠른 시간효율!
