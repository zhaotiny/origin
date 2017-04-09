#!/usr/bin/env python
# coding=utf-8
import os
import re
car_name = ['Car','Van', 'Truck', 'Tram']
person_name = ['Pedestrian', 'Person_sitting']
if __name__ == '__main__':
    GT = '/home/ting/software/capstone/devkit_object/cpp/data/data_object_image/training/label_2'
    GT2 = '/home/ting/software/capstone/devkit_object/cpp/data/data_object_image/training/label_carperson'
    files = [file for file in os.listdir(GT) if re.search(r'.txt', file) != None]
    if (not os.path.exists(GT2)):
        os.mkdir(GT2)
    for file in files:
        file_abs = os.path.join(GT, file);
        file_save = os.path.join(GT2, file);
        f = open(file_abs, 'r');
        f2 = open(file_save, 'w')
        for line in f:
            line_temp = line.strip('\r\n').split(' ')
            if (line_temp[0] in car_name):
                line_temp[0] = 'Car'
            elif (line_temp[0] in person_name):
                line_temp[0] = 'Pedestrian'
            elif (line_temp[0] == 'DontCare'):
                pass
            else:
                continue;
            newline = ""
            for j in range(len(line_temp)):
                newline += line_temp[j] + " "
            newline = newline.strip(' ')
            newline += '\n'
            f2.write(newline)
        f.close()
        f2.close()



