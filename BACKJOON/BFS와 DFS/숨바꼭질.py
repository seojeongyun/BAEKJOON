'''
수빈 위치: N
    - 0 <= N <= 100,000

동생 위치: K
    - 0 <= K <= 100,000

수빈의 위치가 X일 때
    - 걷는다면
        - 1초후 X - 1 또는 X + 1로 이동
    - 순간이동
        - 1초 후 2 * X로 이동
수빈이가 동생을 찾을 수 있는 가장 빠른 시간
'''

def is_in_range(N):
    return 0 <= N <= 100000

def BFS(start, end):
    Q = []
    Q.append(start)
    visited[start] = 1
    while Q:
        start = Q.pop(0)
        if start == end:
            return visited[end]

        for next in (start-1, start+1, start*2):
            if is_in_range(next):
                if visited[next] == 0:
                    visited[next] = visited[start] + 1
                    Q.append(next)

if __name__ == '__main__':
    N, K = tuple(map(int, input().split()))
    # N에서 K를 만드는 경우의 수 찾기
    visited = [0] * 300000
    start = N
    end = K
    time = BFS(start=N, end=K)
    print(time - 1)

