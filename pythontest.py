# from random import randint
# trg = randint(0,10)
# flag = 0
# while flag == 0:
#     x = int(input("请输入猜测的数:"))
#     if x == trg:
#         print("猜对了")
#         flag = 1
#     elif x<trg:
#         print('猜小了')
#     else:
#       print('猜大了')

# i = 1
# while True:
#     i += i
#     if i>10:
#         break
# print('i={}'.format(i))    

# from math import sqrt
# j = 2
# while j <= 100:
#     k = sqrt(j)
#     i = 2
#     while i <= k:
#         if j % i == 0:
#             break
#         i += 1
#     if i> k:
#         print(j,end=" ")
#     j += 1

# i = 1
# while i < 3:
#     i += 1
#     if i == 2:
#         print('stop')
#         break
# else:
#     print(i)
#     print('over')

# def add(x):
# # docString  函数功能解释
#   '为了进行相加运算'
#   return x+x

# print(add.__doc__)
# print(add(3))

# from math import sqrt
# def isPrime(x):
#     '用于验证是否为素数'
#     # 需要使用int函数，以为sqrt(x)开根号出来为小数，也就是浮点数
#     k = int(sqrt(x))
#     for i in range(2,k+1):
#         if x%i == 0:
#             return 0
#     return 1

# for j in range(2,101):
#     if isPrime(j):
#         print(j,end=" ")

# def add(a):
#     return a+a
# def self(f,y):
#     print(f(y))
# self(add,3)

# r = lambda x,y:x+y
# print(r(5,8))

# def F(n):
#     a,b = 1,1
#     count = 2
#     while n>count:
#         a,b = b,a+b
#         count+=1
#     return b

# print(F(6))

# def fib(n):
#     # 写递归函数的时候注意，一定要有递归出口
#     if n == 0 or n == 1:
#         return n
#     else:
#         # 在写递归的时候，一定要是比原来的n小，不能是f(n)-f(n)
#         return fib(n-1)+fib(n-2)
# print(fib(6))

# def add(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return add(n-1)+add(n-2)
# print(add(3))

# a = 5
# def f(x):
#     global a
#     print(a)
#     a = x
#     print(a)

# f(10)
# a = 3
# print(a)

# import math
# # dir用来看库里包含哪些函数
# print(dir(math))
# # pi取值3.141592653589793
# print(math.pi)
# # e取值2.718281828459045
# print(math.e)
# # round函数：四舍五入
# print(round(3.5))
# # pow(x,y) 求x的y次方
# print(math.pow(2,3))

# import os
# # 获取当前工作目录
# print(os.getcwd())
# # 删除文件
# os.remove()
# # 重命名
# os.rename()

# sum = 0
# def add(n):
#     if n == 1:
#         return n
#     else:
#       sum = add(n-1) * n
#       return sum

# print(add(4))

# 练习题1 BMI

# weight, height = input('输入a,b空格隔开:').split()
# weight = int(weight)
# height = float(height)
# BMI = weight / height** 2
# if BMI < 18.5:
#     print('你的BMI为{}'.format(BMI))
#     print("过轻")
# elif BMI >= 18.5 and BMI <= 23.9:
#     print('你的BMI为{}'.format(BMI))
#     print('正常')
# elif BMI >=24 and BMI <= 27.9:
#     print('你的BMI为{}'.format(BMI))
#     print('过重')
# else:
#     print('你的BMI为{}'.format(BMI))
#     print('肥胖')

# 第二题，华氏度摄氏度转换显示
# def changeToS(F):
#     return round(5/9*(F-32))
# F=0
# while F<=300:
#     print('华氏度：{}，摄氏度：{}'.format(F,changeToS(F)))
#     F+=20

# 第三题 角谷猜想
# def whatIs(n):
#     if n % 2 == 0:
#       print("{}/2={}".format(n,int(n/2)))
#       return int(n/2)
#     else:
#       print("{}*3+1={}".format(n,n*3+1))
#       return n*3+1
    
# n = 10
# while n != 1 :
#    n = whatIs(n)



# 第四题 求n!之和
# def add(n):
#     if n==1:
#         return n
#     else:
#       n = add(n-1)*n
#       return n
# x = int(input('请输入你想求的n!之和：'))
# sum = 0
# for i in range(1,x+1):
#     sum = sum + add(i)
# print(sum)

# 第五题 求无重复数
# 三位数的循环，最开始变化的数k放在个位
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and j!=k and i!=k:
#                 print(i*100+j*10+k)

# 第六题 37
# for i in range(100,1001):
#     if i%37 == 0:
#         n = i%10*100 + i/10%10 + i/100*10
#         m = i%10*10 + i/10%10*100 + i/100
#         print(m,n)
#         # if n%37 != 0 and m %37 != 0 :
#         #     print('定理错误')
#         #     break
#         # else:
#         #     print('正确')

# 第七题 完数
# def isWan(n):
#   sum = 0
#   for i in range(1,n):
#       if n%i == 0:
#           sum = sum + i
#   if sum == n:
#       print(n)

# for j in range(1,1001):
#     isWan(j)

# s = 'insert'
# with open('D:\\S\\firstPro.txt','a+') as f:
#     f.seek(0)
#     f.writelines(s)
#     f.seek(0)
#     p = f.readlines()
#     print(p)

# 统计有多少行
# with open('D:\\S\\firstPro.txt') as f:
#     data = f.readlines()
#     length = len(data)
#     print(length)

# 拉取小王子的书评
# url = 'https://book.douban.com/subject/1084336/comments/'

# import requests

# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

# r = requests.get(url,headers=headers)

# html = r.text
# print(html)

# from bs4 import BeautifulSoup

# markup = '<p class = "title"><b>The Little Prince </b></p>'
# soup = BeautifulSoup(markup,"lxml")
# tag = soup.p
# 获取名字  tag.name
# 属性 tag.attrs
# tag['class']
# 非属性字符串 tag.string
# 寻找所有b标签的内容 soup.find_all('b')


# import requests
# from bs4 import BeautifulSoup

# url = 'https://book.douban.com/subject/1084336/comments/'
# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
# r = requests.get(url,headers=headers)
# soup = BeautifulSoup(r.text,"lxml")
# pattern = soup.find_all('span','short')
# for item in pattern:
#     print(item.string)
# # print(soup)

# week = ['one','two','three','four','five','six','seven']
# 根据下标进行输出，-代表从后往前，1:4代表从下标1到下标3（4-1），：6就是0:6，：：-1表示逆序输出
# print(week[1],week[-2],week[1:4],week[:6],week[::-1],sep='\n')
# 输出结果
# two
# six
# ['two', 'three', 'four']
# ['one', 'two', 'three', 'four', 'five', 'six']
# ['seven', 'six', 'five', 'four', 'three', 'two', 'one']

# 字符串重复 *
print('apple'*3) # appleappleapple
# 字符串连接 +
print('pine'+'apple') #pineapple
# in 用于判断对象是否包含在后面的数组里
print('BA' in ('BA','ba'))