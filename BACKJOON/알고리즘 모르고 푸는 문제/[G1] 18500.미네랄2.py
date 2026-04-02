'''
    https://www.acmicpc.net/problem/18500

    1 / 512

    동굴에서 두 사람이 막대기를 던진다. 던진 막대기가 미네랄을 파괴할 수도 있따.

    동굴: R x C
        - 각 칸은 비어있거나 미네랄을 포함하고 있으며, 네 방향 중 하나로 인접한 미네랄이 포함된 두 칸은 같은 클러스터

    턴
        - 번갈아가며 막대기를 던진다.
            - 던지기 전에 던질 높이를 정해야하고, 막대기는 땅과 수평을 이루어 날아감
            - 날아가다가 미네랄을 만나면, 그 칸에 있는 미네랄은 모두 파괴되고 막대는 이동을 멈춤
                - 파괴된 이후 남은 클러스터가 분리될 수 있다.
                    - 새롭게 생성된 클러스터가 떠있는 경우에는 중력에 의해 바닥으로 떨어지게 됨
                        - 떨어지는 동안 클러스터 모양은 변하지 않는다
                        - 다른 클러스터나 땅을 만나기 전까지 계속 떨어짐
                        - 다른 클러스터 위에 떨어질 수 있고 그 이후에는 합쳐짐

    입력: 동굴에 있는 미네랄의 모양과 두 사람이 던진 막대의 높이가 주어진다
    출력: 모든 막대를 던지고 난 이후의 미네랄 모양을 구하시오.
'''

import sys

from collections import deque

def show(arr):
    for row in arr:
        print(*row)

def in_range(i, j):
    return 0 <= i < R and 0 <= j < C

def bfs(start):
    coord_lst = []
    coord_lst.append(start)
    #
    i, j = start
    visited = [[0] * C for _ in range(R)]
    visited[i][j] = 1
    #
    q = deque()
    q.append((i,j))

    while q:
        ci, cj = q.popleft()
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)): # 4방향
            ni, nj = ci+di, cj+dj
            # 범위 내, 미방문, 조건 만족('x')
            if in_range(ni, nj) and not visited[ni][nj] and arr[ni][nj] == 'x':
                q.append((ni, nj))
                visited[ni][nj] = 1
                coord_lst.append((ni, nj))

    return coord_lst

def drop(j, i):
    # 깨진 지점에서 우,좌 한 칸 탐색
    # 발견시 그 방향으로 쭉 탐색하며 아래 방향에 연결된 미네랄 있는지 탐색
    # 아래로 연결된 미네랄 없으면 BFS 통해서 미네랄 클러스터 좌표 획득
    # 해당 좌표 값 '.'으로 덮어 쓴 후
    # 좌표에서 y+gap에 'x' 덮어쓰기 (gap은 y좌표가 제일 큰 것들 밑으로 내리면서 얼마나 내려질 수 있는지 탐색)
    cluster = []
    #
    for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
        ni, nj = i+di, j+dj
        if 0 <= ni < R and 0 <= nj < C:
            if arr[ni][nj] == 'x':
                coord = bfs((ni, nj))
                coord.sort(key=lambda x: (-x[0], -x[1]))
                if coord[0][0] != R - 1 and coord not in cluster:
                    cluster.append(coord)


    # 클러스터가 내려 앉는 거라서 모두 동일한 좌표만큼 이동해야 함
    if len(cluster) > 0:
        for coord in cluster:
            min_val = sys.maxsize
            for i, j in coord:
                arr[i][j] = '.'
                ni = i
                while ni < R and arr[ni][j] == '.':
                    ni += 1
                min_val = min(min_val, ni-i-1)

            for i, j in coord:
                arr[i+min_val][j] = 'x'
    else:
        return


def throw(dir, height):
    height = R-height

    if dir == 0:
        for idx in range(len(arr[height])):
            char = arr[height][idx]
            if char == 'x':
                arr[height][idx] = '.'
                drop(idx, height)
                return
    else:
        for idx in range(len(arr[height])-1, -1, -1):
            char = arr[height][idx]
            if char == 'x':
                arr[height][idx] = '.'
                drop(idx, height)
                return

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    R, C = map(int, input().strip().split())
    arr = [list(input().strip()) for _ in range(R)]
    N = int(input().strip())
    H = list(map(int, input().strip().split()))

    for turn, height in enumerate(H):
        # turn에 따라서 왼쪽 시작, 오른쪽 시작을 결정 (0: 왼 / 1: 오)
        if turn % 2 == 0:
            dir = 0
        else:
            dir = 1

        throw(dir, height)

    for row in arr:
        print(''.join(row))

'''
TC1
5 6
xxxxxx
x...xx
...xx.
..xx..
...x..
1
1    


TC2
5 5
xxx..
x....
xxxx.
...x.
xxxxx
2
4 2

TC3
7 7
....xx.
....xxx
xxxxx..
...xxxx
xxxxxx.
....xxx
xxxxxx.
3
7 5 2

TC4
14 11
xxxxxxxxxxx
x.x.x.x.x.x
x.x.x.x.x.x
x.x.x.x.x.x
x...x.x.x.x
x.....x...x
x.....x....
x..........
x.........x
x.........x
xxxxxxxxxxx
.....x.....
.....x.....
.....x.....
2
4 2

TC5 from GPT
2 2
.x
..
1
2

TC6 
3 3
xxx
x.x
..x
1
3

TC6
4 4
...x
..xx
.xxx
xxxx
10
1 2 3 4 1 2 3 4 3 4

TC 7
10 10
xxxxxxxxxx
....x.....
...xxx....
.....x....
....xx....
.....x....
xxxxxx....
..x.......
.xxxx.....
...xxxxxxx
10
9 8 7 6 5 4 3 2 1 1

정답

..........
..........
..........
..........
..........
..........
xxxxxxxxxx
....xx....
xxxxxx....
.xxxxxxxx.
'''