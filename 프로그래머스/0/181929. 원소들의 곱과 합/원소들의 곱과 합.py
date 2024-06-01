def solution(num_list):
    answer = 0
    n_product = 1 
    n_pow = 0
    
    # 모든 원소들의 곱
    for i in num_list:
        n_product *= i
    # 모든 원소들의 합의 제곱
    n_pow = sum(num_list) ** 2
    
    answer = 1 if n_product < n_pow else 0
    
    return answer