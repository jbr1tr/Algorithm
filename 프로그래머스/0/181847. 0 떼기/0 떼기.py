def solution(n_str):
    answer = ''
    key = 0
    for i in range(len(n_str)):
        if n_str[i] != "0":
            key = i
            break
    answer = n_str[key:]
    return answer