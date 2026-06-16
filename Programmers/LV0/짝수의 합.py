'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120831

    정수 n이 주어질 때 n 이하의 모든 짝수 합
'''

def solution(n):
    answer = 0
    for i in range(n+1):
        if i % 2 == 0:
            answer += i
    return answer

'''
    [다른 사람의 풀이]   
    def solution(n):
    return sum([i for i in range(2, n + 1, 2)])
'''