def solution(picture, k):
    temp = ["" for i in range(len(picture))]
    result = []
    
    for i in range(len(picture)):
        for j in picture[i]:
            temp[i] += j * k
    
    for i in temp:
        for j in range(k):
            result.append(i)
    
    return result