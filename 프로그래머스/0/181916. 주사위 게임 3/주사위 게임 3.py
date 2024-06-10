import math

def solution(a, b, c, d):
    temp = [a, b, c, d]
    temp.sort()
    answer = 0
    
    # 숫자가 모두 같을 때 
    if temp[0] == temp[1] and temp[1] == temp[2] and temp[2] == temp[3]: 
        answer = 1111 * a
    # 세 주사위가 같을 때
    elif (temp[0] == temp[1] and temp[1] == temp[2]): 
        answer = math.pow(10 * temp[0] + temp[3], 2)
    elif (temp[1] == temp[2] and temp[2] == temp[3]):
        answer = math.pow(10 * temp[1] + temp[0], 2)
    # 두 개씩 같은 값 
    elif temp[0] == temp[1] and temp[2] == temp[3]: 
        answer = (temp[0] + temp[2]) * abs(temp[0] - temp[2])
    # 두 개만 서로 같을 때 
    elif temp[0] == temp[1]:
        answer = temp[2] * temp[3]
    elif temp[1] == temp[2]:
        answer = temp[0] * temp[3]
    elif temp[2] == temp[3]:
        answer = temp[0] * temp[1]
    # 모두 다를 때 
    elif temp[0] != temp[1] and temp[1] != temp[2] and temp[2] != temp[3]:
        answer = temp[0]
    return answer