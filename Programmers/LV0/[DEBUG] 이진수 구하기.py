'''

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
    for i in range(len(bin1_lst)-1, -1, -1):
        if bin1_lst[i] == '1':
            dec1 += 2 ** (len(bin1_lst)-i)

    for i in range(len(bin2_lst)-1, -1, -1):
        if bin2_lst[i] == '1':
            dec2 += 2 ** (len(bin1_lst)-i)

    dec = dec1 + dec2

    # dec to bin
    while dec > 1:
        answer.append(dec % 2)
        dec = dec // 2

    return str(answer)

solution("10", "11")