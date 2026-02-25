'''
    https://www.acmicpc.net/problem/11501

    5 / 256

    세 가지 중 하나의 행동을 한다.
        1. 주식 하나를 산다.
        2. 원하는 만큼 가지고 있는 주식을 판다.
        3. 아무것도 안한다.

    날 별로 주식의 가격을 알때 최대 이익을 구하시오.
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = []

    # [0] TC 입력
    TC = int(input().strip())

    for _ in range(TC):
        tc_answ = 0

        # [1] 데이터 입력
        N = int(input().strip())
        price = list(map(int, input().strip().split()))

        max_price = 0
        for i in range(len(price)-1, -1, -1):
            if price[i] > max_price:
                max_price = price[i]

            tc_answ+=(max_price-price[i])

        answ.append(tc_answ)

    for answer in answ:
        print(answer)