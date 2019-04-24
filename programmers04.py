#같은 숫자는 싫어
#coded by sieun bae in 24-04-19
#considering time complexity
def solution(arr):
    answer = []
    key = arr[0]
    answer.append(key)
    for i in arr:
        if key != i:
            answer.append(i)
            key = i
    return answer
