def solution(s):
    answer = ''
    if len(s) % 2 == 0: # 길이 짝수
        answer = s[int(len(s)/2) - 1 : int(len(s)/2) + 1]
    else: # 길이 홀수 
        answer = s[int(len(s)/2)]
    return answer