'''
줄을 바꿔 문자(character) 2개를 입력받고, 순서를 바꿔 한 줄씩 출력해보자.
'''

a = list(input() for _ in range(2))
for i in range(2):
    print(a[-1-i])