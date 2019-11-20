import os
import cv2
import csv
import sys
import numpy as np
import pandas as pd

csvpath = '/home/nvidia/Image_data/ImgData/'
columns = ['filename', 'steering', 'throttle', 'steering_re']
data = pd.read_csv(os.path.join(csvpath, 'curve.csv'), names=columns)
pd.set_option('display.max_colwidth', -1)
#print(data.head(5))

datapath = '/home/nvidia/Image_data/ImgData/curve/'
image_path = []
steering = []
steering_re = []
for i in range(len(data)):
    index_data = data.iloc[i]
    filename = index_data[0]

    image_path.append(os.path.join(datapath, filename.strip()))
    steering.append(float(index_data[1]))
    steering_re.append(float(index_data[3]))

file = open('/home/nvidia/Image_data/ImgData/curve.csv','a')
comma = ','
for i in range(int(len(image_path))):
    image = cv2.imread(image_path[i], cv2.IMREAD_UNCHANGED)
    img_bright = image * 1.4
    img_dark = image / 1.4
    
    dir, filename = os.path.split(image_path[i])
    filename_B = filename[:-4] + '-B.png'
    filename_D = filename[:-4] + '-D.png'
    cv2.imwrite(dir+'/'+filename_B,img_bright)
    cv2.imwrite(dir+'/'+filename_D,img_dark)

    file.write(filename_B+comma)
    file.write(str(int(steering[i]))+comma)
    file.write(str(298)+comma)
    file.write(str(float(steering_re[i]))+'\n')

    file.write(filename_D+comma)
    file.write(str(int(steering[i]))+comma)
    file.write(str(298)+comma)
    file.write(str(float(steering_re[i]))+'\n')

print('Process Finish')

