'''
    https://www.acmicpc.net/workbook/view/12220

    1 / 128

    잔돈
        500
        100
        50
        10
        5
        1

    동전 개수가 가장 적게 잔돈을 준다.

    잔돈 동전의 개수를 구하시오.

    입력:
        지불할 돈

    출력:
        잔돈 동전 개수
'''

import sys

def divide(money, divisor):
    return money // divisor, money % divisor

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = 0
    # [0] 입력
    money = int(input().strip())
    money = 1000 - money
    # 그리디
    # [1] 500으로 나누었을 때 몫이 발생하는가 ?
    quotient, remainder = divide(money, 500)
    answ += quotient

    # [2] 100으로 나누었을 때 몫이 발생하는가 ?
    quotient, remainder = divide(remainder, 100)
    answ += quotient

    # [3] 50으로 나누었을 때 몫이 발생하는가 ?
    quotient, remainder = divide(remainder, 50)
    answ += quotient

    # [4] 10으로 나누었을 때 몫이 발생하는가 ?
    quotient, remainder = divide(remainder, 10)
    answ += quotient

    # [5] 5로 나누었을 때 몫이 발생하는가 ?
    quotient, remainder = divide(remainder, 5)
    answ += quotient+remainder

    #
    changes = [500, 100, 50, 10, 5, 1]
    for change in changes:
        answ += money // change
        money = money % change

    print(answ)
