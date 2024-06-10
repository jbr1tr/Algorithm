def solution(n):
    answer = 2
    for i in range(n):
        if i ** 2 == n:
            answer = 1
    return answer