def rotate(arr):
    rot_arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rot_arr[i][j] = arr[N-1-j][i]
    return rot_arr

if __name__ == '__main__':
    T = int(input())
    for i in range(1, T+1):
        N = int(input())
        arr = [list(map(int, input().split())) for _ in range(N)]
        rot_arr = [row[:] for row in arr]
        rot_arr_90 = rotate(rot_arr)

        rot_arr = [row[:] for row in arr]
        for _ in range(2):
            rot_arr = rotate(rot_arr)
            rot_arr_180 = rot_arr

        rot_arr = [row[:] for row in arr]
        for _ in range(3):
            rot_arr = rotate(rot_arr)
            rot_arr_270 = rot_arr

        print(f'#{i}')
        for a,b,c in zip(rot_arr_90, rot_arr_180, rot_arr_270):
            print(''.join(map(str,a)), ''.join(map(str,b)), ''.join(map(str,c)))
        # for i in range(N):
        #     print(rot_arr_90[i], rot_arr_180[i], rot_arr_270[i])