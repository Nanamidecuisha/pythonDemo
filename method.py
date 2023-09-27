# -*- coding: UTF-8 -*-
# 定义函数

# 创建一个可以输出限定数值内的斐波那契数列函数
# 函数内的第一条语句是字符串时，该字符串就是文档字符串，也称为 docstring，详见 文档字符串。利用文档字符串可以自动生成在线文档或打印版文档，还可以让开发者在浏览代码时直接查阅文档
def fib(n):
    """Print a Fibonacci series up to n."""
    a,b = 0,1
    while a < n:
        print(a,end=",")
        a,b = b,a+b
    print()

# 不直接输出斐波那契数列运算结果，而是返回运算结果列表的函数
def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    a,b = 0,1
    result = []
    while a < n:
        # 它等同于 result = result + [a]，但效率更高。
        result.append(a)
        a,b = b,a+b
    # return 语句返回函数的值。return 语句不带表达式参数时，返回 None。函数执行完毕退出也返回 None。

    return result

# 默认值参数
# 为参数指定默认值是非常有用的方式。调用函数时，可以使用比定义时更少的参数

def ask_ok(prompt,retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        # 关键字 in ，用于确认序列中是否包含某个值
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# 默认值只计算一次。默认值为列表、字典或类实例等可变对象时，会产生与该规则不同的结果。例如，下面的函数会累积后续调用时传递的参数
def e(a,L=[]):
    L.append(a)
    print(L)
# 不想在后续调用之间共享默认值时，应以如下方式编写函数
def g(a,L=None):
    if L is None:
        L =[]
    L.append(a)
    return L

#关键字参数
#kwarg=value 形式的 关键字参数 也可以用于调用函数
#该函数接受一个必选参数（voltage）和三个可选参数（state, action 和 type）
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

def call_parrot():
    parrot(1000)  # 1 positional argument
    parrot(voltage=1000)  # 1 keyword argument
    parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
    parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
    parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
    parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

    # 以下调用函数的方式都无效：
    parrot()  # required argument missing
    # parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
    parrot(110, voltage=220)  # duplicate value for the same argument
    parrot(actor='John Cleese')  # unknown keyword argument

#最后一个形参为 **name 形式时，接收一个字典（详见 映射类型 --- dict），该字典包含与函数中已定义形参对应之外的所有关键字参数。**name 形参可以与 *name 形参（下一小节介绍）组合使用（*name 必须在 **name 前面）， *name 形参接收一个 元组，该元组包含形参列表之外的位置参数
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])



# 特殊参数
#默认情况下，参数可以按位置或显式关键字传递给 Python 函数。
#为了让代码易读、高效，最好限制参数的传递方式，这样，开发者只需查看函数定义，即可确定参数项是仅按位置、按位置或关键字，还是仅按关键字传递。
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    # 仅限位置 时，形参的顺序很重要，且这些形参不能用关键字传递。仅限位置形参应放在 / （正斜杠）前。/ 用于在逻辑上分割仅限位置形参与其它形参。如果函数定义中没有 /，则表示没有仅限位置形参。
    # 把形参标记为 仅限关键字，表明必须以关键字参数形式传递该形参，应在参数列表中第一个 仅限关键字 形参前添加 *
    # 所以，pos1, pos2 在 / 前，是位置性参数，kwd1, kwd2 在 * 后，是关键字参数，而 pos_or_kwd 既能使用 位置性 还可以使用 关键字参数

  print(pos1,pos2)

# 下面的函数定义中，kwds 把 name 当作键，因此，可能与位置参数 name 产生潜在冲突 TypeError: foo() got multiple values for argument 'name'
# 加上 / （仅限位置参数）后，就可以了。此时，函数定义把 name 当作位置参数，'name' 也可以作为关键字参数的键
def foo(name,/, **kwds):
    print(kwds)
    return 'names' in kwds

