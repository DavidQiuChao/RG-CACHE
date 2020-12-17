# RG-CACHE

This project implemented the code of paper "Reflectance-Guided,Contrast-Accumulated Histogram Equalization". Guided-filter[1] was used to get illumination instead of the relative total variation described in the paper.

## Usage

Run the command "python main.py -i path_to_data", where "path_to_data" is the directory contains pictures to processing.

## Results
Testing datas are from the project of LIME[2].


input image|enhance result
----|----
![2in](https://github.com/DavidQiuChao/RG-CACHE/blob/main/figs/2.bmp)|![2out](https://github.com/DavidQiuChao/RG-CACHE/blob/main/figs/2___res.jpg)

![3in](https://github.com/DavidQiuChao/RG-CACHE/blob/main/figs/3.bmp)|![3out](https://github.com/DavidQiuChao/RG-CACHE/blob/main/figs/3_res.jpg)

![5in](https://github.com/DavidQiuChao/RG-CACHE/blob/main/figs/5.bmp)|![5out](https://github.com/DavidQiuChao/RG-CACHE/blob/main/figs/5_res.jpg)

![7in](https://github.com/DavidQiuChao/RG-CACHE/blob/main/figs/7.bmp)|![7out](https://github.com/DavidQiuChao/RG-CACHE/blob/main/figs/7_res.jpg)



<img src="https://github.com/DavidQiuChao/RG-CACHE/blob/main/7.jpg" width = "300" height = "300" alt="pic1"/> <img src="https://github.com/DavidQiuChao/RG-CACHE/blob/main/3.jpg" width = "300" height = "300" alt="pic2"/>
<img src="https://github.com/DavidQiuChao/RG-CACHE/blob/main/2.jpg" width = "300" height = "300" alt="pic3"/> <img src="https://github.com/DavidQiuChao/RG-CACHE/blob/main/5.jpg" width = "300" height = "300" alt="pic4"/>    






## Reference

[1] K. He, J. Sun, and X. Tang, “Guided image filtering,” in Proc. European Conference on Computer Vision (ECCV), Greece, Sep. 2010, pp. 1–14.

[2] X. Guo, Y. Li, and H. Ling, “LIME: Low-light image enhancement via illumination map estimation,” IEEE Trans. Image Processing, vol. 26, no. 2, pp. 982–993, 2017
