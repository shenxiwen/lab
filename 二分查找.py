#!/usr/bin/env python
data=[1,2,3,4,5,6,7,8,9,10]
#data = range(1,1000)
def binary_find(datas,num):
    print(datas)
    if len(datas) > 0 :
        i=len(datas)//2
       # print(i)
        if datas[i] == num:
            print('find the num ',num,i)
        elif datas[i] > num:

            binary_find(datas[0:i],num)
        else:

            binary_find(datas[i+1:],num)
    else:
        print('not find')

#binary_find(data,10)


def finds(datas,num):
    m=0
    n=len(datas)
    while True:
        s = (n - m) // 2 + m
        if datas[s] == num:
            print('find ', num)
            break
        elif datas[s] > num :
            n = s
        else:
            m = s
        if s == 0 or s == len(datas)-1:
            print('cannot find the num ',num)
            break



for i in range(0,12):
    finds(data, i)