'''
    설명: https://www.acmicpc.net/problem/1004

    입력:
        지도, 출발점, 도착점
        - TC
        - 출발점(x1, y1), 도착점(x2, y2)
        - 행성계 개수 N
        - N개의 줄에 걸쳐 (cx, cy, r)

    출력:
        최소의 행성계 진입/이탈 횟수

'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    answ_lst = []
    TC = int(input().strip())
    for _ in range(TC):
        answ = 0
        # [0] 입력
        x1, y1, x2, y2 = map(int, input().strip().split())
        N = int(input().strip())
        circle = [list(map(int, input().strip().split())) for _ in range(N)]

        # [1]
        # 행성계 진입/탈출을 하는 경우는
        # 출발점은 원 안에, 도착점은 원 밖에 있는 경우거나
        # 도착점은 원 안에, 출발점은 원 밖에 있는 경우
        for cx, cy, r in circle:
            from_start_to_center = ((x1-cx)**2 + (y1-cy)**2) ** (1/2)
            from_center_to_end =  ((x2-cx)**2 + (y2-cy)**2) ** (1/2)

            if from_start_to_center < r and from_center_to_end > r:
                answ += 1

            elif from_start_to_center > r and from_center_to_end < r:
                answ += 1

        answ_lst.append(answ)

    for answ in answ_lst:
        print(answ)

'''
    시간복잡도: O(N) * TC
'''