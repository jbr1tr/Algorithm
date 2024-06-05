def solution(ineq, eq, n, m):
    answer = 0
    
    # temp 변수에 식 생성 
    temp = ""
    temp += str(n)
    temp += ineq
    if eq == "=":
        temp += eq
    temp += str(m)
    
    # eval 함수로 계산 
    if eval(temp) == True:
        answer = 1
    else:
        answer = 0
    return answer