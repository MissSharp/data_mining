file_0 = open('new_data.txt')
line = file_0.readline()
file_1 = open('init', 'w')
conf = {}
while line:
    information = line.split('\t')
    if information[0] not in conf:
        conf[information[0]] = 1
        file_1.close()
        file_1 = open(information[0]+'.txt', 'w')
    file_1.write(information[1]+'\n')
    line = file_0.readline()
file_1.close()
file_0.close()