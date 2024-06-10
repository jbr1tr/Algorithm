def solution(array):
    answer = []
    max_int = -1
    max_index = -1
    
    for i in range(len(array)):
        if array[i] > max_int:
            max_int = array[i]
            max_index = i
            
    answer.append(max_int)
    answer.append(max_index)
    
    return answer