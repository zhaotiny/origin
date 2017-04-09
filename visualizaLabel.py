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
import cv2
import matplotlib.pyplot as plt
import numpy as np
#print etree.tostring(root)
#tree.write(open('person.xml', 'w'))

if __name__ == '__main__':
    labelAdd = '/media/ting/新加卷1/capstone/data/data_object_image/training/label_2'
    imageAdd = '/media/ting/新加卷1/capstone/data/data_object_image/training/image_2'
    #saveFileName = 'kitti_train.txt'
    saveFileDir = '/home/ting/software/capstone/groundtruth/'
    onlyfiles = [f for f in listdir(labelAdd) if isfile(join(labelAdd, f))]
    if (not os.path.exists(saveFileDir)):
        os.mkdir(saveFileDir)
    count = 1
    for nametxt in onlyfiles:
  #      root = extractXML(name, labelAdd, imageAdd)
        img_name_s = nametxt[:-4] + '.png'
        img_name = imageAdd + '/' + img_name_s
        im2 = cv2.imread(img_name)
        im2 = im2[:, :, (2, 1, 0)]
        fig, ax = plt.subplots(1)
        ax.imshow(im2)
       # ax.imshow(im2, aspect = 'equal')
        file = open(labelAdd + '/' + nametxt, 'r')
        for line in file:
            lineTemp = line.strip('\r\n').split(' ')
            tag = lineTemp[0]
         #   prob = float(lineTemp[8])
            x_min = int(float(lineTemp[4]))
            y_min = int(float(lineTemp[5]))
            x_max = int(float(lineTemp[6]))
            y_max = int(float(lineTemp[7]))
            score = float(lineTemp[-1])
            ax.add_patch(
                plt.Rectangle((x_min, y_min), 
                              x_max - x_min,
                             y_max - y_min, fill = False,
                             edgecolor = 'red', linewidth = 3.5))
            if (tag == 'DontCare'):
                continue
                #ax.text(x_min, y_min - 2,
                 #       '{:s}'.format(tag),
                  #     bbox = dict(facecolor = 'blue', alpha = 0.5),
                   #    fontsize = 6, color = 'white')
            else:
                ax.text(x_min, y_min - 2, 
                       '{:s} {:.3f}'.format(tag, score),
                       bbox = dict(facecolor = 'blue', alpha = 0.5), 
                       fontsize = 6, color = 'white')
        plt.axis('off')
        plt.tight_layout()
        fig.savefig(saveFileDir + nametxt[:-4] + '.jpeg')
       # plt.draw()
        count += 1
       # if (count > 10): break


           # cv2.rectangle(im2, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
           # cv2.rectangle(im2, (x_min, y_min - 20), (x_max, y_min), (125, 125, 125), -1)
    
        count += 1
        #if (count >= 1): break
