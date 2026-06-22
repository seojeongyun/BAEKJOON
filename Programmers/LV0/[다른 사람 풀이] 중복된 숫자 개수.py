'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120583

    list.count(n): list 내에 n의 개수 return
'''

def solution(array, n):
    answer = 0
    for e in array:
        if e == n:
            answer += 1
    return answer

'''
    def solution(array, n):
    return array.count(n)
'''