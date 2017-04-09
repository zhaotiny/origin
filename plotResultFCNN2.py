#!/usr/bin/env python
# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
import re
def getLoss(file):
    f = open(file, 'r')
    iter = []
    total_loss = []
    rpn_loss_cls = []
    rpn_loss_box = []
    loss_cls = []
    loss_box = []
    count = 1
    for line in f:
        if (re.search(r'loss_cls: [0-9].[0-9]*', line) != None):
            ### find total loss
            str_temp = re.findall(r'total loss: [0-9].[0-9]*', line)[0]
            val = float(re.findall(r'[0-9].[0-9]*', str_temp)[0])
            total_loss.append(val)

            ### find rpn_loss_cls
            str_temp = re.findall(r'rpn_loss_cls: [0-9].[0-9]*', line)[0]
            val = float(re.findall(r'[0-9].[0-9]*', str_temp)[0])
            rpn_loss_cls.append(val)
            
            ### find rpn_loss_box
            str_temp = re.findall(r'rpn_loss_box: [0-9].[0-9]*', line)[0]
            val = float(re.findall(r'[0-9].[0-9]*', str_temp)[0])
            rpn_loss_box.append(val)
            
            ### find loss_cls
            str_temp = re.findall(r' loss_cls: [0-9].[0-9]*', line)[0]
            val = float(re.findall(r'[0-9].[0-9]*', str_temp)[0])
            loss_cls.append(val)
           
            ### find loss_cls
            str_temp = re.findall(r' loss_box: [0-9].[0-9]*', line)[0]
            val = float(re.findall(r'[0-9].[0-9]*', str_temp)[0])
            loss_box.append(val)
            
            ### iter
            iter.append(count)
            count += 1
    return iter, total_loss, rpn_loss_cls, rpn_loss_box, loss_cls, loss_box



if __name__ == '__main__':
    str_file = 'train_driving.out'
    iter, total_loss, rpn_loss_cls, rpn_loss_box, loss_cls, loss_box = getLoss(str_file)
    iter_np = np.asarray(iter)
    total_loss_np = np.asarray(total_loss)
    rpn_loss_cls_np = np.asarray(rpn_loss_cls)
    rpn_loss_box_np = np.asarray(rpn_loss_box)
    loss_cls_np = np.asarray(loss_cls)
    loss_box_np = np.asarray(loss_box)

    plt.figure(1)
    plt.plot(iter_np, total_loss_np)
    plt.title("total loss")
    plt.savefig('total_loss.png')
    
    plt.figure(2)
    plt.plot(iter_np, rpn_loss_cls)
    plt.title("rpn_loss_cls")
    plt.savefig('rpn_loss_cls.png')
    
    plt.figure(3)
    plt.plot(iter_np, rpn_loss_box)
    plt.title("rpn_loss_box")
    plt.savefig('rpn_loss_box.png')
    
    plt.figure(4)
    plt.plot(iter_np, loss_cls)
    plt.title("loss_cls")
    plt.savefig('loss_cls.png')
    
    plt.figure(5)
    plt.plot(iter_np, loss_box)
    plt.title("loss_box")
    plt.savefig('loss_box.png')
    plt.show()
