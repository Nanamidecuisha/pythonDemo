# -*- coding: UTF-8 -*-
# 数据结构
from collections import deque


def list_method():
    num_list = list(range(1,10))
    # 在列表末尾添加一个元素
    num_list.append(10)

    other_list = [11,12,13]
    #用于将一个可迭代对象（通常是另一个列表）中的元素添加到列表的末尾，从而扩展列表的长度。
    num_list.extend(other_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # 在指定位置插入元素。第一个参数是插入元素的索引
    num_list.insert(0,0)
    # 从列表中删除第一个值为 x 的元素。未找到指定元素时，触发 ValueError 异常。
    num_list.remove(len(num_list)-1)
    # 删除列表中指定位置的元素，并返回被删除的元素。未指定位置时,删除最后一个元素
    del_value = num_list.pop(0)
    # 删除列表里的所有元素，相当于 del a[:]
    other_list.clear()
    #返回列表中第一个值为 x 的元素的零基索引。未找到指定元素时，触发 ValueError 异常。
    index_value1 = num_list.index(8)
    index_value2 = num_list.index(8,2,10)
    # 返回列表中元素 x 出现的次数
    num_count = num_list.count(7)
    # 就地排序列表中的元素,reverse 默认为true 升序
    num_list.sort(reverse=True) # [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # 翻转列表中的元素
    num_list.reverse() # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # 返回列表的浅拷贝
    new_list = num_list.copy()

    print(f'num_list,{num_list}')
    print(f'del_value,{del_value}') # 0
    print(f'other_list,{other_list}') #[]
    print(f'index_value1,{index_value1}') # 7
    print(f'index_value2,{index_value2}') # 7
    print(f'num_count,{num_count}') # 1
    print(f'new_list,{new_list}') # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#列表方法可以非常容易地将列表作为栈来使用，最后添加的元素将最先被提取（“后进先出”）。
#要向栈顶添加一个条目，请使用 append()。 要从栈顶提取一个条目，请使用 pop()，无需显式指定索引。
def stack_demo():
    stack = [3, 4, 5]
    stack.append(6)
    stack.append(7)
    print(f'stack,{stack}') # [3, 4, 5, 6, 7]
    first_num = stack.pop()
    second_num = stack.pop()
    third_num = stack.pop()

    print(f'first_num,{first_num}') # 7
    print(f'second_num,{second_num}') # 6
    print(f'third_num,{third_num}') # 5
    print(f'stack,{stack}') # [3, 4]

# 用列表实现队列
# 列表也可以用作队列，最先加入的元素，最先取出（“先进先出”）；然而，列表作为队列的效率很低。
# 因为，在列表末尾添加和删除元素非常快，但在列表开头插入或移除元素却很慢（因为所有其他元素都必须移动一位）
def queue_demo():
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")
    queue.append("Graham")

    first_value = queue.popleft()
    second_value = queue.popleft()

    print(f'first_value,{first_value}') # Eric
    print(f'second_value,{second_value}') #John

# 列表推导式
# 列表推导式创建列表的方式更简洁。常见的用法为，对序列或可迭代对象中的每个元素应用某种操作，用生成的结果创建新的列表；或用满足特定条件的元素创建子序列

def list_comprehensions():
    squares1 = []
    squares2 = []
    squares3 = []

    combs1 = []
    combs2 = []

    # 方法1
    for x in range(10):
        squares1.append(x ** 2)
    print(f'squares1,{squares1}') # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # 方法2
    squares2 = list(map(lambda x: x ** 2, range(10)))
    print(f'squares2,{squares2}') # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # 方法3 ，这种方法最简单易懂
    squares3 = [x ** 2 for x in range(10)]
    print(f'squares3,{squares3}') # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # 以下列表推导式将两个列表中不相等的元素组合起来
    combs1 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
    print(f'combs1,{combs1}') # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
    # 等价于
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                combs2.append((x, y))
    print(f'combs2,{combs2}') # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

    # 实际用法
    vec = [-4, -2, 0, 2, 4]
    # 将数组里面的所有数都乘以2
    vec_double = [v * 2 for v in vec]
    print(f'vec_double,{vec_double}') # [-8, -4, 0, 4, 8]

    # 过滤掉数组中小于0的值
    filter_value = [v for v in vec if v > 0]
    print(f'vec_double,{filter_value}') # [2, 4]

    # 数组中所有元素都执行一个函数
    abs_value = [abs(v) for v in vec]
    print(f'abs_value,{abs_value}') # [4, 2, 0, 2, 4]
    freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
    # 去除两边的空格
    strip_value = [fruit.strip() for fruit in freshfruit]
    print(f'strip_value,{strip_value}') # ['banana', 'loganberry', 'passion fruit']

    # 创建一个 元组的数组对象，(x,y) 其中 y是x的平方
    tuples_value = [(x , x ** 2) for x in range(10)]
    print(f'tuples_value,{tuples_value}')



















if __name__ == '__main__':
    # list_method()
    # stack_demo()
    # queue_demo()
    list_comprehensions()