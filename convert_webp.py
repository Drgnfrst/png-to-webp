from PIL import Image
import PIL
import os


def covert_to_webp(path):
    files=os.listdir(path)
    if not os.path.isdir('Coverted_Images'):
        os.makedirs("Coverted_Images")
    for file in files:
        im=Image.open(path+r"\{}".format(file)).convert("RGB")
        im.save("Coverted_Images\\{}.webp".format(file),"webp")
        
