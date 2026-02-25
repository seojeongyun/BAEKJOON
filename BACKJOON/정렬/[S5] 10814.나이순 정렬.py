'''
    사람들의 나이와 이름이 가입 순으로 주어진다
    나이 오름차순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오도록 정렬
'''

# * 정렬할 때 x[1](나이)를 str로 받은 채로 정렬 했는데, 이러면 2보다 10이 더 앞에 오게됨.
# '10' -> '2' 사전순 정렬
# 그래서 나이 반드시 int로 변환해주고 정렬해야함.

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input().rstrip())
    lst = [[i] + input().rstrip().split() for i in range(N)]

    sorted_lst = sorted(lst, key=lambda x: (int(x[1]), x[0]))

    for lst in sorted_lst:
        print(lst[1], lst[2])
