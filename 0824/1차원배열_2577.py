import sys
sys.stdin = open('input_2577.txt', 'r')

# 백준 단계별 풀이 - 1차원 배열 - 2577 문제
# 각 숫자가 몇 번 나왔는지 저장하기 위해 일차원 배열을 만드는 문제


N = 3
N_LIST = []
multiple_num = 1
multi_list = [0,0,0,0,0,0,0,0,0,0]

for i in range(N):
    NUM = int(input())
    N_LIST.append(NUM)

for i in range(N):
    multiple_num *= N_LIST[i]

for i in str(multiple_num):
    multi_list[int(i)] += 1

for i in multi_list:
    print(i)