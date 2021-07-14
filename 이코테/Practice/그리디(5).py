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



