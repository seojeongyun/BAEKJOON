'''
    https://www.acmicpc.net/problem/1051

    2 / 128

    직사각형: N x M
        각 칸에 한 자리 숫자

    꼭짓점에 쓰여있는 수가 모두 같은 가장 큰 정사각형 찾기

    출력: 가장 큰 정사각형의 넓이

    * N, M <= 50
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = -1

    # [0] 입력
    N, M = map(int, input().strip().split())
    MAP = [list(map(int, input().strip())) for _ in range(N)]

    # [1] 시작점 순회: O(N^2)
    for i in range(N):
        for j in range(M):
            ci, cj = i, j
            val = MAP[ci][cj]
            dist = (N-1)-ci if (N-1)-ci < (M-1)-cj else (M-1)-cj
            # [2] 정사각형 찾기: O(N)
            for didj in range(1, dist+1):
                if val == MAP[ci+didj][cj] == MAP[ci][cj+didj] == MAP[ci+didj][cj+didj]:
                    extent = (didj+1) ** 2
                    answ = max(answ, extent)

    # [3] 출력
    if answ == -1:
        print(1)
    else:
        print(answ)

'''
    시간 복잡도
        - 시작점 찾기 순회: O(N*M), N,M <= 50이므로 O(N^2)로 간주
        - 최대 정사각형 찾기 순회: O(N)
            - 엄밀히는 O(N)이 아닌데, O(N)보다 클 수 없으니 O(N)으로 간주
        - 최종: O(N^3) -> O(50^3) 이므로 2초 이내 가능
    
    공간 복잡도:
        - MAP: O(N*M)
'''

'''
    테스트 케이스
    TC1
        1 1
        1
        
    TC2
        2 2
        11
        11
        
    TC3
        4 4
        1011
        2220
        2221
        1001
'''