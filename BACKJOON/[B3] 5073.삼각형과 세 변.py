'''
    Equilateral :  세 변의 길이가 모두 같은 경우
    Isosceles : 두 변의 길이만 같은 경우
    Scalene : 세 변의 길이가 모두 다른 경우

    주어진 세 변의 길이가 조건을 만족하지 못하면 "Invalid" 출력

    세 변의 길이가 주어질 때 위 정의에 다른 결과 출력
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = []

    while True:
        data = list(map(int, input().strip().split()))
        if sum(data) == 0:
            break

        if max(data) >= sum(data) - max(data):
            answ.append("Invalid")

        elif data[0] == data[1] == data[2]:
            answ.append("Equilateral")

        elif data[0] == data[1] or data[0] == data[2] or data[1] == data[2]:
            answ.append("Isosceles")

        elif data[0] != data[1] != data[2]:
            answ.append("Scalene")

    for answer in answ:
        print(answer)
