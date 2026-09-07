"""
案例：
    演示one-hot编码，分别演示 复杂版 和 简单版

    文本张量相关介绍：
        概述：
            对文本进行切词，把每个词转成对应的词向量，即：用词向量的形式来描述文本 -> 文本张量（也叫：词向量表示法）
        作用：
            模型无法直接解析文本，可以转成 文本张量（词向量），作为模型的输入来进行各种处理，
        实现方式：
            one-hot编码： 稀疏词向量表示法
                独热编码，01编码，有这个词就用1表示，没有这个词就用0表示，
                列表长度 = 文本切词去重后总长
            word2vec:  稠密词向量表示法
                CBOW    连续词袋模式
                SkipGram 跳字模式
            word Embedding:   稠密词向量表示法
                词嵌入表示法

one-hot编码：
    优点：
    缺点：
    针对于缺点的解决方案：
"""

# Tensorflow 使用了 Intel的 oneDNN(原 MKL-DNN) 优化库 来加速CPU上 深度学习运算
"""
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1788748838.635647   29488 port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
"""
# 这个提示是告诉你：某些操作使用了自定义的oneDNN实现，可能导致浮点型计算结构有微小差异（不影响绝大多数任务）
# 注意：关闭后可能会略微降低CPU运算的性能，但不会影响功能
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# 导包
import jieba
from tensorflow.keras.preprocessing.text import Tokenizer       # 导入keras中的<<词汇映射器 Tokenizer>>

import joblib  # 用于对象保存与加载


# todo 1. 定义函数， 演示获取 one-hot编码
def dm01_onehot_generation() :
    # 1. 准备语料(人名，模拟：句子切词后的内容）
    vocabs = {'周杰伦' , '陈奕迅' , '王力宏' , '赵磊' , '李薇薇' , '查成龙'}

    # 2. 实例化 词汇映射器 Tokenizer
    my_tokenizer = Tokenizer()

    # 3. 通过词汇映射器，在语料库上进行训练
    my_tokenizer.fit_on_texts(vocabs)

    # 4. 打印 word_index字典， 键：歌手名  值：索引（序号）
    # 格式为： {'周杰伦': 1, '王力宏': 2, '查成龙': 3, '李薇薇': 4, '李宗盛': 5, '陈奕迅': 6}
    print(my_tokenizer.word_index)
    print('-----' * 5)

    # 5. 对每个词（歌手们） 进行 one-hot编码
    for vocab in vocabs :
        # 5.1 先创建长度 = 语料库长度的列表 ， 列表内长度都是0
        zero_list = [0] * len(vocabs)
        # print(zero_list)
        # 5.2 获取当前此会在 word_index 中的索引，因为索引是从1开始，所以索引要减1
        idx = my_tokenizer.word_index[vocab] - 1
        # 5.3 修改对应位置元素为1，完成one-hot编码
        zero_list[idx] = 1
        # 5.4 打印结果
        print(f'{vocab}的one-hot编码为:{zero_list}')

    # 6. 保存 词汇映射器对象
    joblib.dump(my_tokenizer , './model/onehot_tokenizer.pkl')
    print('模型保存成功')

# todo 2. 定义函数， 演示使用 one-hot编码
def use_one_hot() :
    # 1. 加载训练好的词汇映射器
    my_tokenizer = joblib.load('./model/onehot_tokenizer.pkl')
    # 2. 打印加载的词汇映射器的 word_index 字典，查看词汇和索引的对应关系
    print(my_tokenizer.word_index)
    # {'周杰伦': 1, '王力宏': 2, '陈奕迅': 3, '赵磊': 4, '李薇薇': 5, '查成龙': 6}
    # 3. 对指定词汇进行 one-hot编码
    token = '赵磊'
    # 4. 创建长度 = 语料库长度的列表 ， 列表内元素都是0
    zero_list = [0] * len(my_tokenizer.word_index)
    # 5. 获取指定词汇在 word_index中的索引 ， 因为索引是从1开始 ， 索引索引要减1
    idx = my_tokenizer.word_index[token] - 1
    # 6. 修改对应位置的元素为1 ， 完成one-hot编码
    zero_list[idx] = 1
    # 7. 打印结果
    print(f'{token}你的one-hot编码为:{zero_list}')

# todo 3.（扩展）. one-hot编码的简单版实现方式

# todo 4. 测试代码
if __name__ == '__main__':
    # 1. 测试获取onehot编码
    # dm01_onehot_generation()

    # 2. 测试使用onehot编码
    use_one_hot()