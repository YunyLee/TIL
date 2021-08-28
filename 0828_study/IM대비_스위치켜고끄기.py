import sys
sys.stdin = open('input_1244.txt', 'r')

# IM 대비 백준 1244 문제

SWITCH_NUM = int(input())
S_LIST = list(map(int,input().split()))
student_num = int(input())

for i in range(student_num):
    gender, number = map(int,input().split())

    # 맨 처음 남학생의 경우부터 출발한다. gender 1이고 받은 숫자는 3
    # 3을 받았으니까 그 배수인 3번과 6번을 change하면 된다.
    should_change_list = []

    # 남자인 경우
    if gender == 1:
        multiple_cnt = len(S_LIST)//number #2가 나온다. 내가 곱해줘야할 개수

        for i in range(1, multiple_cnt+1):
            should_change_list.append(i*number)

        for j in should_change_list:
            if S_LIST[j] == 0:
                S_LIST[j] = 1
            else:
                S_LIST[j] = 0

    # 여자인 경우
    if gender == 2:
        pass # 내일 다시 생각해볼것

result = ''
for i in range(1, SWITCH_NUM+1):
    if i == 21 or i == 41 or i == 61 or i == 81:
        print()
        result += str(S_LIST[i]) + ' '
        print(result, end = ' ')
    else:
        result += str(S_LIST[i]) + ' '
        print(result, end = ' ')
