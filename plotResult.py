#!/usr/bin/env python
# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
import re
def getLoss(file):
    f = open(file, 'r')
    iter = []
    loss = []
    count = 1
    for line in f:
        if (re.search(r'loss_cls: [0-9].[0-9]*', line) != None):
            #str_temp = re.findall(r'total loss: [0-9].[0-9]*', line)[0]
            str_temp = re.findall(r'loss_cls: [0-9].[0-9]*', line)[0]
            val = float(re.findall(r'[0-9].[0-9]*', str_temp)[0])
            iter.append(count)
            loss.append(val)
            count += 1
    return iter, loss



if __name__ == '__main__':
    str_file = 'train_driving.out'
    iter, loss = getLoss(str_file)
    iter_np = np.asarray(iter)
    loss_np = np.asarray(loss)
    plt.figure(1)
    plt.plot(iter_np, loss_np)
    plt.savefig('train_driving.png')
    plt.show()
