#ifndef __PROC_HPP__
#define __PROC_HPP__

#include <vector>
#include "bitmap_image.hpp"

// Suppose 3 bytes per pixel
// Store bmp data from memory to storage
Bitmap_image loader(const std::vector<char> &bin_bmp);

// Spread the noise of bmp
Bitmap_image spreader(Bitmap_image img);

// Customize filename
void saver(const Bitmap_image &img, const std::string &filename);
// Return filename for temp
std::string saver(const Bitmap_image &img);

// Returns anti-noise in filename
std::string f_anti_noise(const std::vector<char> &bin_bmp);
std::string f_anti_noise(const std::string &filename);

// Returns anti-noise in vector
// TODO: No file lands on disk
std::vector<char> mem_anti_noise(const std::string &filename);
std::vector<char> mem_anti_noise(const std::vector<char> &bin_bmp);

#endif