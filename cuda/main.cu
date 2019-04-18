#include <iostream>
#include <string>
#include <cstdlib>
#include <math.h>

#include "../utils/bitmap_image.hpp"


struct Quant {
	short unsigned int R;
	short unsigned int G;
	short unsigned int B;
};

struct Quant quants[10] = {
	{0, 0, 0},
	{127, 0, 0},
	{255, 0, 0},
	{0, 127, 0},
	{0, 255, 0},
	{0, 0, 127},
	{0, 0, 255},
	{127, 0, 127},
	{127, 127, 0},
	{0, 127, 127}
};

struct Quant quantize(int intensity, int levels, double level) {
	for (int i = 0; i < levels; i++) {
		if (intensity > level * i && intensity < level * (i + 1)) {
			return quants[i];
		}
	}
}

int main(int argc, char *argv[]) {
	int levels;
	int threads;

	if (argv[2] != NULL && argc > 2) {
		levels = atoi(argv[2]);
	} else {
		levels = 10;
	}

	printf("Number of levels: %i\n", levels);
	if (levels < 4 || levels > 10) {
		printf("Number of levels must be between 4 and 10\n");
		exit(1);
	}
	double level = 255 / levels;
	std::string file_name("input.bmp");
	bitmap_image image(file_name);

	unsigned char r, g, b;
	unsigned int w = image.width();
	unsigned int h = image.height();
	unsigned char *intensity = new unsigned char[w*h];

	cudaSetDevice(0);
	cudaCheckErrord();

	for (int i = 0; i < w; i++) {
		for (int j = 0; j < h; j++) {
			image.get_pixel(i, j, r, g, b);
			int avg = ((int)r + (int)g + (int)b) / 3;
			intensity[j*w + i] = (unsigned char)avg;
		}
	}
	
	bitmap_image G(file_name);

	for (int i = 0; i < w; i++) {
		for (int j = 0; j < h; j++) {
			unsigned char a = (unsigned char)intensity[j*w + i];
			struct Quant quant = quantize(a, levels, level);
			G.set_pixel(i, j, quant.R, quant.G, quant.B);
		}
	}
	
	G.save_image("output.bmp");
	free(intensity);
	printf("Execution time: %f\n");
	return 0;
}
