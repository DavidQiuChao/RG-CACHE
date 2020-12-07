# RG-CACHE

This project implement the code of paper "Reflectance-Guided,Contrast-Accumulated Histogram Equalization". We use guided-filter[1] to get illumination instead of the relative total variation used in the paper.

## Usage

Run the command "python main.py -i path_to_data", where "path_to_data" is the directory contains pictures to processing.

## Results

The testing data is from the project of LIME[2].

<img src="https://github.com/DavidQiuChao/RG-CACHE/blob/main/7.jpg" width = "450" height = "450" alt="pic1"/><img src="https://github.com/DavidQiuChao/RG-CACHE/blob/main/3.jpg" width = "450" height = "450" alt="pic2"/>
<img src="https://github.com/DavidQiuChao/RG-CACHE/blob/main/2.jpg" width = "450" height = "450" alt="pic3"/><img src="https://github.com/DavidQiuChao/RG-CACHE/blob/main/5.jpg" width = "450" height = "450" alt="pic4"/>    






## Reference

[1] K. He, J. Sun, and X. Tang, “Guided image filtering,” in Proc. European Conference on Computer Vision (ECCV), Greece, Sep. 2010, pp. 1–14.

[2] X. Guo, Y. Li, and H. Ling, “LIME: Low-light image enhancement via illumination map estimation,” IEEE Trans. Image Processing, vol. 26, no. 2, pp. 982–993, 2017
