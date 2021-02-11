#include "proc.hpp"
#include <fstream>
#include <iostream>
#include <string_view>
#include <random>
#include <functional>
#include <utility>
#include <sstream>

static std::string rand_name()
{
    auto seed = rand();
    auto salt = rand();
    auto ext_name = ".bmp";
    std::stringstream ss;
    std::hash<int> h_i;

    ss << std::hex << h_i(seed ^ salt);
    ss << ext_name;

    return ss.str();
}

Bitmap_image loader(const std::vector<char> &bin_bmp)
{
    auto gen_name = rand_name();
    // Write to file
    std::ofstream ofs(gen_name.c_str(), std::ofstream::binary);
    ofs.write(&bin_bmp[0], bin_bmp.size());
    ofs.close();

    return Bitmap_image(gen_name);
}

Bitmap_image spreader(Bitmap_image img)
{
    img.convert_to_grayscale();
    img.invert_color_planes();
    return img;
}

void saver(const Bitmap_image &img, const std::string &filename)
{
    img.save_image(filename);
}

std::string saver(const Bitmap_image &img)
{
    std::string filename(rand_name());
    saver(img, filename);
    return filename;
}
