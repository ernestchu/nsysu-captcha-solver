import requests

dir = '../dataset/'

for i in range(25):
    img = requests.get('https://selcrs.nsysu.edu.tw/menu1/validcode.asp').content
    with open(dir+str(i)+'.bmp', 'wb') as f:
        f.write(img)
