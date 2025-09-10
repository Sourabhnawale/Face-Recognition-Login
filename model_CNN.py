
import os

from PIL import Image
from numpy import *



# input image dimensions
img_rows, img_cols = 64, 64

# number of channels
img_channels = 1

#%%
#  data

path1 = 'D:/100% not Runnable code/Authentication person/PhotoData/PhotoData/3'    #path of folder of images    
path2 = 'D:/100% not Runnable code/Authentication person/testing_set/3'  #path of folder to save images    

listing = os.listdir(path1)
num_samples=size(listing)
print(num_samples)

for file in listing:
    im = Image.open(path1 + '\\' + file)  
    img = im.resize((img_rows,img_cols))
    gray = img.convert(mode='RGB')
                #need to do some more processing here          
    gray.save(path2 +'\\' +  file, "JPEG")

imlist = os.listdir(path2)

im1 = array(Image.open('dataset/test/0' + imlist[0])) # open one image to get size
m,n = im1.shape[0:2] # get the size of the images
imnbr = len(imlist) # get the number of images

