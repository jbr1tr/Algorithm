def solution(s):
    answer = True
    count_p = 0
    count_y = 0
    
    for i in s:
        if i == "p" or i == "P":
            count_p += 1
        elif i == "y" or i == "Y":
            count_y += 1
    
    answer = False if (count_p != count_y) else True
        
    return answer