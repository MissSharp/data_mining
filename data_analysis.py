file = open('final_data.txt')
line = file.readline()
inf = {}
while line:
    authors = line.split(sep=',')
    num = len(authors)
    if num in inf:
        inf[num] += 1
    else:
        inf[num] = 1
    line = file.readline()
file.close()
file = open('author_number.csv', 'w')
l = [(number, inf[number]) for number in inf]
l.sort()
for i in l:
    file.write(str(i[0]) + ',' + str(i[1]) + '\n')
file.close()