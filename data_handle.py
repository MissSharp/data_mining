##file_0 = open('data1.txt')
##ile_1 = open('new_data.txt','w')
file_0 = open('new_data.txt')
file_1 = open('final_data.txt','w')
line = file_0.readline()
while line:
    information = line.split('\t')
    file_1.write(information[1][:-1]+'\n')
    line = file_0.readline()

file_0.close()
file_1.close()
