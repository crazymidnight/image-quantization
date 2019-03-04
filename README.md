# image-quantization
## OpenMP implementation
Building: ```g++ cppquant/main.cpp -fopenmp -o quant```

Program takes two parameters:
1. Number of threads
2. Number of quantization levels between 4 and 10

Start quantization: ```./quant 2 7```

## CUDA implementation
Building: ```nvcc cudaquant/main.cpp -o cudaquant```

Program takes number of quantization levels between 4 and 10 as parameter.

Start quantization: ```./cudaquant 7```
