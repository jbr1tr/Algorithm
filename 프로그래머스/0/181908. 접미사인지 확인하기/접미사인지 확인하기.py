def solution(my_string, is_suffix):
    answer = 0
    str_len = len(my_string)
    suf_len = len(is_suffix)
    if my_string[(str_len - suf_len):str_len] == is_suffix:
        answer = 1
    return answer