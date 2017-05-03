import os
from PIL import Image

folder_images = "dataset"
size_images = dict()

count = 0;
# Remove images with small dimensions
for dirpath, _, filenames in os.walk(folder_images):
    for path_image in filenames:
        image = os.path.abspath(os.path.join(dirpath, path_image))
        with Image.open(image) as img:
            width, heigth = img.size
        if heigth < 200 or width < 200:
            count = count + 1
            os.remove(image)
            size_images[path_image] = {'width': width, 'heigth': heigth}

print(size_images)
print("Count {0}".format(count))