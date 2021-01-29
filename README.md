# nsysu-captcha-solver
Captcha solver across websites under [selcrs.nsysu.edu.tw](https://selcrs.nsysu.edu.tw), National Sun Yat-sen University
![](https://media.giphy.com/media/1rX8IEL6WCd7gne9cm/giphy.gif)

## Todo
- [X] Chrome extension
- [ ] Safari extension

## Project Structure
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
## Thanks
Special thanks to
- [楊志璿](https://github.com/25077667) For data collection
- [Paul Peng]() For creative contents
