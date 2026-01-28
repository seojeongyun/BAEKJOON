'''
    https://www.acmicpc.net/problem/2206
    https://www.acmicpc.net/problem/2178 : 미로 탐색 문제

    격자: N x M
        0은 이동할 수 있는 곳
        1은 이동할 수 없는 곳

    이동: (1,1) -> (N, M)
        시작점과 도착점을 포함해 최단 경로 이동

    벽 부수기:
        1로 표시된 곳 한 번 까지 이동 가능

    출력: 최단 경로, 도착지에 도착 못하는 경우 -1
'''

import sys
from collections import deque

def in_range(i, j):
    return 0 <= i < N and 0 <= j < M

def bfs(start):
    i, j, k = start
    DQ = deque()
    DQ.append(start)
    v[k][i][j] = 1

    while DQ:
        ci, cj, ck = DQ.popleft()
        if (ci, cj) == (N-1, M-1):
            return v[ck][ci][cj]
        # 네 방향
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = ci + di, cj + dj
            # 범위 내, 미방문, 조건: 벽을 마주치지 않은 경우
            if in_range(ni,nj) and not v[ck][ni][nj] and not MAP[ni][nj]:
                DQ.append((ni, nj, ck))
                v[ck][ni][nj] = v[ck][ci][cj] + 1
            # 범위 내, 미방문, 조건: 벽을 마주쳤고 벽을 아직 부수지 않은 경우
            elif in_range(ni,nj) and not v[ck+1][ni][nj] and MAP[ni][nj] and ck == 0:
                DQ.append((ni, nj, ck+1))
                v[ck+1][ni][nj] = v[ck][ci][cj] + 1

    return -1

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    N, M = map(int, input().rstrip().split())
    MAP = [list(map(int, input().rstrip())) for _ in range(N)]

    # [1] BFS
    v = [[[0] * M for _ in range(N)] for _ in range(2)]
    answ = bfs((0,0,0))

    print(answ)



'''
    여기서 not v[ck][ni][nj] 부분이 문제입니다.
        상황: 벽(MAP이 1)을 부수려고 합니다.
        논리: ck=0인 상태(벽을 안 부순 상태)에서는 벽을 밟을 수가 없습니다. 
            즉, 벽이 있는 좌표의 v[0][ni][nj]는 언제나 0입니다.
        결과: 따라서 not v[ck][ni][nj]는 항상 True가 됩니다.
        
    이게 무슨 뜻이냐고요?
    벽을 부수는 경우에 한해서는 **"방문 체크를 아예 안 하는 것"**과 똑같습니다.
    
    2. 시뮬레이션: 왜 위험한가요?만약 여러 경로가 하나의 벽으로 모이는 상황을 상상해 보세요.
        경로 A가 벽 X에 도착했습니다. 
        v[0]을 확인하니 0이라서 큐에 넣습니다. (정상)
        경로 B가 벽 X에 조금 늦게 도착했습니다.
        정상적인 로직: "어? 이미 누가 벽 부수고(v[1]) 찜했네?" 하고 무시해야 합니다.
        현재 코드 로직: 
        elif in_range(ni,nj) and not v[ck][ni][nj] and MAP[ni][nj] and ck == 0: 
        v[0]을 확인합니다. 여전히 0입니다. 
        "아싸, 내가 처음이다!" 하고 큐에 또 넣습니다.
        경로 C, D, E... 가 도착할 때마다 계속 큐에 중복해서 넣습니다.
        
    결론: elif in_range(ni,nj) and not v[ck+1][ni][nj] and MAP[ni][nj] and ck == 0:
    v[ck+1]에서의 방문 여부를 체크해라.

'''