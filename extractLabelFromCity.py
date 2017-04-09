#!/usr/bin/env python
# coding=utf-8
import os
import pdb
import re
import json
interests = ['person', 'rider', 'car', 'truck', 'bus', 'on rails', 'motorcycle', 'bicycle', 'caravan', 'trailer']
if __name__ == '__main__':
    count = 0
    #root = '/media/ting/文档/gtFine'
   # savedir = '/media/ting/文档/cityfinexml'
    root = '/media/ting/文档/gtCoarse'
    savedir = '/media/ting/文档/citycoarsexml'
   
    if (not os.path.exists(savedir)):
        os.mkdir(savedir)
    for path, subdirs, files in os.walk(root):
        for name in files:
            if (re.search(r'.json', name) == None):
                continue
            ##### read the json file
            filename =  os.path.join(path, name)
            with open(filename) as file:
                data = json.load(file)

            ##### write it to txt
            savefilename = os.path.join(savedir, name)
            savefilename = savefilename[:-4] + 'txt'
            f = open(savefilename, 'w')

            ##### iterate over each object and select those in our interests
            objects = data['objects']
            numObj = len(objects)
            for i in range(numObj):
                object = objects[i]
                if (object["label"] not in interests):
                    continue
                name = object['label']
                polygon = object['polygon']
                minX = 10000
                minY = 10000
                maxX = 0
                maxY = 0
                for j in range(len(polygon)):
                    point = polygon[j]
                    minX = min(minX, point[0])
                    minY = min(minY, point[1])
                    maxX = max(maxX, point[0])
                    maxY = max(maxY, point[1])
                str1 = name + ' ' + str(minX) + ' ' + str(minY) + ' ' + str(maxX) + ' ' + str(maxY) + '\n'
                f.write(str1)
            f.close()
            count += 1
           # pdb.set_trace()
            #if (count >= 1): break;
    print count 


