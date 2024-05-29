def solution(a, b):
    answer = 0
    if a % 2 != 0 and b % 2 != 0: # 둘 다 홀수
        answer = a ** 2 + b ** 2
    elif a % 2 == 0 and b % 2 == 0: # 둘 다 홀수 x
        answer = abs(a - b)
    else: # 둘 중 하나만 홀수
        answer = 2 * (a + b)
    return answer