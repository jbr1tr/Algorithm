def solution(arr, queries):
    answer = []
    for i in queries:
        count = 0
        temp = 999999999999
        for j in range(i[0], i[1] + 1):
            if arr[j] > i[2]:
                temp = min(arr[j], temp)
                count += 1
        if count == 0:
            answer.append(-1)
        else:
            answer.append(temp)
    return answer
