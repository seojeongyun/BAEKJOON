'''
    https://www.acmicpc.net/problem/2292

    2 / 128

    중앙의 방 1부터 시작해서 이ㅇ웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매김

    숫자 N이 주어졌을 때 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때
    몇 개의 방을 지나가는지 계산하는 프로그램을 작성하시오. (시작과 끝 포함)

    입력
        - N(1 ≤ N ≤ 1,000,000,000)

    출력
        - 지나는 방의 최소 개수
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    N = int(input().strip())

    # [1] 최소 개수
    # 벌집 층 경계의 최대값
    # 1 + 6 * 0 = 1
    # 1 + 6 * 1 = 7
    # 7 + 6 * 2 = 19
    # 19 + 6 * 3 = 37
    numbox = 1
    cnt = 1
    while N > numbox:
        numbox += 6 * cnt
        cnt += 1

    print(cnt)