import sys, os
file = open('dblp.xml')
pipe = open('result4.txt', 'w')
s_1 = 'inproceedings'
s_2 = 'proceedings'
sign = 0
for line in file:
    if line[1:14] == s_1 == 'inproceedings' or line[1:12] == s_1 == 'inproceedings':
        sign = 1
    if sign:
        pipe.write(line)
    if line[-15:-2] == s_1 == 'inproceedings' or line[-13:-2] == s_1 == 'inproceedings':
        sign = 0

file.close()
pipe.close()
