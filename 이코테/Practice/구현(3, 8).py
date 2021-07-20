# 9. 문자열 압축 : 문자열의 단위 중 가장 짧게 압축 되는 것을 반환 

def solution(s):   # s = 문자열
    answer = len(s)
    
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:step]   # 앞에서부터 step 만큼 문자열 추출
        count = 1
        
        for j in range(step, len(s), step):  # 시작을 step으로 놓기
            
            # 연속한 그 다음게 같으면 
            if prev == s[j: j+step]:  
                count += 1  # count 하나 추가 
            
            # 같지 않다면 
            else:
                compressed += str(count) + prev if count>=2 else prev
                prev = s[j: j+step]  # 다시 상태 초기화. prev 재설정 
                count = 1
                
        # 남아있는 문자열 처리
        compressed += str(count) + prev if count>=2 else prev
        answer = min(answer, len(compressed))  # 계속 둘 중 작은거 저장 
    
    return answer  # 가장 작은게 반환됨 

## 이 생각을 대체 어떻게해요....역시 카카오....


# 14. 외벽점검 : 외벽 둘레, distance에 맞는 최소 친구 수 출력 

from itertools import permutations

def solution(n, weak, dist):   # weak : 취약 지점
    length = len(weak)
    
    for i in range(length):
        weak.append(weak[i]+n)   # 길이를 2배로 늘려서 원형을 일자로 만들기
        
    answer = len(dist) + 1   # 투입할 최소 친구 수
    
    for start in range(length):
        
        for friends in list(permutations(dist, len(dist))):  # 친구 나열 경우의 수 조합
            count = 1
            position = weak[start] + friends[count-1]
            
            for index in range(start, start+length):
                if position < weak[index]:
                    count += 1 
                    
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count-1]
                    
        answer = min(answer, count)

    if answer > len(dist):
        return -1
    
    return answer

