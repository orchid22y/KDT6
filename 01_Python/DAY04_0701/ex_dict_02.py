#---------------------------------------------------------------------------------------------------
# Dict 자료형 살펴보기
#   - 여러가지 데이터를 dict 타입으로 저장
#---------------------------------------------------------------------------------------------------
#[다양한 종류의 키]----------------------------------------------------------------------------------
##  - 키가 여러개 정보 합쳐서 사용하는 경우 => tuple타입
##  - 예) 홍길동 1996, 홍길동 2000
'''
person={'age':20,['홍길동',2000]:100}
>> TypeError: unhashable type: 'list'
'''

person={'age':20,('홍길동',2000):100}

## 3명의 정보를 저장
p1={'name':'홍길동', 'age':20, 'job':'학생'}
p2={'name':'마징가', 'age':100, 'job':'영웅'}
p3={'name':'배트맨', 'age':98, 'job':'박쥐'}
p4={'name':'홍길동', 'age':11, 'job':'학생'}

persons=[p1, p2, p3, p4]
persons[0]['name']

#   -키 : 나이데이터
persons2={20:{'name':'홍길동','job':'학생'},
          100:{'name':'마징가','job':'영웅'},
          98:{'name':'배트맨','job':'박쥐'},
          11:{'name':'홍길동','job':'학생'}}

print(persons2[11])
print()
#   -키 : 이름과 나이 데이터
persons3={('홍길동',20):{'job':'학생'},
          ('마징가',100):{'job':'영웅'},
          ("베트맨",98):{'job':'박쥐'},
          ('홍길동',11):{'job':'학생'}}

print(persons3[('홍길동',20)])
'''
{'job': '학생'}
'''