def solution(n):
    answer = ""
    arr = []
    temp = str(n)
    
    for i in temp:
        arr.append(i)
    arr.sort(reverse = True)
    for i in arr:
        answer += i
    answer = int(answer)
    return answer