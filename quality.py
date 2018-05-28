import PIL
from PIL import Image
import numpy as np
import os

output_dir = 'tensor'

dir = '/Users/chloewang/Desktop/Images/new_pics'

output_dir = 'quality'

quality = 0

for file in os.listdir(dir):
        #print(file)
        im = Image.open('/Users/chloewang/Desktop/Images/new_pics/'+file)
        im.save('/Users/chloewang/Desktop/Images/quality/'+file, quality=90, optimize=True)
        for i in range (0, 11):
                Image.open('/Users/chloewang/Desktop/Images/quality/'+ file).save('/Users/chloewang/Desktop/Images/quality/'+file, quality=30+quality)
                quality += 5
                #print(str(30 + quality))
