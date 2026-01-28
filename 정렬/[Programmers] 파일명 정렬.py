'''
    파일명에 포함된 '숫자'를 반영한 정렬 기능 구현
        파일명 100글자 이내, 영문자 시작, 숫자 하나 이상 포함
            - 영문 대소문자
            - 숫자
            - 공백(" ")
            - 마침표(".")
            - 빼기 부호("-")

        - HEAD
            숫자가 아닌 문자로 이루어지며 최소 한글자 이상

        - NUMBER
            한 글자에서 최대 다섯 글자 사이의 연속된 숫자
            0부터 99999 사이의 숫자
            00000이나 0101등도 가능

        - TAIL
            그 외 나머지 부분
            숫자가 다시 나타날 수도 있고 아무 글자도 없을 수 있다.

    정렬
        HEAD를 기준으로 사전 순 정렬
            문자열 비교시 대소문자 구분 X

        HEAD가 같은 경우 NUMBER의 숫자로 정렬
            9 < 10 < 0011 < 012 ..
            012와 12는 같은 값으로 처리

        HEAD와 NUMBER가 같은 경우 원래 입력에 주어진 순서 유지
            MUZI01.zip과 muzi1.png가 들어오면 정렬 후에도 순서 보존


    입력:
        배열 files
'''

import sys

def head_ext(file:str):
    for i, ch in enumerate(file):
        if ch.isdigit():
            return file[:i], i

# tail에서 또 숫자가 등장하는 경우 문제 발생, tail이 없는 경우
def number_ext(file:str, number_start:int):
    cnt = 0
    NO_TAIL = True
    for i, ch in enumerate(file[number_start:]):
        if cnt == 5 or not ch.isdigit():
            NO_TAIL = False
            break
        cnt += 1
    number_end = i + number_start if not NO_TAIL else i + number_start + 1
    return file[number_start:number_end], number_end

def tail_ext(file:str, tail_start) -> str:
    return file[tail_start:]

def split_filename(file:str) -> list:
    head, number_start = head_ext(file)
    number, tail_start = number_ext(file,number_start)
    tail = tail_ext(file, tail_start)

    return [head, number, tail]

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    input_data = input().rstrip()[1:-1].strip().split(',')

    files = []
    answ = []
    for file in input_data:
        files.append(file.strip()[1:-1])

    # [1] HEAD, NUMBER, TAIL로 분류
    for file in files:
        answ.append(split_filename(file))

    # [2] Sorting
    answ.sort(key=lambda x: (x[0].lower(), int(x[1])))

    for head, number, tail in answ:
        file = ''.join([head, number, tail])
        print(file)


'''
    isnumeric()
    
    ["img12", "abc12.123.txt.png", "boe1233333.txt", "img12.ver2.zip"]
'''