# coding: utf-8

# # 그리디 실전문제 
# - 최적의 해 찾기
# - 그리디 정당성 찾기
# - 아이디어 !!!!!!!!!

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


"""조건을 잘보자!!!!!!!!!!!""" 


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






