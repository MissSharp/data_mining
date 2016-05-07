# coding: utf-8
##��ģ�����ڹ���FPtree���ݽṹ

class Leaf:  # FP���еĽڵ�
    def __init__(self, item=None):
        self.item = item
        self.frequency = 0
        self.last = None  # ���еĸ��ڵ�
        self.next = {}  # �ӽڵ���ֵ䣬������Ϊ����������Ӧ��Leaf����Ϊֵ
        self.successor = None  # ���ӱ��е���һͬ��Leaf����


class LinkLeaves:  # FP������ͬ������ӽṹ������Leaf��successor��Ա����
    def __init__(self):
        self.head = None
        self.tail = None
        self.empty = True

    def push_back(self, ele):  # ���ӱ����������
        if self.empty:
            self.head = ele
            self.tail = ele
            self.empty = False
        else:
            self.tail.successor = ele
            self.tail = self.tail.successor


# ��ͷ�е�Ԫ��
class Head:
    def __init__(self, item):
        self.item = item  # ��ӦԪ�س�Ա
        self.frequency = 0  # ֧�ֶ�
        self.leaf_link = LinkLeaves()  # ��FP���е����ӽṹ


class FPTree:
    def __init__(self, sup):
        self.sup = sup  # ֧�ֶ���ֵ
        self.head = []  # ��ͷ
        self.support = {}  # Ƶ�����֧�ֶ�
        self.tree = Leaf()  # FP������
        self.alpha_order = {}  # ��python�б��Դ����ֵ���������֧�ֶ���ͬ��Ƶ����

    def in_tree(self, file):  # ��һ��ÿһ�����Զ��ŷָ����������ݵ��ļ��й���FP��
        line_0 = file.readline()  # ��һ�ζ�ȡ�ļ�����ȡƵ���������
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
        line_1 = file.readline()  # �ڶ��ζ�ȡ�ļ�������FP��
        while line_1:
            current_leaf = self.tree  # ��������
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

    def frequent_pattern(self):  # �ھ�����Ƶ���
        frequent_pattern = [[]]

        def projection_tree(head, tree):  # ����ͶӰ���ݵ�����FP��
            node = head.leaf_link.head
            pro_tree = FPTree(sup=tree.sup)
            pro_tree.alpha_order = tree.alpha_order
            while node is not None:
                leaf = node
                temp_sup = node.frequency  # ͶӰ���ݼ���֧�ֶ���FP���������Ԫ�ؾ���
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
            for index in range(len(self.head)):  # �ݹ���Ƶ���
                con_fp = projection_tree(self.head[-1-index], self)
                temp_pattern = con_fp.frequent_pattern()
                for FP in temp_pattern:
                    FP.append(self.head[-1-index].item)
                frequent_pattern += temp_pattern
        return frequent_pattern
