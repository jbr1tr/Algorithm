def solution(arr):
    answer = []
    temp = []
    for i in range(len(arr)):
        if arr[i] == 2:
            temp.append(i)
    if len(temp) >= 2:
        answer = arr[temp[0]:temp[-1] + 1]
    elif len(temp) == 1:
        answer = [2]
    else:
        answer = [-1]
    return answer