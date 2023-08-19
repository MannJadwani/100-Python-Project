from PIL import Image,ImageFilter
import os

path  = '/imgs'

pathOut='/editedImages'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN)
    
    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathOut}/{clean_name}_edited.jpg')

# you can import images into the /imgs folder and apply 
# whatever effect you want to them.
# this particular code adds sharpness to the images
# their is a lot you can do with this library

# read the docs here:https://pillow.readthedocs.io/en/stable/