"""
读取特定账户的INFO文件，分别记录顺序：按照0~500*1000的顺序，和乱序：根据order文件中的顺序 标签
"""

from PIL import Image
import os
import config

FactoryLabellingPath = config.setting['NetworkSetting']['FactoryLabellingPath']
DEFAULT = {1: (-1, -1), 2: (-1, -1, -1)}  # 不同版本的默认未分类标签


class Account:
    def __init__(self, version=1, account_index=0):
        """
        :param account_index: 用户账户序号
        """
        self.version, self.account_index = version, account_index
        # 初始化所有tag，一共500*1000
        self.tags = [[] for _ in range(500*1000)]  # 顺序标签
        # 读取order
        self.order = open(os.path.join(FactoryLabellingPath, 'INFO v' + str(version), 'ACCOUNT', str(self.account_index) + '.ini'), 'r').readlines()
        self.order = [int(i[:-1]) for i in self.order]
        self.default = DEFAULT[version]
        self.order_tags = [self.default for _ in self.order]  # 乱序标签
        # 分类标签
        self.category_tags = {}

        # 读取已贴标签tag
        files = os.listdir(os.path.join(FactoryLabellingPath, 'INFO v' + str(version), str(self.account_index)))
        files = [int(i[:-4]) for i in files]
        files.sort()
        for file in files:
            f = open(os.path.join(FactoryLabellingPath, 'INFO v' + str(version), str(self.account_index), str(file) + '.ini'), 'r').readlines()
            for i in range(2, len(f)):
                line = f[i]
                equal = line.index('=')
                index = int(line[:equal])
                value = line[equal + 2:-2].split(',')
                value = tuple([int(i) for i in value])
                self.tags[self.order[file*1000+index]].append(value)
                self.order_tags[file*1000+index] = value

    def __getitem__(self, item):
        return self.order_tags[item]

    def __len__(self):
        return len(self.order_tags)

    def getOrderImage(self, item):
        """
        获取乱序item对应的图片
        :param item:
        :return:
        """
        return self.getImage(self.order[item])

    def getImage(self, item):
        """
        获取有序item对应的图片
        :param item:
        :return:
        """
        a, b = item // 1000, item % 1000
        fig = Image.open(os.path.join(FactoryLabellingPath, 'FIG', str(a), str(b).rjust(3, '0') + '.jpg'))
        ref = Image.open(os.path.join(FactoryLabellingPath, 'REF', str(a), str(b).rjust(3, '0') + '.jpg')).crop((54, 54, 162, 162))
        return fig, ref

    def orderTagsOverWriteTags(self):
        """
        根据乱序tags覆盖成有序tags
        :return:
        """
        pass

    def saveAll(self):
        """
        保存所有标签信息到INFO
        :return:
        """
        files = list(range(len(self) // 1000))
        for i in files:
            f = open(os.path.join(FactoryLabellingPath, 'INFO v' + str(self.version), str(self.account_index), str(i) + '.ini'), 'w')
            f.write(';This is the tag info\n\n')
            for j in range(1000):
                 if tuple(self.order_tags[i*1000 + j]) != (-1, -1, -1):
                     f.write(str(j) + '=' + str(tuple(self.order_tags[i*1000 + j])) + '\n')
            f.flush()
            f.close()

    def transfer(self, tag1, tag2):
        """
        批量将tag1改成tag2
        :param tag1: 原始分类
        :param tag2: 目标分类
        :return:
        """
        for i, tag in self.order_tags:
            if tag == tag1:
                self.order_tags[i] = tag2

    def order2category(self):
        # 分类存储标签
        self.category_tags = {}
        for item in config.tags:
            self.category_tags[item] = []
        for i, item in enumerate(self.order_tags):
            if tuple(item) == (-1, -1, -1):
                continue
            self.category_tags[tuple(item)].append(i)

    def category2order(self):
        for category, item in self.category_tags.items():
            for index in item:
                self.order_tags[index] = category


def account_Combine(account1: Account, account2: Account, mode='and'):
    """
    合并两个账户中的数据，相同部分保留，不同部分舍弃
    :param account1:
    :param account2:
    :param mode: 'and'：合并两个账户中有效且相同的部分；
                 'first'：保留所有account1中的所有标签，account1中未被标记的标签则被account2中的有效标签代替；
                 ‘or’：合并两个账户中有效且相同的部分，无效标签按未被标记处理
    :return:
    """
    if mode == 'and':
        tags = []
        for i, j in zip(account1.tags, account2.tags):
            tag1, tag2 = list(set(i)), list(set(j))
            if len(tag1) == 1 and len(tag2) == 1 and tag1[0] == tag2[0]:
                tags.append(tag1[0])
            else:
                tags.append(account1.default)
        return tags
    elif mode == 'first':
        tags = []
        for i, j in zip(account1.tags, account2.tags):
            tag1, tag2 = list(set(i)), list(set(j))
            if len(tag1) > 1:
                tags.append(account1.default)
            elif len(tag1) == 1:
                tags.append(tag1[0])
            elif len(tag1) == 0 and len(tag2) == 1:
                tags.append(tag2[0])
            else:
                tags.append(account1.default)
        return tags
    elif mode == 'or':
        tags = []
        for i, j in zip(account1.tags, account2.tags):
            tag1, tag2 = list(set(i)), list(set(j))
            if len(tag1) == 1:
                if len(tag2) == 1:
                    if tag1[0] == tag2[0]:
                        tags.append(tag1[0])
                    else:
                        tags.append(account1.default)
                else:
                    tags.append(tag1[0])
            else:
                if len(tag2) == 1:
                    tags.append(tag2[0])
                else:
                    tags.append(account1.default)
        return tags
    else:
        return

