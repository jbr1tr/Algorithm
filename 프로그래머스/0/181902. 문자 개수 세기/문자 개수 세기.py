def solution(my_string):
    upper = [0 for i in range(ord("A"), ord("Z") + 1)]
    lower = [0 for i in range(ord("a"), ord("z") + 1)]
    for i in my_string:
        if i.isupper():
            upper[ord(i) - 65] += 1
        else:
            lower[ord(i) - 97] += 1
    result = upper + lower
    return result