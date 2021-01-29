import requests
import time

from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('from_url', help='url of target image')
parser.add_argument('dst_dir', help='output directory')
args = parser.parse_args()

dst_dir = args.dst_dir
if dst_dir[-1] != '/':
    dst_dir+='/'

for i in range(100):
    time.sleep(1)
    img = requests.get(args.from_url).content
    with open(dst_dir+str(i)+'.bmp', 'wb') as f:
        f.write(img)
    print('Get '+str(i))
