"""
案例：
    演示 jieba 分词库的应用

分词的相关介绍：
    概述：
        分词过程 = 找到 分界符 的过程 ， 找到分界符就可以分词了
        每个分词结果 = 1个 Token
    常见的分词包：
        jieba：          精确模式，全模式，搜索引擎模式，繁体字符，用户自定义字典...
        IK分词器：        ElasticSearch搜索引擎用的多；
        SnowNLP：        基于概率算法的中文自然语言处理工具包
        pyltp：          哈工大的
        THULAC:         清华的

    jieba的作用介绍：
        A. 支持多种分词模式
            精确模式：       试图把句子 最精确的切开 适合：文本分析
            全模式：        把句子中所有的可以成词的词语都扫描出来，速度非常快，但是不能消除歧义
            搜索引擎模式：    在精确模式的基础上对长词再次切分，提高召回率
        B. 支持中文繁体分词
        C. 支持用户自定义词典
        总结：
            上述的分词模式，其实就是 分词的粒度不同， 例如 “软件工程 ” -> 软件工程（粗粒度） ； 软件，工程（细粒度）

额外做的事：
    为了不和前面的环境冲突，创建1个新的沙箱使用

细节：
    jieba属于第三方的库，用之前需要安装
"""

# 导包
import jieba

# todo 1. 定义函数，演示jieba精确分词模式，适用于：文本分析
def dm01() :
    # 1. 定义待分词的文本内容
    content = "投身农牧广阔舞台，解锁无限职业可能，期待你的加入！"

    # 2. 使用jieba进行 精确模式分词(默认模式) -> cut_all = False
    # result1 : 生成器对象，好处：节省内存，只能便利一次
    result1 = jieba.cut(content , cut_all=False)
    print(result1) # <generator object Tokenizer.cut at 0x0000024252472F00>

    # 3. 从生成器对象中，获取所有的分词结果
    # # 3.1 思路1：next()函数，逐个获取下个元素
    # print(next(result1))
    # print(next(result1))
    # print(' =·= ' * 10)
    #
    # # 3.2 思路2：遍历方式，从生成器中获取元素
    # for item in result1 :
    #     print(item)
    # print(' =·= ' * 10)

# todo 2. 定义函数，演示jieba全模式，适用于：关键词提取，不需要严格分词准确性的场景
def dm02() :
    # 定义待分词的文本内容
    content = "投身农牧广阔舞台，解锁无限职业可能，期待你的加入！"

    # 2. 使用jieba进行 精确模式分词(默认模式) -> cut_all = False
    # result1 : 生成器对象，好处：节省内存，只能便利一次
    result1 = jieba.cut(content, cut_all=False)
    print(result1)  # <generator object Tokenizer.cut at 0x0000024252472F00>

    # 3. 从生成器对象中，获取所有的分词结果
    # 3.1 思路1 : next()函数 ，逐个获取下个元素
    # print(next(result1))
    # print(next(result1))
    # print(' -.- ' * 10)

    # # 3.2 思路2：遍历方式，从生成器中获取元素
    # for item in result1 :
    #     print(item)
    # print(' =·= ' * 10)

    # 4. 如果要列表怎么办？即：[词1,词2,词3...]
    # 思路1 ： 直接吧上述的生成器转成列表
    list1 = list(result1)
    print(list1)

    # 思路2：切词时直接返回 list ， 相当于：语法糖
    list2 = jieba.lcut(content, cut_all=True)
    print(list2)

# todo 3. 定义函数，演示jieba搜索引擎模式，适用于：搜索引擎分词，文本匹配
"""
解释：
    搜索引擎分词模式 -> 在精确分词的基础上对长词进行再次切分，提高召回率
例如：：
    场景1：用户录入“程序员”
        精确模式：只能匹配包含完整“程序员”的文档
        搜索引擎模式：不仅能匹配“程序员”文档，还能匹配“程序”，“员”的文档，提高召回
        
    场景2： 实际应用场景（电商搜索），商品标题为：《苹果手机保护套》，用户搜索《苹果套》
        精确模式：无法匹配，分词为:（"苹果","手机","保护套")
        搜索引擎模式：能匹配，分词为：（"苹果","手机","保护","套")
"""
def dm03() :
    # 定义待分词的文本内容
    content = "投身农牧广阔舞台，解锁无限职业可能，期待你的加入！"

    # 2. 使用jieba进行 搜索引擎模式分词 -> cut_for_search
    # result1 : 生成器对象，好处：节省内存，只能便利一次
    result1 = jieba.cut_for_search(content)
    print(result1)  # <generator object Tokenizer.cut at 0x0000024252472F00>

    # 3. 从生成器对象中，获取所有的分词结果
    # 3.1 思路1 : next()函数 ，逐个获取下个元素
    # print(next(result1))
    # print(next(result1))
    # print(' -.- ' * 10)

    # # 3.2 思路2：遍历方式，从生成器中获取元素
    # for item in result1 :
    #     print(item)
    # print(' =·= ' * 10)

    # 4. 如果要列表怎么办？即：[词1,词2,词3...]
    # 思路1 ： 直接吧上述的生成器转成列表
    list1 = list(result1)
    print(list1)

    # 思路2：切词时直接返回 list ， 相当于：语法糖
    list2 = jieba.lcut_for_search(content)
    print(f'搜索引擎模式:{list2}')

    # 5. 扩展：打印下 精确模式分词，全模式分词，以便和上述的搜索引擎模式进行对比
    list3 = jieba.lcut(content , cut_all=False)
    print(f"精确模式:{list3}")

    list4 = jieba.lcut(content, cut_all=True)
    print(f"全模式:{list4}")

# todo 4. : 定义函数，演示jieba分词之繁体字
def dm04() :
    # 1. 定义句子，记录要被分词的内容
    content = '煩惱即是菩提，我暫且不提'

    # 2. 使用jieba进行繁体字分词
    result = jieba.lcut(content , cut_all = False) # 精确模式

    # 3. 打印结果
    print(result)

# todo 6. 测试代码
if __name__ == '__main__':
    # 1. 测试：jieba的精确模式分词
    # dm01()
    # 2. 测试：jieba的全模式分词
    # dm02()
    # 3. 测试：jieba的 搜索引擎分词
    #dm03()
    # 4. 测试：jieba的繁体字分词
    dm04()



