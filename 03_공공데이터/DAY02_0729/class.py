# 객체 리스트의 정렬 기준 설정
#   - Student 객체의  name 값을 기준으로 리스트를 오름차순 정렬

class Student:
    def __init__(self,name, grade,number):
        self.name=name
        self.grade=grade
        self.number=number

    def __repr__(self):     # 객체를 문자열로 표현하는 함수
        return f'({self.name},{self.grade},{self.number})'
    
# Student 객체 리스트 생성
students=[Student('홍길동',3.9,20240303),
          Student('김유신',3.0,20240302),
          Student('박문수',4.3,20240301)]

print(students[0])  #객체 출력
print( '-'*100)
print('Student객체의 name을 기준으로 정렬')
sorted_list=sorted(students,key=lambda s:s.name)
print(sorted_list)