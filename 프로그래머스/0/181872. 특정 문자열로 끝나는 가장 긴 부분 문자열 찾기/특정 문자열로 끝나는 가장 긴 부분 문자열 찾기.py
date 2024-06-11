def solution(myString, pat):
    answer = myString[0: myString.rfind(pat) + len(pat)]
    return answer