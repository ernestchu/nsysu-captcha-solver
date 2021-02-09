# nsysu-captcha-solver
驗證碼破解插件，運作於所有在國立中山大學 [selcrs.nsysu.edu.tw](https://selcrs.nsysu.edu.tw) 下的網站。 
### [Chrome 插件](https://chrome.google.com/webstore/detail/%E8%BB%8A%E7%AE%A1%E6%9C%83%E9%82%84%E6%88%91%E9%8C%A2/naodomfadjejcbhdhnhpoffjjiljmnch?hl=en-US&authuser=0)
![](https://media.giphy.com/media/1rX8IEL6WCd7gne9cm/giphy.gif)

## 開發進度
- [X] Chrome 插件
- [ ] Safari 插件

## 專案架構
```shell
.
├── README.md                       # this file
└── src
    ├── extension_chrome
    │   ├── content.js              # content script
    │   ├── manifest.json           # manifest file
    │   └── tf.min.js               # tensorflow js package
    ├── extension_safari            # under construction
    └── neural_network_engine       # train backend engine
        ├── data_preprocessing
        │   ├── full_len_data       # original images
        │   ├── split_img.py        # generate splitted training data and labels
        │   └── utils
        │       ├── get_img.py      # primitive image crawler
        │       └── predict_img.py  # predict single captcha image
        ├── dataset
        ├── labels.csv              # data instance's path & label
        ├── outputs                 # model outputs of train.py
        ├── train.py
        └── train_demo.ipynb
```
## 使用方法
### Chrome 插件
安裝即可使用。
### Safari 插件
開發中。

## 訓練神經網路引擎
1. 將原始尺寸的訓練資料放置 [full_len_data](src/neural_network_engine/data_preprocessing/full_len_data)
2. 使用 [split_img.py](src/neural_network_engine/data_preprocessing/split_img.py) 切割影像以利辨識，並產生標註檔 [labels.csv](src/neural_network_engine/labels.csv). 切割後的影像預設輸出至 [dataset](src/neural_network_engine/dataset).
3. 使用 [train.py](src/neural_network_engine/train.py) 訓練神經網路, 訓練好的目標會在 [outputs](src/neural_network_engine/outputs).
4. 此插件目前使用的已訓練模型目前放置在 [ernestchu.github.io](https://ernestchu.github.io/files/nsysu-captcha-solver/model_tfjs/model.json)

## 感謝
特別感謝
- [楊志璿](https://github.com/25077667) 資料搜集
- [Paul Peng]() 創意發想
