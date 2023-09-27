# -*- coding: UTF-8 -*-
# 更多控制流工具，除了刚介绍的 while 语句，Python 还用了一些别的。



# if 语句
def ifcase():
    x = int(input("Please enter an integer: "))
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

#match 语句
def matchcase(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 500:
            return "It is error"
        case 200:
            return "Success"
        # 你可以使用 | （“ or ”）在一个模式中组合几个字面值
        case 401 | 403 :
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"


# for语句
def forcase():
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))
    #很难正确地在迭代多项集的同时修改多项集的内容。更简单的方法是迭代多项集的副本或者创建新的多项集
    # 创建集合
    users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
    # 需要复制一个新数组 copy(), 否则会报错：RuntimeError: dictionary changed size during iteration
    for user, status in users.copy().items():
        # print(f'user,{user}') # user,Hans
        # print(f'status,{status}') # status,active
        if status == 'inactive':
            del users[user]
    print(users) #{'Hans': 'active', '景太郎': 'active'}
    # 或者创建一个集合对象
    active_users = {}
    for user,status in users.items():
        if status == 'active':
            active_users[user] = status
    print(active_users) # {'Hans': 'active', '景太郎': 'active'}

    # 内置函数 range() 用于生成等差数列
    for i in  range(5):
        print(i) # 0 1 2 3 4 5
    # 生成的序列绝不会包括给定的终止值；range(10) 生成 10 个值——长度为 10 的序列的所有合法索引。range 可以不从 0 开始，且可以按给定的步长递增（即使是负数步长）
    print(list(range(5,10)))  # [5, 6, 7, 8, 9]
    print(list(range(0,10,3))) # [0, 3, 6, 9]
    print(list(range(-10, -100, -30))) # [-10, -40, -70]

    # 要按索引迭代序列，可以组合使用 range() 和 len()
    strArray = ['Mary', 'had', 'a', 'little', 'lamb']
    for i in range(len(strArray)):
        print(i,strArray[i])
        # 0 Mary
        # 1 had
        # .....

# 循环中的 break、continue 语句及 else 子句
# break 语句将跳出最近的一层 for 或 while 循环,for 或 while 循环可以包括 else 子句.
# 在 for 循环中，else 子句会在循环成功结束最后一次迭代之后执行,在 while 循环中，它会在循环条件变为假值后执行,无论哪种循环，如果因为 break 而结束，那么 else 子句就 不会 执行。
# 寻找 2 ～ 10 之间的质数
def find_prime_num():
    for n in range(2,10):
        for x in range(2,n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                # 跳出循环，甚至不会执行最外层的 else 语句
                break
        else:
            # else 子句用于循环时比起 if 语句的 else 子句，更像 try 语句的。try 语句的 else 子句在未发生异常时执行，循环的 else 子句则在未发生 break 时执行。
            print(n, 'is a prime number')

# continue 语句,以执行循环的下一次迭代来继续
def find_even_num():
    for num in range(0,10):
        if num % 2 == 0:
            print("Found an even number", num)
            # 继续下一次循环，如何用break 就会在进入if 子句后直接跳出整个循环
            continue
        print("Found an odd number", num)

# pass 语句不执行任何动作。语法上需要一个语句，但程序毋需执行任何动作时，可以使用该语句 ????
def passcase():
    while True:
        pass




if __name__ == '__main__':
    # ifcase()
    # print(matchcase(401))
    # forcase()
    # find_prime_num()
    # find_even_num()
    passcase()