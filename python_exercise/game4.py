# 输出9*9乘法口诀表


for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(j,i,i*j), end = ' ')
        if j == i :
            print('\n')