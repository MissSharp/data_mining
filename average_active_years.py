file_0 = open('new_data.txt')
active_years={}
line = file_0.readline()
while line:
    information = line.split(sep='\t')
    authors = information[1].split(sep=',')
    for author in authors:
        if author in active_years:
            active_years[author].append(int(information[2][:-1]))
        else:
            active_years[author] = [int(information[2][:-1])]
    line = file_0.readline()
file_0.close()
file_1 = open('active_year.txt', 'w')
for author_0 in active_years:
    file_1.write(author_0 + '\t' + str(sum(active_years[author_0])/len(active_years[author_0])) + '\n')
file_1.close()