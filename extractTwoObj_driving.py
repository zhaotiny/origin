#!/usr/bin/env python
# coding=utf-8
from os import listdir
from os.path import isfile, join
from operator import itemgetter
import pdb
import os
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
import xml.etree.ElementTree as ET
from sets import Set
import re
if __name__ == '__main__':
    folderAdd = './driving_all_200k/';
    folderSave = './driving_car_200k/'
    saveFileName = 'train_driving.txt'
    saveFileDir = '/home/ting/software/capstone/'
    onlyfiles = [f for f in listdir(folderAdd) if isfile(join(folderAdd, f))]
    onlyfiles.sort()
    if (not os.path.exists(folderSave)):
        os.makedirs(folderSave)
    print onlyfiles[0:10]
   # f = open(saveFileDir + saveFileName, 'w')
    count = 0
    objs_name = Set()
    for name in onlyfiles:
        if (re.search(r'.xml', name) == None):
            continue
        filename1 = os.path.join(folderAdd, name)
        tree = ET.parse(filename1)

        root = Element('annotation')
        folder = tree.find('folder')
        filename = tree.find('filename')
        source = tree.find('source')
        size = tree.find('size')
        segmented = tree.find('segmented')
        objects = tree.findall('object')
        
        root.append(folder)
        root.append(filename)
        root.append(source)
        root.append(size)
        root.append(segmented)

        for object in objects:
            if (object.find('name').text == 'car'):
                root.append(object)

        tree_new = ElementTree(root)
        tree_new.write(open(folderSave  + name, 'w'));
        '''
        pdb.set_trace()
        for elem in tree.iter():
            pdb.set_trace()
            print elem.tag, elem.text
        '''
        count += 1
        #if (count >= 1): break
   # print onlyfiles[0:1000
    print count
    print objs_name
    