#任意实参列表
#调用函数时，使用任意数量的实参是最少见的选项。这些实参包含在元组中（详见 元组和序列 ）。在可变数量的实参之前，可能有若干个普通参数
def concat(*args, sep="/"):
    return sep.join(args)

#解包实参列表
#函数调用要求独立的位置参数，但实参在列表或元组里时，要执行相反的操作。例如，内置的 range() 函数要求独立的 start 和 stop 实参。如果这些参数不是独立的，则要在调用函数时，用 * 操作符把实参从列表或元组解包出来

def unpack(voltage, state='a stiff', action='voom'):
    print(list(range(3,6))) #[3, 4, 5]
    range_list = [3,6]
    print(list(range(*range_list))) #[3, 4, 5]
    # 字典可以用 ** 操作符传递关键字参数
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

#Lambda 表达式
#lambda 关键字用于创建小巧的匿名函数。lambda a, b: a+b 函数返回两个参数的和。Lambda 函数可用于任何需要函数对象的地方。在语法上，匿名函数只能是单个表达式
def make_incrementor(n):
    return lambda x: x + n

def sort_case():
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    # 解读一下这个lambda表达式，key=lambda pair: pair[2] ，key 就类似于函数名， lambda后面的pari 就类似于参数
    # pair[2] 就类似于返回值
    # sort(key=None,reverse=False)的作用是 ，根据key值来进行升序排序（默认升序），要像降序就设置 reverse=True
    pairs.sort(key=lambda pair: pair[1])
    print(pairs)  # [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]


if __name__ == '__main__':
    # fib(200)
    f = fib
    # 函数定义在当前符号表中把函数名与函数对象关联在一起。解释器把函数名指向的对象作为用户自定义函数。还可以使用其他名称指向同一个函数对象，并访问访该函数
    f(200) #0,1,1,2,3,5,8,13,21,34,55,89,144,
    # fib 不返回值，因此，其他语言不把它当作函数，而是当作过程。事实上，没有 return 语句的函数也返回值，只不过这个值比较是 None ,一般来说，解释器不会输出单独的返回值 None ，如需查看该值，可以使用 print()
    fib(0) # 没有输出值
    print(fib(0)) # None

    f100 = fib2(100)
    print(f100) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # 只给出必选实参
    #ask_ok('Do you really want to quit?')
    # 给出一个可选实参
    #result = ask_ok('OK to overwrite the file?', 2)
    # 给出所有实参
    #result = ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
    # print(result)
    e(1) #[1]
    e(2) #[1, 2]
    e(3) #[1, 2, 3]

    print(g(1)) #[1]
    print(g(2)) #[2]
    print(g(3)) #[3]

    #call_parrot()

    # 第一个值，是位置性参数
    # 第二 三个值，是位置性参数
    # 其他值是，关键性参数

    cheeseshop("Limburger", "It's very runny, sir.",
               "It's really very, VERY runny, sir.",
               shopkeeper="Michael Palin",
               client="John Cleese",
               sketch="Cheese Shop Sketch")

    # -- Do you have any Limburger ?
    # -- I'm sorry, we're all out of Limburger
    # It's very runny, sir.
    # It's really very, VERY runny, sir.
    # ----------------------------------------
    # shopkeeper : Michael Palin
    # client : John Cleese
    # sketch : Cheese Shop Sketch

    print(foo('', **{'name': 2,'age':18,'nickname':'nanami'}))

    print(concat("earth", "mars", "venus"))

    unpack_value = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
    # 没有在前面加 ** ，把unpack_value 当成了位置性参数，所以给 voltage 赋值
    unpack(unpack_value) #-- This parrot wouldn't voom if you put {'voltage': 'four million', 'state': "bleedin' demised", 'action': 'VOOM'} volts through it. E's a stiff !
    # 在前面加 **，就把集合内对应的值 赋给了对应的字段
    unpack(**unpack_value) #This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
    ff  = make_incrementor(42)
    print(ff(0)) #42
    print(ff(1)) #43
    print(ff(2)) #44

    sort_case()





