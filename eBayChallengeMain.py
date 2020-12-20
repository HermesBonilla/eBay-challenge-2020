#Import statements
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.io import imread

#Plt
plt.style.use('seaborn-whitegrid')

# Set Matplotlib defaults
plt.rc('figure', autolayout=True)
plt.rc('axes', labelweight='bold', labelsize='large',
       titleweight='bold', titlesize=18, titlepad=10)
plt.rc('animation', html='html5')


url = 'https://i.ebayimg.com/00/s/MTYwMFgxMjAw/z/iYYAAOxydgZTJwYc/$_1.JPG?set_id=880000500F'

imArray = imread(url)

print(imArray)
imgplot = plt.imshow(imArray)

#Preprocessing


