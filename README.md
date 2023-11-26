# handwritten-calculator
A convolutional neural network (CNN) which can recognize digits, letters a-f and x, and basic mathematical symbols. 

Dependencies (any version): 
- numpy
- matplotlib
- keras
- tensorflow (if using Apple M1 chip, use tensorflow-macos)
- shutils
- os
- opencv-python

Dataset:
https://www.kaggle.com/datasets/xainano/handwrittenmathsymbols

First import the Handwritten Math Symbols from Kaggle and unzipped the rar file. Next, iterate through dataset folders and 
move only folders containing images of symbols of interest into another folder. 