# coding: utf-8
##此模块用于构建FPtree数据结构

class Leaf:  # FP树中的节点
    def __init__(self, item=None):
        self.item = item
        self.frequency = 0
        self.last = None  # 树中的父节点
        self.next = {}  # 子节点的字典，以项名为键，项名对应的Leaf对象为值
        self.successor = None  # 链接表中的下一同项Leaf对象


class LinkLeaves:  # FP树中相同项的链接结构，运用Leaf的successor成员链接
    def __init__(self):
        self.head = None
        self.tail = None
        self.empty = True

    def push_back(self, ele):  # 链接表的增长操作
        if self.empty:
            self.head = ele
            self.tail = ele
            self.empty = False
        else:
            self.tail.successor = ele
            self.tail = self.tail.successor


# 表头中的元素
class Head:
    def __init__(self, item):
        self.item = item  # 对应元素成员
        self.frequency = 0  # 支持度
        self.leaf_link = LinkLeaves()  # 在FP书中的链接结构


class FPTree:
    def __init__(self, sup):
        self.sup = sup  # 支持度阈值
        self.head = []  # 表头
        self.support = {}  # 频繁项及其支持度
        self.tree = Leaf()  # FP树树根
        self.alpha_order = {}  # 用python列表自带的字典序处理排列支持度相同的频繁项

    def in_tree(self, file):  # 从一个每一行是以逗号分隔的事务数据的文件中构造FP树
        line_0 = file.readline()  # 第一次读取文件，获取频繁项，并排序
        while line_0:
            transaction_0 = line_0.split(',')
            transaction_0[-1] = transaction_0[-1][:-1]
            for item_0 in transaction_0:
                if item_0:
                    if item_0 in self.support:
                        self.support[item_0] += 1
                    else:
                        self.support[item_0] = 1
            line_0 = file.readline()
        raw_list = [item_2 for item_2 in self.support.keys()]
        for item_1 in raw_list:
            if self.support[item_1] >= self.sup:
                head = Head(item_1)
                head.frequency = self.support[item_1]
                self.head.append(head)
            else:
                self.support.pop(item_1)
        temp_alpha_list = [item_5 for item_5 in self.support.keys()]
        temp_alpha_list.sort(reverse=True)
        for index in range(len(temp_alpha_list)):
            self.alpha_order[temp_alpha_list[index]] = index / len(temp_alpha_list)
        self.head.sort(key=lambda x: self.support[x.item] + self.alpha_order[x.item], reverse=True)
        file.seek(0)
        line_1 = file.readline()  # 第二次读取文件，构造FP树
        while line_1:
            current_leaf = self.tree  # 返回树根
            transaction_1 = line_1.split(',')
            transaction_1[-1] = transaction_1[-1][:-1]
            transaction_2 = [item_4 for item_4 in transaction_1 if item_4 in self.support]
            transaction_2.sort(key=lambda x: self.support[x] + self.alpha_order[x], reverse=True)
            for item_3 in transaction_2:
                if item_3 in current_leaf.next:
                    current_leaf = current_leaf.next[item_3]
                    current_leaf.frequency += 1
                else:
                    current_leaf.next[item_3] = Leaf(item_3)
                    temp = current_leaf
                    current_leaf = current_leaf.next[item_3]
                    current_leaf.last = temp
                    current_leaf.frequency += 1
                    for heads in self.head:
                        if heads.item == item_3:
                            heads.leaf_link.push_back(current_leaf)
                            break
            line_1 = file.readline()

    def frequent_pattern(self):  # 挖掘所有频繁项集
        frequent_pattern = [[]]

        def projection_tree(head, tree):  # 构造投影数据的条件FP树
            node = head.leaf_link.head
            pro_tree = FPTree(sup=tree.sup)
            pro_tree.alpha_order = tree.alpha_order
            while node is not None:
                leaf = node
                temp_sup = node.frequency  # 投影数据集的支持度由FP树最下面的元素决定
                while leaf.last:
                    if leaf.item in pro_tree.support:
                        pro_tree.support[leaf.item] += temp_sup
                    else:
                        pro_tree.support[leaf.item] = temp_sup
                    leaf = leaf.last
                node = node.successor
            raw_list = [item_0 for item_0 in pro_tree.support.keys()]
            for item_1 in raw_list:
                if pro_tree.support[item_1] >= pro_tree.sup:
                    if item_1 != head.item:
                        head_0 = Head(item_1)
                        head_0.frequency = pro_tree.support[item_1]
                        pro_tree.head.append(head_0)
                else:
                    pro_tree.support.pop(item_1)
            pro_tree.head.sort(key=lambda x: pro_tree.support[x.item]+self.alpha_order[x.item], reverse=True)
            node = head.leaf_link.head

            while node is not None:
                current_leaf = pro_tree.tree
                temp_sup = node.frequency
                leaf = node
                stack = []
                while leaf.last:
                    if leaf.item != head.item:
                        stack.append(leaf)
                    leaf = leaf.last
                stack = [item_2 for item_2 in stack if item_2.item in pro_tree.support]
                stack.sort(key=lambda x: pro_tree.support[x.item] + pro_tree.alpha_order[x.item], reverse=True)
                while stack:
                    original_leaf = stack.pop()
                    if original_leaf.item in current_leaf.next:
                        current_leaf.next[original_leaf.item].frequency += temp_sup
                    else:
                        current_leaf.next[original_leaf.item] = Leaf()
                        temp = current_leaf
                        current_leaf = current_leaf.next[original_leaf.item]
                        current_leaf.frequency = temp_sup
                        current_leaf.last = temp
                        for heads in pro_tree.head:
                            if heads.item == current_leaf.item:
                                heads.leaf_link.push_back(current_leaf)
                                break
                node = node.successor
            if pro_tree.support:
                pro_tree.support.pop(head.item)

            return pro_tree

        if self.tree.next:
            for index in range(len(self.head)):  # 递归获得频繁项集
                con_fp = projection_tree(self.head[-1-index], self)
                temp_pattern = con_fp.frequent_pattern()
                for FP in temp_pattern:
                    FP.append(self.head[-1-index].item)
                frequent_pattern += temp_pattern
        return frequent_pattern
