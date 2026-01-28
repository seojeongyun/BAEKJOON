'''
    N개의 문자열로 이루어진 집합 S (set 사용)
    M개의 문자열 중에 S에 포함되어있는 것이 몇 개인지 구하시오.
'''


'''
    교집합으로 풀면 왜 틀리지 ? 를 생각해봤는데
    M개 문자열 중에 중복되어 들어오는 게 있을 수 있는데
    이를 set으로 덮어버리면 중복이 제거되어버려서 틀림
'''

# sys.stdin.readline으로 입력을 받으면 rstrip()을 하자.

import sys

if __name__ == '__main__':
    # [0] 입력
    input = sys.stdin.readline

    N, M = map(int, input().rstrip().split())
    set_A = {input().rstrip() for _ in range(N)}

    cnt  = 0
    for _ in range(M):
        if input().rstrip() in set_A:
            cnt += 1

    print(cnt)

