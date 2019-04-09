###algorithm programmers python level1###
###완주하지 못한 선수###
###sieun bae###

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
    answer = participant[-1]
    return answer

participant = ["leo", "kiki", "edun"]
completion = ["edun", 'kiki']

solution(participant, completion)