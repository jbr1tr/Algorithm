def solution(l, r):
    answer = []
    arr = ["1", "2", "3", "4", "6", "7", "8", "9"]
    cnt = 0
    
    for i in range(l, r+1):
        for j in str(i):
            if j in arr:
                cnt += 1
        if cnt == 0:
            answer.append(i)
        cnt = 0
        
    if len(answer) == 0:
        answer.append(-1)
        
    return answer
