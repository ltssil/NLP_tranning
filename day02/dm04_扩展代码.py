# 某些函数的实例 Demo

# 需求 1. 演示下map函数的用法
# todo 1. 定义1个函数 ， 接收一个参数 ， 返回其+2的结果
def fun(x) :
    return x + 2

# todo 2. 定义函数，演示map()函数的用法， 即：把上述的 fun() 函数 ， 作用到列表中的每个元素上
def dm01_map() :
    # 1. 将上述的fun() 函数， 作用到：列表中的每个元素上
    # map() : 返回1个迭代器对象，此时并未实现执行运算
    result = map(fun , [1 , 2 , 3 , 4 , 5])
    print(f"result:{result}") # result:<map object at 0x00000231D3E5C610>

    # 2. 第一次 遍历map对象
    for i in result :
        print(i)        # 依次输出：3 , 4 , 5 , 6 , 7
    print("---" * 10)

    # 3. 第二次尝试遍历map对象
    print(f'result : {list(result)}')       # result : []

    # 4. 使用 lambda表达式实现 相同功能
    result2 = list(map(lambda x : x + 2 , [10 , 20 , 30]))
    print(f"result2 : {result2}")       # result2 : <map object at 0x00000211A4F688E0>

# 需求2 ： 演示chain()函数的用法
# 导包
from itertools import chain
import jieba

# todo 1. 测试chain()函数的用法
def dm02_chain() :
    # 1. 定义两个列表
    list1 = [1 , 2 , 3]
    list2 = [1 , 2 , 3 , 4]

    # 2. chain(): 他是"惰性"的，即：创建chain()对象时，不会立即遍历底层的可迭代对象，只有在实际迭代(例如：转列表，遍历打印等)时，才会逐个获取元素，节省内存
    # 一旦迭代完毕，再次迭代同一个chain对象，不会得到数据，因为迭代器的元素已经耗尽
    result = chain(list1, list2)
    print(f'result : {result}')         # result : <itertools.chain object at 0x000001F5961450F0>
    print(f'result : list({result})')

    # chain()函数，有点类似于 : list1.extend(list2)
    # list1.extend(list2)
    # print(f'result2 : {list1}')

    # 3. 重新定义列表，记录两个句子
    list1 = ['今天天气很好' , '今天天很热']
    # 4. 对上述两个例子进行切词
    tmp_list = map(lambda x : jieba.lcut(x), list1)
    # print(f'tmp_list : {tmp_list}')             # <map object at 0x000001C3D4AA4CA0>
    # print(f'tmp_list : {list(tmp_list)}')       # tmp_list : [['今天天气', '很', '好'], ['今天', '天', '很', '热']]

    # 5. 用chain()函数链接两个列表 ， 这里的 * 意思是 告诉函数 ： 把后面的参数，逐个取出来，拼接到前面
    # result = list(chain(*tmp_list))     # 不会去重
    # print(f'result : {result}')
    # result = set(chain(*tmp_list))      # 会去重
    # print(f'result : {result}')

    # 6. 合并版
    list1 = ['今天天气很好' , '今天天很热']
    result = set(chain(*map(lambda x : jieba.lcut(x), list1)))
    print(f'result : {result}')

# todo n. 测试代码
if __name__ == '__main__':
    # 1. 测试map()函数的用法
    # dm01_map()

    # 2. 测试chain()函数的用法
    dm02_chain()