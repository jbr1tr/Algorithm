def solution(myString):
    answer = ''
    for i in myString:
        if i.islower() == True:
            answer += i.upper()
        else:
            answer += i
    return answer