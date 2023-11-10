def solution(phone_book):
    answer = True
    _phone_book = sorted(phone_book)
    
    for i in range(len(_phone_book) - 1):
        if len(_phone_book[i]) < len(_phone_book[i+1]):
            if _phone_book[i] == _phone_book[i+1][:len(_phone_book[i])]:
                answer = False
    return answer