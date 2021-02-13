# This is the bmp preprocessing library.

## Methods
Use the traditional method to anti-noise of the captcha.

### Idea:
The noise is thinner than real numbers.
Spread the near colors.

## Impl.
Compile to a lib from C++.

## Usage:
Compile to your platform.
### CMAKE
```
mkdir build
cd build
cmake ..
make
```


### C++ demo
```
g++ lib/proc.cpp driver/cpp/main.cpp -std=c++17 -Ofast -o test.elf
./test.elf demo/1372.bmp
```