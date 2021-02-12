#include "proc.hpp"
#include <fstream>
#include <functional>
#include <iostream>
#include <random>
#include <sstream>
#include <string_view>
#include <utility>
const int THRESHOLD = 150;

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
    const auto [wid, hei] = std::make_pair(img.width(), img.height());
    double *resp_img = new double[wid * hei];
    img.export_gray_scale_response_image(resp_img);
    for (size_t i = 0; i < hei; i++)
        for (size_t j = 0; j < wid; j++) {
            auto avg =
                ((resp_img[((i - 1) % hei) * wid + (j - 1) % wid] +
                  resp_img[((i - 1) % hei) * wid + j] +
                  resp_img[((i - 1) % hei) * wid + (j + 1) % wid]) +
                 (resp_img[i * wid + (j - 1) % wid] + resp_img[i * wid + j] +
                  resp_img[i * wid + (j + 1) % wid]) +
                 (resp_img[((i + 1) % hei) * wid + (j - 1) % wid] +
                  resp_img[((i + 1) % hei) * wid + j] +
                  resp_img[((i + 1) % hei) * wid + (j + 1) % wid])) /
                9.0 * 256.0;
            char spr = (avg > THRESHOLD) ? 255 : 0;
            img.set_pixel(j, i, spr, spr, spr);
        }

    delete[] resp_img;
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
