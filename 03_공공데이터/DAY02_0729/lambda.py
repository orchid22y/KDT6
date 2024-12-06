# key 매개변수 : 여러 항목을 가지는 리스트 정렬
#   - key 매개변수에 lambda 사용
#       - lanmbda 함수 : 다양한 정렬 기준을 설정

students=[('Alice',3.9,20160303),
          ('Bob',3.0,20160302),
          ('Charlie',4.3,20160301)]
print('-'*105)
print(sorted(students))
print('-'*105)

# 학번(students[2])을 기준으로 오름차순 정렬
sorted_students1=sorted(students,key=lambda s:s[2])
print('학번 기준 오름차순 정렬:',sorted_students1)

# 학점(students[1])을 기준으로 내림차순 정렬
sorted_students2=sorted(students,key= lambda s:s[1],reverse=True)
print('학점 기준 내림차순 정렬:',sorted_students2)