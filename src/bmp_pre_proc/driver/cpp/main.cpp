#include "../../lib/proc.hpp"

int main(int argc, char *argv[])
{
    Bitmap_image img(argv[1]);
    img = spreader(img);
    img.save_image("a.bmp");
    return 0;
}