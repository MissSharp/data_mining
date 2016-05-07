import FPTree
def is_subset(transaction, other_transaction):
    sign = 1
    for item in other_transaction:
        if not item in transaction:
            sign = 0
            break
    if sign:
        return True
    else:
        return False

file_0 = open('final_data.txt')
fpt = FPTree.FPTree(20)
fpt.in_tree(file_0)
l = fpt.frequent_pattern()
l_1 = []
file_1 = open('frequent_pattern.txt', 'w')
for i in range(len(l)):
    for j in range(i):
        if is_subset(l[i], l[j]) or is_subset(l[j], l[i]):
            pass
        else:
            l_1.append(l[j])
for fp in l:
    ##if len(fp) >= 2:
        for item in fp:
            file_1.write(item+',')
        file_1.write('\n')

file_0.close()
file_1.close()