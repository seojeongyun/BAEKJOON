'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120866
    [1] 2차원 배열 깊은 복사: [row[:] for row in array]
'''


def print_arr(arr):
    for array in arr:
        print(*array)


def in_range(i, j, length):
    return 0 <= i < length and 0 <= j < length


def solution(board):
    answer = 0
    around = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    length = len(board[0])
    copy = [row[:] for row in board]
    print_arr(board)

    for i in range(length):
        for j in range(length):
            if board[i][j] == 1:
                for di, dj in around:
                    if in_range(i + di, j + dj, length):
                        copy[i + di][j + dj] = 1
    print('----------')
    print_arr(copy)
    for arr in copy:
        answer += (length - sum(arr))
    return answer