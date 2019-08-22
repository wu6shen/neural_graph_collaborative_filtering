import numpy as np

item_fre = dict()
item_num = 5702
clk_file = '../data/EComm2/cate_2/train.txt'
user_item = dict()
with open(clk_file) as f:
    for l in f.readlines():
        l = l.strip('\n').split('\t')
        items = [int(i) for i in l[1:]]
        user = int(l[0])
        user_item[user] = []
        for p in items:
            user_item[user].append(p)
            if p not in item_fre:
                item_fre[p] = 0
            item_fre[p] += 1

with open(test_file) as f:
    for l in f.readlines():
        l = l.strip('\n').split('\t')
        items = [int(i) for i in l[1:]]
        user = int(l[0])
        uesr = int

