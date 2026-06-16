'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120836

    소인수분해 개수 구하기
    -> 처음엔 2중 포문으로 i * j == 20인 걸 구했는데 시간초과
    -> 반대로 나눴을 때 나머지가 0이되는 것의 개수를 구함
'''

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += 1
    return answer

