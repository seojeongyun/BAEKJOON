'''
    * 백트래킹으로 접근했었는데, 언제 매수-매도 했을 때 가장 높은 수익을 챙길 수 있느냐 !를 묻는 문제가 아니라서
    백트래킹으로 접근하는 것 보다 그냥 시뮬레이션으로 접근하는 게 맞는듯.
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    SEED = int(input().rstrip())
    PRICE = list(map(int, input().rstrip().split()))

    BNP_SEED = TIMING_SEED = SEED

    BNP_ANSW = 0
    TIMING_ANSW = 0
    #
    BNP_BUY_NUM = 0
    TIMING_BUY_NUM = 0
    #
    # for루프로 1일부터 14일까지
    for i in range(14):
        # BNP 매매
        if BNP_SEED >= PRICE[i]:
            BNP_BUY_NUM = BNP_SEED // PRICE[i]
            BNP_SEED -= BNP_BUY_NUM * PRICE[i]
            BNP_ANSW += BNP_BUY_NUM

        # TIMING 매수
        if i >= 3 and PRICE[i-3] > PRICE[i-2] > PRICE[i-1] and TIMING_SEED >= PRICE[i]:
            TIMING_BUY_NUM = TIMING_SEED // PRICE[i]
            TIMING_SEED -= TIMING_BUY_NUM * PRICE[i]
            TIMING_ANSW += TIMING_BUY_NUM

        # TIMING 매도
        if i >= 3 and PRICE[i-3] < PRICE[i-2] < PRICE[i-1]:
            TIMING_SELL_NUM = TIMING_ANSW
            TIMING_SEED += TIMING_SELL_NUM * PRICE[i]
            TIMING_ANSW = 0

    BNP_VAL = BNP_SEED + PRICE[13] * BNP_ANSW
    TIMING_VAL = TIMING_SEED + PRICE[13] * TIMING_ANSW

    if BNP_VAL > TIMING_VAL:
        print('BNP')
    elif TIMING_VAL > BNP_VAL:
        print('TIMING')
    else:
        print('SAMESAME')