# -*- coding: UTF-8 -*-
# Python 支持多种 复合 数据类型，可将不同值组合在一起。最常用的 列表 ，是用方括号标注，逗号分隔的一组值。

def print_param():
    squares = [1, 4, 9, 16, 25]
    print(squares)
    # 数组的索引，左边从 0 开始，右边从-1 开始
    print(squares[0]) # 1
    print(squares[-1]) # 25
    # :  左边截取，右边保留，索引都是从左到右计算
    # [2:] = [2:squares.len()] = [2:5]
    # [:2] = [0:2]
    print(squares[2:]) # [9, 16, 25]
    print(squares[:2]) # [1, 4]
    print(squares[-3:]) # [9, 16, 25]
    print(squares[-2:]) # [16, 25]
    print(squares[:-2]) # [1, 4, 9]

    # 数组的浅拷贝
    newSquares = squares[:]
    print(newSquares)

    # 数组合并操作
    squares += [36, 49, 64, 81, 100]
    print(squares)

    #与 immutable 字符串不同, 列表是 mutable 类型，其内容可以改变
    cubes = [1, 8, 27, 65, 125]
    cubes[3] = 64
    # append() 方法 可以在列表末尾添加新元素
    cubes.append(216)
    cubes.append(7 ** 3)
    print(cubes)

    #切片赋值可以改变列表大小，甚至清空整个列表
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # start 有值，end 有值，就是截取，前开后闭
    letters[2:5] = ['C', 'D', 'E']
    print(letters)
    # 清空数组
    letters[:] = []
    print(letters) # []

    # 还可以嵌套列表（创建包含其他列表的列表）
    a = ['a', 'b', 'c']
    n = [1, 2, 3]
    x = [a, n]
    print(x)
    print(x[0]) # ['a', 'b', 'c']
    print(x[0][1]) # b


def loop_num():
    a,b = 0,1
    while a < 10:
        print(a) # 0 1 1 2 3 5 8
        a,b = b,a+b

def print_num():
    a,b = 0,1
    while a < 1000:
        # 关键字参数 end 可以取消输出后面的换行, 或用另一个字符串结尾
        print(a,end= ',') # 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
        a,b = b,a+b



if __name__ == '__main__':
    # print_param()
    # loop_num()
    print_num()