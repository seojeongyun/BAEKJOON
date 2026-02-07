'''
    AC는 정수 배열에 연산을 하기 위해 만든 언어
        - R(뒤집기)
            - 배열에 있는 수의 순서를 뒤집음
        - D(버리기)
            - 첫 번째 수를 버림
            - 배열이 비어있을 경우 에러 발생

    함수는 조합해서 한 번에 사용
        - 'RDD'는 뒤집고 처음 두 수를 버리는 함수

    출력 : 배열의 최종 결과
'''
from collections import deque

# [알고리즘]
# D가 들어왔을 때, 0번째 인덱스의 값을 버리는 것이므로, 덱의 popleft 사용
# R이 들어왔을 때, 배열을 뒤집는 것 보다 popleft를 사용할 건지, pop을 사용할 건지 정하는 게 시간 효율 좋다 판단
# Reverse 여부를 판단해, 뒤에서부터 프린트

# [시간 복잡도]
# 테스트케이스 하나에 대해,
# 입력 P의 length에 의해, 남아있는 DQ의 length에 의해 (== 입력 DATA의 length - D의 개수) 선형적으로 증가, O(N)
if __name__ == '__main__':
    answ = []
    # [0] 입력
    # [0-1] 테스트케이스
    T = int(input())
    for _ in range(T):
        DQ = deque()
        reverse = False
        GO_next = False
        # [0-2] 수행할 함수 p
        P = input()
        # [0-3] 배열에 들어있는 수의 개수 n
        N = int(input())
        # [0-4] 배열에 들어있는 정수 ([1,2,3,4] 형태로 제공 리스트 X 문자열 O)
        DATA = input()

        if N > 0:
            if ',' in DATA[1:-1]:
                for num in DATA[1:-1].split(','):
                    DQ.append(int(num))

            else:
                DQ.append(int(DATA[1:-1]))

        else:
            pass

        # [1] 함수 실행
        # [1-1] for func in p:
        for func in P:
            # [1-2] if R: 뒤집기, 제거 방향만 정해주면 됨. popleft or pop
            if func == 'R':
                if reverse:
                    reverse = False
                else:
                    reverse = True

            # [1-3] else: try DQ.popleft() except: print(error)
            else:
                try:
                    if reverse: DQ.pop()
                    else: DQ.popleft()

                except:
                    GO_next = True
                    answ.append('error')
                    break

        if not GO_next:
            start, end = '[', ']'
            output = []
            if reverse:
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
