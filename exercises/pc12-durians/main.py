# get data from file
infile = open("INPUT_2.txt", 'r')
RELATIONS = infile.read()[:-2].split(',')
infile.close()

d = dict()
# d => {durian letter : [list of durian letters which are lighter], ...}

# populate dict d with available data
for rel in RELATIONS:
    if rel[1] == '>':
        heavier = rel[0]
        lighter = rel[2]
    else:
        heavier = rel[2]
        lighter = rel[0]

    d[heavier] = d.get(heavier, []) + [lighter]
    # accounting for duplicate values is unnecessary

    # ensure that the lightest durian still has a k:v pair in d
    if lighter not in d:
        d[lighter] = []

# iterate dict values and add other lighter durians by comparison
# e.g. {'e':['f'], 'f':['g'], 'g':[]} => {'e':['f', 'g'], 'f':['g'], 'g':[]}
for durian in d:
    add = []
    for lighter in d[durian]:
        if lighter in d:
            add += d[lighter]
    d[durian] = d[durian] + add

# removing duplicate values is unnecessary

durian_list = []  # list of tuples
# durian_list => [(durian, no. of durians which are lighter), ...]
for durian in d:
    durian_list.append((durian, len(d[durian])))

# sort (bubblesort) from heaviest to lightest,
# by comparing no. of durians in each value list
# NOTE: requires a stable sorting algorithm to maintain relative order, since
# some keys have same number of values
for i in range(len(durian_list)-1):
    for j in range(len(durian_list)-i-1):
        if durian_list[j][1] < durian_list[j+1][1]:
            durian_list[j], durian_list[j+1] = durian_list[j+1], durian_list[j]

print(' '.join(durian[0] for durian in durian_list))
