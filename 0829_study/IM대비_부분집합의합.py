import sys
sys.stdin = open('input_4837.txt', 'r')

# SWEA - Learn- Course - List2 - 부분집합의 합(4837)
# 너무어렵당...

TC = int(input())
A = list(range(1,13))
lst = []

#부분집합 구하기
for i in range(1 << len(A)):
    sub_lst = []
    for j in range(len(A)):
        if i & (1 << j):
            sub_lst.append(A[j])
    lst.append(sub_lst)

for test_case in range(1, TC+1):
    N, K = map(int,input().split())
    result = 0
    cnt = 0

    # 길이 맞는 리스트 구하기
    len_lst = []
    for i in lst:
        if len(i) == N:
            len_lst.append(i)

    for i in len_lst:
        if sum(i) == K:
            result += 1

    print('#{} {}'.format(test_case, result))