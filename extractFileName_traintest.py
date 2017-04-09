#!/usr/bin/env python
# coding=utf-8
from os import listdir
from os.path import isfile, join
from operator import itemgetter
import pdb
import random
if __name__ == '__main__':
    folderAdd = '/media/ting/新加卷/capstone/data/data_object_image/training/image_2'
    saveFileName1 = 'kittitrain_train.txt'
    saveFileName2 = 'kittitrain_test.txt'
    saveFileDir = '/home/ting/software/capstone/'
    onlyfiles = [f for f in listdir(folderAdd) if isfile(join(folderAdd, f))]
    onlyfiles.sort()
    random.shuffle(onlyfiles)
    ration = 4
    totalnum = len(onlyfiles)
    trainnum = totalnum / 4
    f = open(saveFileDir + saveFileName1, 'w')
    count = 0
    for i in range(trainnum):
        name = onlyfiles[i]
        f.write(name[:-4] + '\n')
        count += 1
    f.close()
    f = open(saveFileDir + saveFileName2, 'w')
    for i in range(trainnum, totalnum):
        name = onlyfiles[i]
        f.write(name[:-4] + '\n')
        count += 1
    f.close()
    print count, totalnum
        
   # print onlyfiles[0:1000]
    
