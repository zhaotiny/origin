#!/usr/bin/env python
# coding=utf-8
import numpy as np
if __name__== '__main__':
    file = 'kitti_train_all_valid_car.txt'
    f = open(file, 'r')
    list_arr = []
    for line in f:
        line = line.strip('\r\n')
        list_arr.append(line)
    number = len(list_arr)
    random_order = np.random.permutation(number)
    ratio = 8
    train_num = number / ratio
    train_rand = random_order[0: train_num]
    test_rand = random_order[train_num:]

    train_index = [list_arr[i] for i in train_rand]

    file2 = "train.txt"
    f2 = open(file2, 'r')
    all_arr = []
    for line in f2:
        line = line.strip('\r\n')
        all_arr.append(line)

    test_index = []
    for idx in all_arr:
        if (idx not in train_index):
            test_index.append(idx)

    train_file = open('train_split2.txt', 'w')
    test_file = open('test_split2.txt', 'w')
    for line in train_index:
        train_file.write(line + '\n')
    
    for line in test_index:
        test_file.write(line + '\n')
    train_file.close()
    test_file.close()
    f.close()
    f2.close()

