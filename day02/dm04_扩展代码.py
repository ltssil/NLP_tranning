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





# todo n. 测试代码
if __name__ == '__main__':
    # 1. 测试map()函数的用法
    dm01_map()