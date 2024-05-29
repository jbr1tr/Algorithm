def solution(my_string, n):
    answer = ''
    ms_len = len(my_string)
    for i in range(ms_len - n, ms_len):
        answer += my_string[i]
    return answer