#ifndef __PROC_HPP__
#define __PROC_HPP__

#include "bitmap_image.hpp"
#include <vector>

// Suppose 3 bytes per pixel
// Store bmp data from memory to storage
Bitmap_image loader(const std::vector<char> &bin_bmp);

// Spread the noise of bmp
Bitmap_image spreader(Bitmap_image img);

// Customize filename
void saver(const Bitmap_image &img, const std::string &filename);
// Return filename for temp
std::string saver(const Bitmap_image &img);

#endif