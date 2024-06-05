def solution(price, money, count):
    answer = -1
    temp = 0
    
    for i in range(count):
        temp += (i + 1) * price
        
    if temp > money:
        answer = temp - money
    else:
        answer = 0

    return answer