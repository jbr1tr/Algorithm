def solution(seoul):
    answer = ''
    key = 0
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            key = i
    answer = "김서방은 " + str(key) + "에 있다"
    return answer