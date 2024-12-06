subject=['kor','eng','math','sci']
jumsu=list(map(int,input("").split()))
jsum=0
for j in range(0,len(jumsu)):
    if 0<=jumsu[j]<=100:
       jsum=jsum+jumsu[j]
    else:
       print("잘못된 점수 입니다.")
    avg=jsum/len(jumsu)

data=list(zip(subject,jumsu))

if avg>=80:
    print(f"{data}, 평균 : {avg} 합격입니다.")
else:
    print(f"{data}, 평균 : {avg} 불합격입니다.")