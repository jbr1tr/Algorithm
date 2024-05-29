def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        temp = a + d * i
        print(temp)
        if included[i] == True:
            answer += temp
    return answer