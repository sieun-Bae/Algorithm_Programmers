def byFreq(pair):
    return pair[1]

def solution(genres, plays):
    h = {} 
    t = {} #total num of plays
    for i in set(genres):
        h[i] = list()
        t[i] = 0
    for i in range(len(genres)):
        h[genres[i]].append([i, plays[i]])
        t[genres[i]] += plays[i]
    
    t = list(t.items())
    t.sort(key = byFreq, reverse = True)
    for key in h.keys():
        h[key].sort(key = byFreq, reverse = True)

    answer = []
    for key in t:
        for i in range(2):
            if ((len(h[key[0]])==1) and (i == 1)):
                break
            answer.append(h[key[0]][i][0])
    return answer
