'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120906
    주어진 정수의 각 자리수 더하기
'''


def solution(n):
    answer = 0

    for _ in range(n):
        answer += n % 10
        n = n // 10

    return answer

'''
    [주어진 정수 문자화]
    def solution(n):
        return sum(int(i) for i in str(n))
'''