"""
案例：
    演示 文本分析的常规操作

文本分析的作用：
    帮助我们理解数据语料，快速检查出语料中可能存在的问题
    例如：：
        数据质量类：          错别字、语法错误、重复内容、缺失值、噪声数据
        分布不均衡问题：       标签分布不均，句子长度不同

文本分析的方式：
    1. 标签的数量分布
    2. 句子长度分布
    3. 词频统计和关键字词云
"""

# 导包
import jieba                        # 分词包
import seaborn as sns               # 画图包
import pandas as pd                 # 数据处理包
import matplotlib.pyplot as plt     # 画图包，推荐pip install matplotlib==3.9
from itertools import chain         # 迭代器工具
import jieba.posseg as pseg         # 词性标注包
from wordcloud import WordCloud     # 词云包

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']        # 如果是Mac本，可以换成:'Arial Unicode MS'
plt.rcParams['axes.unicode_minus'] = False

# todo 1. 定义函数，实现： 训练集 和 测试集的 标签分布的 可视化统计
def dm01_label_sns_countplot() :
    # 1. 设置538风格 -> 一种具有现代感的可视化风格（可用可不用）
    # plt.style.use('fivethirtyeight')

    # 2. 读取训练集 和 测试集
    """
        :param1 : 文件路径
        :param2 : 列分隔符（csv文件用","  ， tsv文件用"\t"
    """
    train_data = pd.read_csv('data/train.tsv' , sep = '\t')
    dev_data = pd.read_csv('data/dev.tsv' , sep = '\t')
    # print(train_data.head())

    # 3. 统计训练集标签的 0 (负样本) 和 1(正样本) 的 数量，并可视化，采用：计数柱状图
    """
        :param1 : x轴标签
        :param2 : 数据集
        :param3 : 用于分组的分类变量
        :param4 : 是否显示图例(默认为True)
    """
    sns.countplot(x='label', data=train_data , hue='label' , legend=False)
    plt.title('train_label')        # 设置标题
    plt.tight_layout()              # 紧凑布局
    plt.show()

    # 4. 统计测试集标签的 0 (负样本) 和 1(正样本) 的 数量，并可视化，采用：计数柱状图
    sns.countplot(x='label', data=dev_data , hue='label' , legend=False)
    plt.title('dev_label')
    plt.tight_layout()
    plt.show()

# todo 2. 定义函数，实现： 训练集 和 测试集的 句子长度分布的 可视化统计
def dm02_len_sns_displot() :
    # 1. 读取训练集和测试集测试集
    train_data = pd.read_csv('data/train.tsv' , sep = '\t')
    dev_data = pd.read_csv('data/dev.tsv' , sep = '\t')

    # 2. 计算训练集的 每个句子的 长度
    # 思路1 ： map() 函数的方式实现
    # train_data['sentence_length'] = list(map(函数对象的功能是 获取句子长度 ， 句子))
    train_data['sentence_length'] = list(map(lambda x : len(x) , train_data['sentence']))
    # print(train_data.head())

    # 思路2 ： apply()函数的方式实现
    # train_data['sentence_length'] = train_data['sentence'].apply(lambda x : len(x))
    # print(train_data.head())

    # 3. 绘制训练集的句子长度分布
    # 3.1 计数柱状图
    sns.countplot(x='sentence_length', data=train_data)
    plt.title('训练集句子长度分布 —— 计数柱状图')
    plt.xticks([])      # 隐藏x轴刻度值
    plt.show()
    # 3.2 密度曲线图
    # 旧版
    # sns.displot(x='sentence_length', data=train_data)
    # plt.yticks([])
    # plt.show()

    # 新版 histplot() 直方图
    sns.histplot(x='sentence_length', data=train_data , kde=True)
    plt.title('训练集句子长度分布 —— 密度曲线图')
    plt.show()

    # 4. 计算测试集 每个句子的 长度
    dev_data['sentence_length'] = list(map(lambda x : len(x) , dev_data['sentence']))
    # 4.1 计数柱状图
    sns.countplot(x='sentence_length', data=dev_data)
    plt.title('测试集句子长度分布 —— 计数柱状图')
    plt.xticks([])
    plt.show()
    # 4.2 密度曲线图
    sns.histplot(x='sentence_length', data=dev_data, kde=True)
    plt.title('测试集句子长度分布 —— 密度曲线图')
    plt.show()

# todo n. 测试代码

if __name__ == '__main__':
    # 1. 测试：训练集 和 测试集的 标签分布的 可视化统计
    # dm01_label_sns_countplot()

    # 2. 测试： 训练集 和 测试集的 句子长度分布的 可视化统计
    dm02_len_sns_displot()


