#!/usr/bin/env python
# coding=utf-8
import os
import xml.etree.ElementTree as ET

if __name__ == '__main__':
    path = './train_bit_carperson_xml'
    files = [f for f in os.listdir(path)]
    count = 0
    f = open('bitvalidtrain.txt', 'w')
    for file in files:
        filename = os.path.join(path, file)
        tree = ET.parse(filename)
        objs = tree.findall('object')
        if (len(objs) == 0): continue
        count += 1
        f.write(file[:-4] + '\n')
    f.close()
    print count

