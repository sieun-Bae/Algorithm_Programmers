###2016년###
###level1###
###sieun Bae###
def solution(a, b):
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    num=0
    while True:
        if a==1:
            break
        else:
            num = num+ days[a-2]
            a-=1
    num = num+(b-1)
    answer = day[num%7]
    return answer
