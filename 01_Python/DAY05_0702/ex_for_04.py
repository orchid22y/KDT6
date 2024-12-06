# # -----------------------------------------------------------------------------------------
# # [실습] 2단 ~ 9단까지 모두 출력하세요.

# 중첩 for문
for d in range(2,10):
    print(f"{'-'*5}{d}단{'-'*5}")
    for n in range(1,10):
        print(f'{d} * {n} = {d*n}')
    print()

# for문 1개만 사용
for d in range(20,100):
    if d%10==1:
        print(f"{'-'*5}{d//10}단{'-'*5}")
    if d%10:
        print(f'{(d//10)} * {(d%10)} ={(d//10)*(d%10)}')

# 

# for d in range(20,100):
#     if d%10==1:
#         print(f"{'-'*5}{d//10}단{'-'*5}",end = ' ')
#         if d//10==5:
#             print('\n')
    # if d%10:
    #     print(f'{(d//10)} * {(d%10)} = {(d//10)*(d%10)}')

    # for n in range(1,10):
    #     for d in range(2,10):
    #         print(f'{d} * {n} = {d*n:<3}',end=' ')
    


# 가로로 출력하기
# for n in range(0,10):
#     for d in range(2,6):
#         if n==0:
#             print(f"{'-'*4}{d}단{'-'*4}", end=' ')
#         else:
#             print(f'{d} * {n} = {d*n:<3}',end=" ")
#     print()
# for n in range(0,10):
#     for d in range(6,10):
#         if n==0:
#             print(f"{'-'*4}{d}단{'-'*4}", end=' ')
#         else:
#             print(f'{d} * {n} = {d*n:<3}',end=" ")
#     print()


for n in range(0,20):
    if n<10:
        for d in range(2,6):
            if n==0:
                print(f"{'-'*4}{d}단{'-'*4}", end=' ')
            else:
                print(f'{d} * {n} = {d*n:<3}',end=" ")
        print()
    else:
        n-=10
        for d in range(6,10):
            if n==0:
                print(f"{'-'*4}{d}단{'-'*4}", end=' ')
            else:
                print(f'{d} * {n} = {d*n:<3}',end=" ")
        print()

