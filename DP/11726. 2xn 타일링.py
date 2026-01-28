'''
    2 x N 크기의 직사각형을 1 x 2, 2 x 1 타일로 채우는 방법의 수를 구하시오.
'''

# 재귀
def find_reculsive(K) -> int:
    if K == 1:
        return 1
    elif K == 2:
        return 2

    result = find_reculsive(K-1) + find_reculsive(K-2)
    return result

# DP: Top-down
def find_dp_T(K) -> int:
    if K == 1:
        return 1
    elif K == 2:
        return 2

    if K in DP_dict:
        return DP_dict[K]

    DP_dict[K] = find_dp_T(K-1) + find_dp_T(K-2)

    return DP_dict[K]


# DP: Bottom-up
def find_dp_B(K) -> int:
    for i in range(3, N+1):
        DP_list[i] = DP_list[i-1] + DP_list[i-2]

if __name__ == '__main__':
    # [0] input
    N = int(input())

    # [1] 재귀
    # print(find_reculsive(N) % 10007)

    # [2] DP: Top-down
    DP_dict = {}
    # print(find_dp_T(N) % 10007)

    # [3] DP: Bottom-up
    DP_list = [0] * (N+1)
    DP_list[1] = 1
    DP_list[2] = 2
    find_dp_B(N)
    print(DP_list[N] % 10007)