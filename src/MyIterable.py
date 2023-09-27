from collections.abc import Iterable, Sequence
import platform
import time


# 定义一个自定义类，实现 Iterable 接口
class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)


# 定义一个自定义类，实现 Sequence 接口
class MySequence:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)



if __name__ == '__main__':


    # 创建一个 Iterable 对象
    my_iterable = MyIterable([1, 2, 3, 4])

    # 创建一个 Sequence 对象
    my_sequence = MySequence([1, 2, 3, 4])

    print(f'python version is ,{platform.python_version()}')
    print(f'time.clock() is ,{time.process_time()}')
    # 使用 isinstance 检查对象是否符合 Iterable 或 Sequence 接口
    # print(isinstance(my_iterable, Iterable))  # 输出 True
    # print(isinstance(my_sequence, Sequence))  # 输出 True
