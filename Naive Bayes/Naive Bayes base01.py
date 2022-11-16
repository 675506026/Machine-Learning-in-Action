# 以在线社区留言为例。为了不影响社区的发展，我们要屏蔽侮辱性的言论，所以要构建一个快速过滤器。
# 如果某条留言使用了负面或者侮辱性的语言，那么就将该留言标志为内容不当。
# 过滤这类内容是一个很常见的需求。对此问题建立两个类型：侮辱类和非侮辱类，使用1和0分别表示。
# 我们把文本看成单词向量或者词条向量，也就是说将句子转换为向量。
# 考虑出现所有文档中的单词，再决定将哪些单词纳入词汇表或者说所要的词汇集合，然后将每一篇文档转换为词汇表上的向量。
# 简单起见，我们先假设已经将本文切分完毕，存放到列表中，并对词汇向量进行分类标注。


"""
函数说明:创建实验样本

Parameters:
    无
Returns:
    postingList - 实验样本切分的词条
    classVec - 类别标签向量

"""


def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],  # 切分的词条
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 类别标签向量，1代表侮辱性词汇，0代表不是
    return postingList, classVec


if __name__ == '__main__':
    postingLIst, classVec = loadDataSet()
    for each in postingLIst:
        print(each)
    print(classVec)
