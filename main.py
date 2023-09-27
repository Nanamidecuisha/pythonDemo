# This is a sample Python script.
# -*- coding: UTF-8 -*-
# 字符串


def print_hi(name):
    word = 'Python'
    print(word[2]) # t ,从左到右的第n个字符，索引从0开始
    print(word[-2]) # o，从右到左的第n个字符，索引从-1开始
    # : 就好比坐标轴的原点，左边就是 从字符串的左截取几位，右边就是 从左至右 保留几位。
    print(f'left, {word[2:]}') #thon
    print(f'right, {word[:2]}')  # Py
    # 负数的话，按照我的理解是在负数前 加上字符串的总长度，6-4=2
    # 所以，word[-4:] = word[2:] word[:-2] = word[:4]
    print(f'left, {word[-4:]}')  #thon
    print(f'right, {word[:-2]}') #Pyth
    #Python 字符串不能修改,Python 字符串不能修改，是 immutable 的。因此，为字符串中某个索引位置赋值会报错
    #如果必须存储一个不同的值，则必须创建新的对象
    # word[0] = 'j' # TypeError: 'str' object does not support item assignment
    # print(f'new word,{word}')

    newWord = 'j' + word[1:]
    print(f'newWord,{newWord}')
    # 使用len() 返回字符串的长度
    print(len(word)) #6
    # capitalize() 返回原字符串的副本，其首个字符大写，其余为小写
    print(newWord.capitalize()) #Jython
    # casefold() 返回原字符串消除大小写的副本。 消除大小写的字符串可用于忽略大小写的匹配。
    print(word.casefold()) #python
    # center() 返回长度为 width 的字符串，原字符串在其正中。 使用指定的 fillchar 填充两边的空位（默认使用 ASCII 空格符）。 如果 width 小于等于 len(s) 则返回原字符串的副本。
    print(word.center(9,'n')) #nnPythonn
    # count() 返回子字符串 sub 在 [start, end] 范围内非重叠出现的次数。 可选参数 start 与 end 会被解读为切片表示法。如果 sub 为空，则返回字符之间的空字符串数，即字符串的长度加一。
    print(word.count('n', 0, 6)) # 1
    print(word.count('',0,6)) # 7












# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
