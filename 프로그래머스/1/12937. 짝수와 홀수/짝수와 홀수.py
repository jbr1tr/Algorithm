def solution(num):
    answer = ''
    if num % 2 == 0: # 짝수
        answer = "Even"
    elif num % 2 != 0:
        answer = "Odd"
    return answer