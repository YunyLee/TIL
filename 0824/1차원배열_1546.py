import sys
sys.stdin = open('input_1546.txt', 'r')

# 백준 단계별 풀이 - 1차원 배열 - 1546 문제
# 평균을 조작하는 문제

N = int(input())
N_LIST = list(map(int, input().split()))

max_score = max(N_LIST)
result = 0

for i in N_LIST:
    result += i/max_score * 100

print(result/len(N_LIST))