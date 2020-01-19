def solution(array, commands):
    answer = []
    
    for i in commands:
        array_2 = array[i[0]-1:i[1]]
        array_2.sort()
        answer.append(array_2[i[2]-1])
    return answer