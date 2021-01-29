# nsysu-captcha-solver
[中文版](README.zh_tw.md)
Captcha solver across websites under [selcrs.nsysu.edu.tw](https://selcrs.nsysu.edu.tw), National Sun Yat-sen University
![](https://media.giphy.com/media/1rX8IEL6WCd7gne9cm/giphy.gif)

## Todo
- [X] Chrome extension
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
The extension is currently pending review, however you can download [extension_chrome](src/extension_chrome) and use it in the developer mode.
### Safari extension
Currently under construction.

## Train backend CNN engine
1. Prepare your training images and place them under [full_len_data](src/neural_network_engine/data_preprocessing/full_len_data)
2. Use [split_img.py](src/neural_network_engine/data_preprocessing/split_img.py) to generate processed training data and [labels.csv](src/neural_network_engine/labels.csv). The default output directory is [dataset](src/neural_network_engine/dataset).
3. Run [train.py](src/neural_network_engine/train.py) to train the CNN, the output model will be under [outputs](src/neural_network_engine/outputs).
4. The model in this project currently using is hosted under [ernestchu.github.io](https://ernestchu.github.io/files/nsysu-captcha-solver/model_tfjs/model.json)

## Thanks
Special thanks to
- [楊志璿](https://github.com/25077667) For data collection
- [Paul Peng]() For creative contents
