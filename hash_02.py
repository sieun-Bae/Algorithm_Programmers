def solution(clothes):
    h = {}
    for i in clothes:
        h[i[1]] = h.get(i[1], 0) + 1
    g = [ i+1 for i in h.values()]

    answer = 1
    for i in g:
        answer = answer*i    
    return answer-1
