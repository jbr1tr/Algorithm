def solution(num_list):
    answer = []
    count_even = 0
    count_odd = 0
    
    for i in num_list:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
            
    answer.append(count_even)
    answer.append(count_odd)
    
    return answer