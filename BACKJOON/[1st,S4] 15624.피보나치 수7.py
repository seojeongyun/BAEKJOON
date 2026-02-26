'''

'''

import sys

def fibo(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = b% 1000000007, a+b% 1000000007

    return b
if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    N = int(input().strip())

    answ = fibo(N-1)

    print(answ)