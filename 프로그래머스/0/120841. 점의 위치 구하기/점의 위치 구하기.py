def solution(dot):
    answer = 0
    if dot[0] > 0: # x좌표 > 0
        answer = 1 if dot[1] > 0 else 4
    else: # x좌표 < 0
        answer = 2 if dot[1] > 0 else 3
    return answer