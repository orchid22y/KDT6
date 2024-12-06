## [1] outer = 5, inner=5
for i in range(5):
    for j in range(5):
        print(f'j:{j}',end=' ')
    print(f'i:{i}\\n')
    
print()

## [2] 대각선 * 출력------------------------------------------------------------
# *
#  *
#   *
#    *
#     *

for v in range(5):
    for h in range(v+1):
        # if h==v:
        #     print("*",end='')
        #     print()
        # else : 
        #     print(" ",end='')
        print('*' if h==v else ' ', end='\n' if h==v else' ')
        
for i in range(5):
    for j in range(5):
        if j>=i:
            print("*",end='')
        else:
            print(' ',end='')
    print()


height=int(input("높이"))

