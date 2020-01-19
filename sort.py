def solution(numbers):
    d = {}
    answer = ''
    
    for i in range(10):
        d[i+1] = []
        
    #첫 자리수가 1-9인, 각각 경우에 해당하는 자료로 분리하여 저장        
    for i in numbers:
        if str(i)[0]=='1' :
            d[1].append(i)
        if str(i)[0]=='2' :
            d[2].append(i)
        if str(i)[0]=='3' :
            d[3].append(i)
        if str(i)[0]=='4' :
            d[4].append(i)
        if str(i)[0]=='5' :
            d[5].append(i)
        if str(i)[0]=='6' :
            d[6].append(i)
        if str(i)[0]=='7' :
            d[7].append(i)
        if str(i)[0]=='8' :
            d[8].append(i)
        if str(i)[0]=='9' :
            d[9].append(i)

    for i in range(1,10,1):
        #자릿수로 비교하여 한자리 수 먼저, 그 다음 자릿수마다 비교하여 더 큰값이 나올 때 먼저 넣기
        if (10-i) in d[10-i]:
            for i in range(len(d[10-i])):
                
        #
        for j in d[10-i]:
            answer = answer+str(j)
        
    return answer
