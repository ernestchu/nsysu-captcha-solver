import requests
import time

dir = 'training/dataset/'

for i in range(100):
    time.sleep(1)
    img = requests.get('https://selcrs.nsysu.edu.tw/menu1/validcode.asp').content
    with open(dir+str(i)+'.bmp', 'wb') as f:
        f.write(img)
    print('Get '+str(i))
