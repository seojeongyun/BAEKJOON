'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120885
    [1] bin 함수: 정수를 2진수 문자열로 변환
'''


def solution(bin1, bin2):
    answer = []
    #
    bin1_lst = list(bin1)
    bin2_lst = list(bin2)
    #
    dec1 = 0
    dec2 = 0
    #
    for i in range(1, len(bin1_lst) + 1):
        if bin1_lst[i-1] == '1':
            dec1 += 2 ** (len(bin1_lst)-i)

    for i in range(1, len(bin2_lst) + 1):
        if bin2_lst[i-1] == '1':
            dec2 += 2 ** (len(bin2_lst)-i)

    dec = dec1 + dec2

    # dec to bin
    while True:
        answer.append(str(dec % 2))
        if dec == 0 or dec == 1:
            break
        dec = dec // 2

    return ''.join(answer[::-1])

print(solution("10", "11"))