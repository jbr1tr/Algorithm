def solution(my_string, s, e):
    # s가 0일때 고려 
    if s != 0:
        answer = my_string[0:s] + my_string[e:s-1:-1] + my_string[e+1:]
    else:
        answer = my_string[e::-1] + my_string[e+1:]
    return answer