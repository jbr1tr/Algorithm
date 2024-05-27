def solution(num_list):
    answer = 0
    even = ''
    odd = ''
    for i in num_list:
        if i % 2 == 0: # 짝수
            even += str(i)
        else: # 홀수
            odd += str(i)
    answer = int(even) + int(odd)
    return answer