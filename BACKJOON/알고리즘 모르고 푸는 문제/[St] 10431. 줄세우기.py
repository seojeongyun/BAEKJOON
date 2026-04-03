'''
    https://www.acmicpc.net/problem/10431

    1 / 256

    키 순서대로 번호를 부여 (20명, 같은 키를 가진 학생 X)
        - 키가 가장 작은 아이가 1번
        - ...
        - 가장 큰 아이가 20번

    아무나 한 명 뽑아 맨 앞에 세운다.
    그 다음 부터는 한 명씩 줄의 맨 뒤에 서면서 다음 과정을 거친다
        - 자기 앞에 자기보다 큰 학생이 없다면 그냥 그 자리에 서고 차례가 끝난다.
        - 자기 앞에 자기보다 큰 학생이 한 명 이상 있다면 그 중 가장 앞에 있는 학생(A)의 바로 앞에 선다.
            - A부터 그 뒤의 모든 학생들은 공간을 만들기 위해 한 발 씩 물러선다

    이 과정을 반복하면 오름차순으로 줄을 설 수 있따.
    줄서기가 끝났을 때 학생들이 총 몇 번 뒤로 물러서게 될까?
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    answer = []
    # [0] TC 입력
    P = int(input().strip())

    for _ in range(P):
        DATA = list(map(int, input().strip().split()))
        TC_NUM = DATA[0]
        line = DATA[1:]
        #
        answ = sorted(line)

        try_num = 0
        # i, j = 0, 1
        # while line != answ:
        #     if line[i] > line[j]:
        #         try_num += 1
        #         line[i], line[j] = line[j], line[i]
        #     i += 1
        #     j += 1
        #     if i == 19 and j == 20:
        #         i, j = 0, 1

        for i in range(19):
            for j in range(i+1, 20):
                if line[i] > line[j]:
                    line[i], line[j] = line[j], line[i]
                    try_num += 1

        answer.append((TC_NUM, try_num))

    for answ in answer:
        print(*answ)


'''
P=int(input())
for _ in range(P):
    arr=list(map(int,input().split()))
    total=0
    for i in range(1,len(arr)-1):
        for j in range(i+1,len(arr)): # i 뒤에 애들과 전부 비교해서
            if arr[i] > arr[j]:  # i가 더 크면
                arr[i],arr[j] = arr[j],arr[i]  # 자리바꾸기
                total+=1
    print(arr[0], total)
'''