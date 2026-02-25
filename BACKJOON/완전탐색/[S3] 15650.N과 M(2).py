'''
    https://www.acmicpc.net/problem/15650

    자연수 N과 M이 주어졌을 때
    1부터 N까지 자연수 중에 중복 없이 M개를 고른 수열을 모두 구하는 프로그램을 작성하시오

    * 고른 수열은 오름차순이어야 한다.
        - 중복 없이 (2,3)과 (3,2)를 골랐다고 했을 때, (3,2)는 내림차순이므로 틀림
        - 즉 (2,3)만 정답

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
        # 대소 비교
        if len(lst) == 0:
            combination(n + 1, lst + [i])
        else:
            if i > lst[-1]:
                # lst.append(i)
                combination(n+1, lst+[i])

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M = map(int, input().rstrip().split())

    answ = []
    combination(0, [])

    for answer in answ:
        print(*answer)