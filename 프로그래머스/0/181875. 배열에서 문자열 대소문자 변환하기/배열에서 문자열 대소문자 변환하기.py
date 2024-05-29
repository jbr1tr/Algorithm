def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i % 2 == 0: # 짝수번째 인덱스
            answer.append(strArr[i].lower())
        else: # 홀수번째 인덱스
            answer.append(strArr[i].upper())
    return answer