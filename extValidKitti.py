#!/usr/bin/env python
# coding=utf-8
import os
import xml.etree.ElementTree as ET

if __name__ == '__main__':
    path = './train_kitti_car_xml'
    f1 = open('kittitrain_train.txt')
  #  files = [f for f in os.listdir(path)]
    count = 0
    f = open('kitti_train_valid_car.txt.txt', 'w')
    for file in f1:
        file = file.strip('\n\r')
        file = file + '.xml'
        filename = os.path.join(path, file)
        tree = ET.parse(filename)
        objs = tree.findall('object')
        if (len(objs) == 0): continue
        count += 1
        f.write(file[:-4] + '\n')
    f.close()
    print count

