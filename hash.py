#hash

def solution(phone_book):
    N = min(phone_book)
    n = len(min(phone_book))
    I = phone_book.index(N)
    del phone_book[I]
    
    for i in range(len(phone_book)):
        if phone_book[i][:n] == N:
            return False
    return True
