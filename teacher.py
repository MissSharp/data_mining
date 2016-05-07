# coding: utf-8
##此文件用于挖掘师生关系
file_0 = open('relation.txt')
file_1 = open('active_year.txt')
file_2 = open('teacher.txt', 'w')
line = file_1.readline()
active_year ={}
while line:
    a_y = line.split('\t')
    if len(a_y) == 2:
        a_y[1] = a_y[1][:-1]
        active_year[a_y[0]] = float(a_y[1])
    line=file_1.readline()
i = 0
while i < 10:
    line = file_0.readline()
    pairs = line.split(sep='\t')[0]
    pair = pairs.split(sep=',')
    if len(pair) == 2:
        a = pair[0]
        b = pair[1]
        if a in active_year and b in active_year:
            if active_year[a] > active_year[b]:
                c = a
                a = b
                b = c
            if active_year[b] - active_year[a] >= 10:
                file_2.write(a + ',' + b + '\n')
                i += 1
    if not line:
        break
file_0.close()
file_1.close()
file_2.close()