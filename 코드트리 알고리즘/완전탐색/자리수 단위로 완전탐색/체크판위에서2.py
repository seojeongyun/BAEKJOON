'''
    R×C 크기인 직사각형의 각 칸이  ′W′, ′B′ 로 표현되어 있습니다.
′W′ 는 하얀색으로, ′B′는 검은색으로 칸이 채워져 있는것을 뜻합니다.

왼쪽 상단에서 출발하여 우측 하단으로 이동할 때, 특정 룰을 만족하면서 이동에 성공할 수 있는 경우의 수를 구하는 프로그램을 작성해보세요. 아래가 특정 룰입니다.
    이동은 항상 점프를 통해서만 가능합니다. 또, 점프 진행시 항상 현재 위치에 적혀있는 색과, 점프한 이후의 칸에 적혀있는 색이 달라야만 합니다.
    점프 진행시 현재 위치에서 적어도 한칸 이상 오른쪽에 있는 위치이며 동시에 현재 위치에서 적어도 한칸 이상 아래쪽에 있는 위치인 곳으로만 점프가 가능합니다.
    정확히 시작, 도착 지점을 제외하고 점프하며 도달한 위치가 정확히 2곳 뿐이어야 합니다.

첫 번째 줄에 R, C가 공백을 사이에 두고 주어집니다.
R은 직사각형의 세로변, C는 가로변을 뜻합니다.

두 번째 줄부터 R개의 줄에 걸쳐 R x C 크기의 직사각형이 주어집니다.
각 줄에는 C개의 문자 'W' 또는 'B'가 공백으로 구분되어 주어집니다.

TC1
입력
5 5
W W W W W
W W W W W
W B W W W
W W W W W
W W W W B

출력
2
'''

# 격자: R x C
    # 각 칸이 'W', 'B'로 표현
        # 'W': 백
        # 'B': 흑

# 좌상단에서 우하단으로 이동
    # 이동: 서로 다른 색으로 점프
    # 이동 시, 적어도 한 칸 이상 오른쪽, 적어도 한 칸 이상 오른쪽 아래인 곳으로 점프
    # 시작, 도착 지점 제외하고 점프하며 도달한 위치가 정확히 2곳이어야 함

# 룰에 만족하면서 이동에 성공할 수 있는 경우의 수

import sys
input = sys.stdin.readline

def in_range(i, j):
    return 0 <= i < R and 0 <= j < C

R, C = map(int, input().strip().split())
GRID = [list(map(str, input().strip().split())) for _ in range(R)]
v = [[0] * C for _ in range(R)] # debug

si, sj = 0, 0
ei, ej = R-1, C-1

ckpt1 = []
ckpt2 = []
answer = 0

for i in range(R):
    for j in range(C):
        if GRID[si][sj] != GRID[i][j] and si < i and sj < j:
            ckpt1.append((i,j))

for ci, cj in ckpt1:
    for i in range(ci, R):
        for j in range(cj, C):
            if GRID[ci][cj] != GRID[i][j] and ci < i and cj < j:
                ckpt2.append((i,j))

for ci, cj in ckpt2:
    for i in range(ci, R):
        for j in range(cj, C):
            if GRID[ci][cj] != GRID[i][j] and ci < i and cj < j and i == R-1 and j == C-1:
                answer += 1

print(answer)


'''
[해설]

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
grid = [
    input().split()
    for _ in range(n)
]

# 이동 시에 행과 열이 전부 증가하도록
# 모든 쌍을 다 잡아봅니다.
cnt = 0
for i in range(1, n):
    for j in range(1, m):
        for k in range(i + 1, n - 1):
            for l in range(j + 1, m - 1):
                # 그 중 색깔이 전부 달라지는 경우에만 개수를 세줍니다.
                if grid[0][0] != grid[i][j] and \
                   grid[i][j] != grid[k][l] and \
                   grid[k][l] != grid[n - 1][m - 1]:
                    cnt += 1
                        
print(cnt)

k와 l의 시작범위가 각각 i+1, j+1이므로 우하단으로 점프하는 게 성립함.
'''