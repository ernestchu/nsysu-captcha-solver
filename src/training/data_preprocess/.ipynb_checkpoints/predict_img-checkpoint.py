import os
import cv2
import csv
import numpy as np
import tensorflow as tf

encoding = '123456789'
model = tf.keras.models.load_model('model.h5')
model.trainable = False
print(model.summary())

from_dir = 'more_data/400/'
to_dir = 'temp/'
img_list = []
for root, dirs, files in os.walk(from_dir):
    if root == from_dir:
        img_list.extend([root+f for f in files])

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
    cv2.imwrite(to_dir+label+'.bmp', colorful_img)
