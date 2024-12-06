
print("1.for문 1개만 사용해서 구구단 출력\n")

for d in range(20,100):
    if d%10==1:
        print(f"{'-'*5}{d//10}단{'-'*5}")
    if d%10:
        print(f'{(d//10)} * {(d%10)} ={(d//10)*(d%10)}')

print()

print("2. 구구단 가로로 출력(for문 4개)\n")
for n in range(0,10):
    for d in range(2,6):
        if n==0:
            print(f"{'-'*4}{d}단{'-'*4}", end=' ')
        else:
            print(f'{d} * {n} = {d*n:<3}',end=" ")
    print()
for n in range(0,10):
    for d in range(6,10):
        if n==0:
            print(f"{'-'*4}{d}단{'-'*4}", end=' ')
        else:
            print(f'{d} * {n} = {d*n:<3}',end=" ")
    print()

print() 
print('2.구구단 가로로 출력하기(for문 2개)\n') 

for n in range(0,20):
    for d in range(2,10):
        if n<10 and d<6:
            if n==0:
                print(f"{'-'*4}{d}단{'-'*4}", end=' ')
            else:
                print(f'{d} * {n} = {d*n:<3}',end=" ")
        if n>=10 and d>5:
            c=n-10
            if c==0:
                print(f"{'-'*4}{d}단{'-'*4}", end=' ')
            else:
                print(f'{d} * {c} = {d*c:<3}',end=" ")
    print()

