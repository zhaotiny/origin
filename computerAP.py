#!/usr/bin/env python
# coding=utf-8
import pdb
if __name__ == '__main__':
    str1 = 'stats_car_detection.txt';
 #   str1 = 'stats_pedestrian_detection.txt'
    f = open(str1, 'r')
    for line in f:
        temp = line.strip('\r\n ').split(' ')
        #pdb.set_trace()
        num = len(temp)
        acc = 0.0
        for i in range(0, 41, 4):
            acc += float(temp[i])
        acc = acc / 11.0
        print 'acc', acc
