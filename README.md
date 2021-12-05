# nsysu-captcha-solver
Captcha solver across websites under [selcrs.nsysu.edu.tw](https://selcrs.nsysu.edu.tw), National Sun Yat-sen University
### [Chrome extension](https://chrome.google.com/webstore/detail/%E8%BB%8A%E7%AE%A1%E6%9C%83%E9%82%84%E6%88%91%E9%8C%A2/naodomfadjejcbhdhnhpoffjjiljmnch?hl=en-US&authuser=0)
![](https://media.giphy.com/media/1rX8IEL6WCd7gne9cm/giphy.gif)

[Chinese README](README.zh_tw.md)

## Todo
- [X] Chrome extension
- [X] Firefox extension
- [ ] Safari extension

## Project Structure
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
## Usage
### Chrome extension
Effective immediately after installation
### Safari extension
Currently under construction.

## Train backend CNN engine
1. Prepare your training images and place them under [full_len_data](src/neural_network_engine/data_preprocessing/full_len_data)
2. Use [split_img.py](src/neural_network_engine/data_preprocessing/split_img.py) to generate processed training data and [labels.csv](src/neural_network_engine/labels.csv). The default output directory is [dataset](src/neural_network_engine/dataset).
3. Run [train.py](src/neural_network_engine/train.py) to train the CNN, the output model will be under [outputs](src/neural_network_engine/outputs).
4. The model this project currently using is hosted under the [gh-pages](https://ernestchu.github.io/nsysu-captcha-solver/assets/model_tfjs/model.json) branch.

## Thanks
Special thanks to
- [SCC](https://github.com/25077667) For data collection
- [Paul Peng](https://github.com/paulpeng-popo) For creative contents
