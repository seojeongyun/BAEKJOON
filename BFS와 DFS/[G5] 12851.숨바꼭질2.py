'''
    수빈이의 위치  N
    동생의 위치 K

    수빈의 이동(위치 N일 때)
        - 걸음
            - X+1 혹은 X-1
        - 순간이동
            - 2 * X
'''
import sys
from collections import deque

def in_range(pos):
    return 0 <= pos <= 100000

def BFS(start):
    DQ = deque()
    DQ.append(start)
    visited[start] = 1
    #
    time = -1
    find_cnt = 0
    #
    while DQ:
        now = DQ.popleft()
        # 동생을 찾은 경우
        if now == K:
            time = visited[now]
            find_cnt += 1
        # 세 방향, 범위 내, 미방문이거나, 방문했어도 현재 시간보다 더 많거나 같다면 현재 시간으로 업데이트
        for n_pos in ([now+1, now-1, now*2]):
            if in_range(n_pos) and visited[n_pos] == 0 or visited[n_pos] >= visited[now] + 1:
                DQ.append(n_pos)
                visited[n_pos] = visited[now] + 1

    return time-1, find_cnt

if __name__ == '__main__':
    # [0] N, K 입력
    input = sys.stdin.readline
    N, K = map(int, input().rstrip().split())

    # [1] BFS로 최단 시간 탐색
    visited = [0] * 200000 + [0] # 200,000개 배열 -> N=100,000에서 순간이동하는 순간고려
    start = N
    time, find_cnt = BFS(start)

    print(time)
    print(find_cnt)
    # print(visited)