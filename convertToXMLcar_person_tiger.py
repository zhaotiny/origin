#!/usr/bin/env python
# coding=utf-8
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
from os import listdir
from os.path import isfile, join
from operator import itemgetter
from scipy import misc
import pdb as pdb
import os
import json
#print etree.tostring(root)
#tree.write(open('person.xml', 'w'))
car_name = ['Car','Van', 'Truck', 'Tram']
person_name = ['Pedestrian', 'Person_sitting']
dict_name = {1: 'Car', 2 : 'pedestrian', 3: 'cyclist', 20 : 'traffic lights'}
def extractXML(name, labels, imageAdd):
    image_name = name
    root = Element('annotation')

   # pdb.set_trace()
    ##### folder
    folder = Element('folder')
    folder.text = 'VOC2007'
    root.append(folder)
    ##### filename
    filename = Element('filename')
    filename.text = image_name
    root.append(filename)
    ##### source
    source = Element('source')
        ##### database
    database = Element('database')
    database.text = 'The VOC2007 Database'
    source.append(database)
        ##### annotation
    annotation = Element('annotation')
    annotation.text = 'PASCAL VOC2007'
    source.append(annotation)
        ##### image
    image = Element('image')
    image.text = 'flickr'
    source.append(image)
        ##### flickrid
    flickrid = Element('flickrid')
    flickrid.text = '341012865'
    source.append(flickrid)
    root.append(source)
    #pdb.set_trace()
    
    ##### owner
    owner = Element('owner')
        ##### flickrid
    flickrid1 = Element('flickrid')
    flickrid1.text = 'Fried Camels'
    owner.append(flickrid1)
        ##### name
    name = Element('name')
    name.text = 'Jinky the Fruit Bat'
    owner.append(name)
    root.append(owner)
    #pdb.set_trace()
    img = misc.imread(imageAdd +  '/' + image_name)

    ##### size
    size = Element('size')
        ##### width
    width = Element('width')
    width.text = str(img.shape[1])
    size.append(width)
        ##### height
    height = Element('height')
    height.text = str(img.shape[0])
    size.append(height)
        ##### depth
    depth = Element('depth')
    depth.text = str(img.shape[2])
    size.append(depth)
    root.append(size)

    ##### segmented
    segmented = Element('segmented')
    segmented.text = '0'
    root.append(segmented)
    #pdb.set_trace()
    for k in range(len(labels)):
        tempLine = labels[k]
             #   tempLine = line.strip('\r\n').split(' ')
        ##### object
        object = Element('object')
            ##### name
        name = Element('name')
       # name.text = tempLine[0]
        if (tempLine[4] != 1 and tempLine[4] != 2):
            continue
        name.text = dict_name[tempLine[4]]
        object.append(name)
            ##### pose
        pose = Element('pose')
        pose.text = 'Left'
        object.append(pose)
            ##### truncated
        truncated = Element('truncated')
        truncated.text = '0.0'
        object.append(truncated)
	     ###### difficult
        difficult = Element('difficult')
        difficult.text = '0'
        object.append(difficult)
            ##### bndbox
        bndbox = Element('bndbox')
                ##### xmin
        xmin = Element('xmin')
        xmin.text = str(tempLine[0])
        bndbox.append(xmin)
                ##### ymin
        ymin = Element('ymin')
        ymin.text = str(tempLine[1])
        bndbox.append(ymin)
                ##### xmax
        xmax = Element('xmax')
        xmax.text = str(tempLine[2])
        bndbox.append(xmax)
                ##### ymax
        ymax = Element('ymax')
        ymax.text = str(tempLine[3])
        bndbox.append(ymax)
        object.append(bndbox)
        root.append(object)
  #  tree = ElementTree(root)
    return root


if __name__ == '__main__':
    labelname = 'label.idl'
    #imageAdd = '/media/ting/新加卷/capstone/data/data_object_image/training/image_2'
    saveFileDir = '/home/ting/software/capstone/train_bit_carperson_xml/'
    imageAdd = '/home/ting/software/training/training'
  #  onlyfiles = [f for f in listdir(labelAdd) if isfile(join(labelAdd, f))]
    #pdb.set_trace()
    count = 0
    if (not os.path.exists(saveFileDir)):
        os.mkdir(saveFileDir)
    alllines = []
    f = open(labelname, 'r')
    for line in f:
        tempLine = line.strip('\r\n')
        alllines.append(tempLine)    
    for i in range(len(alllines)):
        dict = json.loads(alllines[i])
        for key, value in dict.iteritems():
            name = key
        root = extractXML(name, dict[name], imageAdd)
        tree = ElementTree(root)
        xmlname = name[:-3] + 'xml'
        #pdb.set_trace()
        tree.write(open(saveFileDir + '/' + xmlname, 'w'))
        count += 1
       # if (count >= 1): break
