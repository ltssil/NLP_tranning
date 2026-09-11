"""
案例：
    演示 文本张量（文本的词向量表示形式）的实现方式之 word2vec

word2vec介绍：
    概述：
        它是文本张量的一种实现手段，基于 one-hot 做的优化，主要有 CBOW（连续词袋模式），SkipGram（跳字模式）
    其中：
        CBOW：基于上下文预测 中间值
        SkipGram：基于中间值 预测上下文
    无论：
        是上述的那种方式，最终都是用（隐藏层）的权重矩阵，充当：词向量矩阵。
    即：
        权重矩阵的每一列，分别对应1个单词的word2vec词向量，
    细节：
        facebook开发的FastText工具包，就是一个开源的词向量和文本分类工具，我们直接用它来演示 word2vec.

关于 fasttext 的安装：
    pip install fasttext        直接装即可，如果报错，就装如下的编译版本
    pip install fasttext-wheel  如果上述命令报错，则执行这个命令即可
"""

# 导包
import fasttext

# todo 1. 定义函数 实现：训练向量模型，并保存模型
def dm01_train_save() :
    # 1. 直接开始训练，以无监督的方式运行
    my_model = fasttext.train_unsupervised('./data/wh02ad')

    # 2. 保存模型为 -> 二进制文件，后续可以通过fasttext.load_model() 加载模型
    my_model.save_model('./model/wh02_fil9.bin')
    print("训练完毕，模型保存成功")

# todo 2. 定义函数 实现：加载模型，并预测
def dm02_get_word_vector() :
    # 1. 加载预训练的fasttext模型
    model = fasttext.load_model('./model/wh02_fil9.bin')

    # 2. 获取单个词的词向量表示
    results = model.get_word_vector('the')

    # 3. 打印结果
    print(f'type:{type(results)}')      # Numpy数组
    print(f'shape:{results.shape}')     # (100,)
    print(f'result:{results}')          # 具体的词向量值

# todo 3. 定义函数 实现：查看单词的相似度（即：找单词的近义词） -> 模型的效果检验
def dm03_get_similarity() :
    # 1. 加载预训练的fasttext模型
    model = fasttext.load_model('./model/wh02_fil9.bin')

    # 2. 查找某个单词的近义词
    # 默认是10个，可以用于：检验模型的语义理解能力
    # 返回的结果格式为：[(相似度分数,近义词),(相似度分数,近义词),(相似度分数,近义词)...]
    result = model.get_nearest_neighbors('dog')

    # 3. 输出结果
    print(f'result:{result}')

# todo n. 测试代码
if __name__ == '__main__':
    # 1. 测试：训练向量模型，并保存模型
    # dm01_train_save()
    # 2. 测试：加载模型，并预测
    # dm02_get_word_vector()
    # 3. 测试:查看单词的相似度（即：找单词的近义词） -> 模型的效果检验
    dm03_get_similarity()