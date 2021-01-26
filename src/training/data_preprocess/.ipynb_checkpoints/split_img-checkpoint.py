import os
import cv2
import csv

from_dir = 'full_len_data/'
to_dir = '../dataset/'
img_list = []
label_list = []
for root, dirs, files in os.walk(from_dir):
    if root == from_dir:
        img_list.extend([root+f for f in files])
        label_list.extend([f[:4] for f in files])

with open('../labels.csv', 'w', newline='') as csvfile:
    fieldnames = ['img_dir', 'label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    out_name = 0
    for img, label in zip(img_list, label_list):
        img = cv2.imread(img)
        width = img.shape[1]
        for i, l in zip(range(0, width, width//4), label):
            writer.writerow({'img_dir': to_dir[3:]+str(out_name)+'.jpg', 'label': l})
            crop = img[:, i:i+width//4, :]
            cv2.imwrite(to_dir+str(out_name)+'.jpg', crop)
            out_name += 1
