def page_rank(s):
    file_0 = open(s)
    degree = {}
    relation = {}
    line = file_0.readline()
    while line:
        authors = line.split(sep=',')
        authors[-1]=authors[-1][:-1]
        if len(authors) > 2:
            for author in authors:
                if not author in relation:
                    relation[author] = {}
                for author_3 in authors:
                    if author_3 == author:
                        pass
                    else:
                        if author_3 in relation[author]:
                            relation[author][author_3] += 1
                        else:
                            relation[author][author_3] = 1
                if author in degree:
                    degree[author] += 1
                else:
                    degree[author] = 1
        line = file_0.readline()
    file_0.close()

    PR = {author_4: 1 for author_4 in degree}

    def difference(PR_1, PR_2):
        diff = 0
        for author in PR_1:
            diff += abs(PR_1[author] - PR_2[author])
        return diff

    def new(PR_1):
        PR_2 = {author_5: 0 for author_5 in PR_1}
        for author_0 in PR_1:
            for author_1 in relation[author_0]:
                PR_2[author_1] += relation[author_0][author_1]/degree[author_0]
        return PR_2

    while True:
        PR_0 = new(PR)
        if difference(PR, PR_0) < 0.01:
            break
        PR = PR_0
    return PR

conf = ['colt.txt', 'cvpr.txt', 'dmkd.txt', 'icdm.txt', 'icml.txt', 'nips.txt', 'pakdd.txt', 'sdm.txt', 'sigir.txt', 'tkde.txt', 'wsdm.txt']
file_1 = open('influence.txt','w')
for name in conf:
    file_1 = open('result ' + name, 'w')
    pr = page_rank(name)
    l = [(pr[author], author) for author in pr]
    l.sort(reverse=True)
    for i in l:
        file_1.write(i[1] + '\n')
    file_1.close()