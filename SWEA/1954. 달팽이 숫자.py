if __name__ == '__main__':
    T = int(input())
    for TC in range(T):
        N = int(input())
        arr = [[0] * N for _ in range(N)]

        x, y = 0,0
        dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
        dir = 1
        cnt = 1
        arr[y][x] = cnt
        cnt += 1

        while True:
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < N and 0 <= ny < N and arr[ny][nx] == 0:
                x, y = nx, ny
                arr[y][x] = cnt
                cnt += 1

            else:
                dir = (dir + 1) % 4

            if cnt == N * N + 1: break

        print(f'#{TC+1}')
        for i in range (N):
            print(*arr[i])
