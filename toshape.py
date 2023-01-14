'''
Author: Wxl
Date: 2023-01-14 13:09:34
LastEditTime: 2023-01-14 13:10:39
LastEditors: Wxl
Description: 
FilePath: /workspace/detectron2/toshape.py
可以输入预定的版权声明、个性签名、空行等
'''
import cv2 
img = cv2.imread("../2022-12-24.png")
img = cv2.resize(img,(1344,1344))
print(img.shape)
cv2.imwrite("sample.jpg",img)