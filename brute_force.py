def byFreq(pair):
    return pair[1]
    
def solution(answers):
    answer = {1:0, 2:0, 3:0}
    final = []
    answer1 = [1,2,3,4,5]
    answer2 = [2,1,2,3,2,4,2,5]
    answer3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answer1[i%5] == answers[i]:
            answer[1] += 1
        if answer2[i%8] == answers[i]:
            answer[2] += 1
        if answer3[i%10] == answers[i]:
            answer[3] += 1
            
    answer = list(answer.items())
    answer.sort(key=byFreq, reverse=True)
    a = answer[0][1]
    b = answer[1][1]
    c = answer[2][1]
    if a != b:
        final=[answer[0][0]]
    elif b != c:
        final=[answer[0][0], answer[1][0]]
    else:
        final=[answer[0][0], answer[1][0], answer[2][0]]
    return final

