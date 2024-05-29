def solution(arr, k):
    answer = []
    if k % 2 != 0: # k가 홀수
        for i in arr:
            answer.append(i * k)
    else: # k가 짝수 
        for i in arr:
            answer.append(i + k)
    return answer