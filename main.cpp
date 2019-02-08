#define _SECURE_SCL_DEPRECATE 0
#include <iostream>
#include <string>
#include <cstdlib>
#include <omp.h>
#include <math.h>

#include "bitmap_image.hpp"


int main(void) {
	std::string file_name("input.bmp");
	bitmap_image image(file_name);

	unsigned char r, g, b;
	unsigned int w = image.width();
	unsigned int h = image.height();
	unsigned char *red = new unsigned char[w*h];
	unsigned char *green = new unsigned char[w*h];
	unsigned char *blue = new unsigned char[w*h];
	unsigned char *intensity = new unsigned char[w*h];
	

	for (int i = 0; i < w; i++) {
		for (int j = 0; j < h; j++) {
			image.get_pixel(i, j, r, g, b);
			red[j*w + i] = r;
			green[j*w + i] = g;
			blue[j*w + i] = b;
			int avg = ((int)r + (int)g + (int)b) / 3;
			intensity[j*w + i] = (unsigned char)avg;
		}
	}
	
	bitmap_image G(file_name);
	for (int i = 0; i < w; i++) {
		for (int j = 0; j < h; j++) {
			unsigned char a = (unsigned char)intensity[j*w + i];
			G.set_pixel(i, j, a, a, a);
		}
	}

	G.save_image("output.bmp");
	free(red);
	free(green);
	free(blue);
	free(intensity);
	return 0;
}
