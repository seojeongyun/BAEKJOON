'''
    미국 전역의 나무들이 주어졌을 때, 각 종이 전체에서 몇 %를 차지하는지 구하시오.
'''

import sys
from collections import defaultdict

# 입력 개수가 정해져있지 않으면 while True: -> input이 ''이면 break
if __name__ == '__main__':
    # [0] 입력: 한 줄에 하나의 나무 종 이름
    input = sys.stdin.readline
    tree = {}
    cnt = 0
    #

    while True:
        data = input().rstrip()
        if data == '':
            break
        #
        cnt += 1 # 나무 개수 카운트
        tree.setdefault(data, 0) # key: 나무 종류
        tree[data] += 1          # value : 개수

    sorted_tree = dict(sorted(tree.items()))

    for k, v in sorted_tree.items():
        print(f"{k} {v / cnt * 100:.4f}")

