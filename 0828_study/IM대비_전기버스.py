import sys
sys.stdin = open('input_4831.txt', 'r')

# SWea - Learn- Course - List1 - 전기버스(4831)

TC = int(input())

for test_case in range(1, TC+1):
    CAN_GO, N, CHARGER = map(int, input().split())
    CHARGE_NUM = list(map(int,input().split()))

    # 필요한 변수들 초기화 (현재위치, 카운트)
    current_pos = 0
    cnt = 0

    while current_pos + CAN_GO < N :
        for step in range(CAN_GO, 0, -1):
            if current_pos + step in CHARGE_NUM:
                current_pos += step
                cnt += 1
                break
        else:
            cnt = 0
            break

    print('#{} {}'.format(test_case, cnt))

        # 내 첫번째 접근 (list out of range로 실패)

        # for i in range(len(CHARGE_NUM)):
        #     if CHARGE_NUM[i] == bus_stop:
        #         cnt += CAN_GO
        #         charge_cnt += 1
        #         current_pos = i
        #         next_pos = current_pos+1
        # cnt -= 1
        # if CHARGE_NUM[next_pos] - CHARGE_NUM[current_pos] > cnt:
        #     charge_cnt = 0

        # print('#{} {}'.format(test_case, cnt))
