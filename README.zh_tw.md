# 中山大學選課系統驗證碼破解器

這是一個專門給解析中山大學選課系統驗證碼的破解計。
[selcrs.nsysu.edu.tw](https://selcrs.nsysu.edu.tw), 國立中山大學
![](https://media.giphy.com/media/1rX8IEL6WCd7gne9cm/giphy.gif)

## Todo
- [X] Chrome extension
- [ ] Safari extension

## 專案架構
```shell
.
├── README.md                       # this file
├── README.zh_tw.md                 # the Chinese version
└── src                             
    ├── extension                   # The extension folder
    │   ├── chrome
    │   │   ├── content.js          # content script
    │   │   ├── icons               # The extension icons
    │   │   ├── manifest.json       # manifest file
    │   │   └── tf.min.js           # tensorflow js package
    │   └── safari                  # TBA
    └── neural_network_engine
        ├── data_preprocessing      
        │   ├── full_len_data       # original images
        │   ├── split_img.py        # generate splitted training data and labels
        │   └── utils
        │       ├── get_img.py      # primitive image crawler
        │       ├── model.h5        
        │       └── predict_img.py  # predict single captcha image
        ├── dataset
        ├── labels.csv              # data instance's path & label
        ├── outputs                 # model outputs of train.py
        ├── train.py
        └── train_demo.ipynb
```

## 如何使用
### Chrome 擴充套件
正在申請上架中，你可以透過 [extension_chrome](src/extension_chrome) 下載開發者預覽版。
並且使用於開發者模式。[開發者預覽教學](https://support.google.com/chrome/a/answer/2714278?hl=zh-Hant)

### Safari 擴充套件
開發中。

## 如何訓練
### 0. 安裝環境
#### Arch Linux:
```
sudo pacman -S python-tensorflow-gpu-opt python-opencv python-numpy
```

#### Debian/Ubuntu(deb)
```
sudo apt update
...
```
[Tensorflow 安裝教學](https://www.tensorflow.org/install/docker?hl=zh-tw)
TDB

1. 準備您的原始資料集，並且放至於 [full_len_data](src/neural_network_engine/data_preprocessing/full_len_data)
2. 使用 [split_img.py](src/neural_network_engine/data_preprocessing/split_img.py) 產生訓練資料集與 [labels.csv](src/neural_network_engine/labels.csv). 預設輸出於： [dataset](src/neural_network_engine/dataset).
3. 執行 [train.py](src/neural_network_engine/train.py) 訓練 CNN，其輸出會在 [outputs](src/neural_network_engine/outputs).
4. 此「元老」專案之模型目前放至於 [ernestchu.github.io](https://ernestchu.github.io/files/nsysu-captcha-solver/model_tfjs/model.json)

# 如何貢獻
Fork 此專案并提交請求(Pull request)。

# 授權條款
依原作者 @ernestchu 決定之。

## 致謝
特別感謝
- [25077667](https://github.com/25077667) 資料蒐集
- [Paul Peng]() 創意發想