'''
    자연수 N과 M이 주어졌을 때
    1부터 N까지 자연수 중에 중복 없이 M개를 고른 수열을 모두 구하는 프로그램을 작성하시오

    출력: 오름차순으로 출력

    EX) N = 3, M = 1
        1부터 3까지 자연수 중 중복 없이 1개를 고른 수열을 모두 구해라
        1, 2, 3

    조합: 1부터 N까지 중복없이 M개 뽑을 수 있는 경우의 수 구하기
        - 중복이 없어야 한다 => list 내에 들어있으면 continue
        - M개 뽑아야 한다   => M개 되면 return
'''

import sys

def combination(n, lst):
    global answ

    # [1] 종료 조건 및 정답 처리
    if n == M:
        answ.append(lst)
        return

    # [2] 하부 함수 호출
    for i in range(1, N+1):
        # 중복 처리
        if i not in tuple(lst):
            # lst.append(i)
            combination(n+1, lst+[i])

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M = map(int, input().rstrip().split())

    answ = []
    combination(0, [])

    for answer in answ:
        print(*answer)