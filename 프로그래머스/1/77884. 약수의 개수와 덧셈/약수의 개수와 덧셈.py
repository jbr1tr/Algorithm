def solution(left, right):
    answer = 0
    cnt = 0
    
    for i in range(left, right + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0: # 약수의 개수가 짝수
            answer += i
        else: # 약수의 개수가 홀수 
            answer -= i
        cnt = 0 # i마다 약수의 개수 리셋 
        
    return answer