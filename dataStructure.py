# -*- coding: UTF-8 -*-
# 数据结构


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








if __name__ == '__main__':
    # list_method()
    stack_demo()