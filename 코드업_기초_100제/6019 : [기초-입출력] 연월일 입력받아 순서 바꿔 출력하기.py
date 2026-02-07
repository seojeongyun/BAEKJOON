'''
"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.
'''

splited_input = input().split('.')
print(splited_input)
y, m, d = splited_input[0], splited_input[1], splited_input[-1]
print(y + '-' + m + '-' + d)