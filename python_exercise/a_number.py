# 自己实现：列出1~100之间的所有质数

#质数定义：只能被1和本身整除

'''for n in range(2,100):
    if n == 2:
        print(n)
    else:
        for i in range(2,n):
            if (n % i) ==0:
                break
            else:
                print(n)  # 错误在此处
'''
#上面写法的错误在于，如果n = 97，i = 2、3、4 、5…… 都会将97打印一次

for n in range(2,100):
    if n == 2:
        print(n)
        continue # 根据python tutorial，if的else是optional的，可以忽略
    for i in range(2,n):
        if (n % i) == 0: # 如果n能除尽2~n中的任意一个数，即跳过该n，检验下一个n
            break
    else: # 因此，此处的else是for语句的
        print(n)