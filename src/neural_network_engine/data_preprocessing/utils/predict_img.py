import os
import cv2
import csv
import numpy as np
import tensorflow as tf

from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('model', help='tensorflow model output .h5')
parser.add_argument('src_dir', help='directory contains images to be predicted')
parser.add_argument('dst_dir', help='output directory')
args = parser.parse_args()

encoding = '123456789'
model = tf.keras.models.load_model(args.model);
model.trainable = False
print(model.summary())

from_dir = args.src_dir
to_dir = args.dst_dir
if from_dir[-1] != '/':
    from_dir+='/'
if to_dir[-1] != '/':
    to_dir+='/'


img_list = []
for root, _, files in os.walk(from_dir):
    if root == from_dir:
        img_list.extend([root+f for f in files])

existing_dir = args.dst_dir
exist_list = []
for root, _, files in os.walk(existing_dir):
    if root == existing_dir:
        exist_list.extend([f[:-4] for f in files])

for img in img_list:
    colorful_img = cv2.imread(img)
    img = cv2.imread(img, 0)
    width = img.shape[1]
    label = ''
    for i in range(0, width, width//4):
        crop = img[:, i:i+width//4]
        crop = tf.keras.preprocessing.image.img_to_array(crop)
        crop = np.expand_dims(crop, 0)
        crop = 1 - crop.astype(float)/255
        out = model.predict(crop)
        label += encoding[tf.math.argmax(out, axis=1).numpy()[0]]
    print(label)
    if label in exist_list:
        print('repeated')
        continue
    cv2.imwrite(to_dir+label+'.bmp', colorful_img)
