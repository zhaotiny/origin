#!/usr/bin/env python
# coding=utf-8
from os import listdir
from os.path import isfile, join
from operator import itemgetter
import pdb
import re
if __name__ == '__main__':
 #   folderAdd = '/media/ting/新加卷/capstone/data/data_object_image/testing/image_2'
    folderAdd = '/home/ting/software/training/training'
    saveFileName = 'bittrain.txt'
    saveFileDir = '/home/ting/software/capstone/'
    onlyfiles = [f for f in listdir(folderAdd) if isfile(join(folderAdd, f))]
    onlyfiles.sort()
    print onlyfiles[0:50]
    f = open(saveFileDir + saveFileName, 'w')
    count = 0
    for name in onlyfiles:
        if (re.search(r'.jpg', name) == None):
            continue
        f.write(name[:-4] + '\n')
        count += 1
   # print onlyfiles[0:1000]
    f.close()
    print count
    
