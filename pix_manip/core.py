from PIL import Image
import random

def load_image(path):
    return Image.open(path)

def scramble_pixels(img, key):
    pixels = list(img.getdata())
    random.Random(key).shuffle(pixels)
    img.putdata(pixels)
    return img

def descramble_pixels(img, key):
    width, height = img.size
    pixels = list(img.getdata())
    indexes = list(range(len(pixels)))
    shuffled = indexes[:]
    random.Random(key).shuffle(shuffled)

    # Create reverse mapping
    descrambled = [None] * len(pixels)
    for original, shuffled_idx in enumerate(shuffled):
        descrambled[shuffled_idx] = pixels[original]

    img.putdata(descrambled)
    return img

