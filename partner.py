file_0 = open('final_data.txt')
relation = {}
line = file_0.readline()
while line:
    authors = line.split(sep=',')
    authors[-1]=authors[-1][:-1]
    if len(authors) > 2:
        for index_0 in range(len(authors)-1):
            for index_1 in range(index_0+1, len(authors)):
                author_0 = authors[index_0]
                author_1 = authors[index_1]
                if author_0 > author_1:
                    temp_author = author_1
                    author_1 = author_0
                    author_0 = temp_author
                if (author_0, author_1) in relation:
                    relation[(author_0, author_1)] += 1
                else:
                     relation[(author_0, author_1)] = 1
    line = file_0.readline()
file_0.close()
file_1 = open('relation.txt', 'w')
l = [[relation[keys], keys] for keys in relation]
l.sort(reverse=True)
for t in l:
    file_1.write(t[1][0]+','+t[1][1]+'\t'+str(t[0])+'\n')
file_1.close()