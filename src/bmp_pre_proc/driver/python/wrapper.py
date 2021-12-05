#!/usr/bin/python3
import cppyy

cppyy.include('../../lib/proc.hpp')
cppyy.load_library('../../libanti_noise.so')


def do_anti(filename):
    # Return a filename, which is anti-noised.
    return cppyy.gbl.f_anti_noise(filename)


if __name__ == '__main__':
    print("No, this is a interface wrapper.")
