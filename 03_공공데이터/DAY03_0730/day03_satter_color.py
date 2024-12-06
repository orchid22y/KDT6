#산점도에 color bar 추가하기

import matplotlib.pyplot as plt
y_value = [10,20,20,10]
x_value=[1,2,3,4]
size=[]

for y in y_value:
    size.append(y*5)

plt.scatter(x_value, y_value, s=size, c=range(4), cmap='jet')
plt.colorbar()
plt.show()
