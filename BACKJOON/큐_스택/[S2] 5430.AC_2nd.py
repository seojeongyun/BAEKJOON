'''
    함수 R:
        - 배열에 있는 수의 순서를 뒤집는 함수
    함수 D:
        - 첫 번째 수를 버리는 함수
        - 비어있는데 D를 사용하면 에러 발생
'''

import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = []

    # [0] 입력
    TC = int(input().rstrip())

    for _ in range(TC):
        GO_TO_NEXT = False
        REVERSE = False
        #
        FUNC = input().rstrip()
        NUM = int(input().rstrip())
        DATA = input().rstrip()[1:-1].split(',')
        LST = []

        # [1-1] 배열에 어떤 숫자가 들어 있으면
        if NUM > 0:
            for data in DATA:
                LST.append(int(data))

        # [1-2] 배열에 아무 숫자도 들어있지 않으면
        else:
            LST = []

        DQ = deque(LST)

        # [2] 함수 처리
        for function in FUNC:
            # [2-1] 함수 D 처리
            if function == 'D':
                # [2-1-1] DQ에 원소가 들어있는 경우 0번 인덱스 pop
                if len(DQ) > 0:
                    if REVERSE: DQ.pop()
                    else: DQ.popleft()
                # [2-1-2] DQ에 아무 원소도 없는 경우 error 발생
                else:
                    GO_TO_NEXT = True
                    answ.append('error')
                    break

            # [2-2] 함수 R 처리
            else:
                REVERSE ^= 1

        # if not GO_TO_NEXT:
        #     if REVERSE: DQ.reverse()
        #     answ.append(list(DQ))

        if not GO_TO_NEXT:
            start, end = '[', ']'
            output = []
            if REVERSE:
                for i in range(len(DQ)-1, -1, -1):
                    output.append(str(DQ[i]))
                output = ','.join(output)
                str_ = start + output + end

            else:
                for i in DQ:
                    output.append(str(i))
                output = ','.join(output)
                str_ = start + output + end

            answ.append(str_)

    for answer in answ:
        print(answer)
