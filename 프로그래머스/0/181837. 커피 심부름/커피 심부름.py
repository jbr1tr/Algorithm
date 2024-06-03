def solution(order):
    answer = 0
    
    americano = ["iceamericano", "americanoice", "hotamericano", "americanohot",	
                 "americano", "anything"]
    latte = ["icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot",
             "cafelatte"]
    
    for i in order:
        if i in americano:
            answer += 4500
        elif i in latte:
            answer += 5000
    return answer