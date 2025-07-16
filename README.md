# PRODIGY_CY_02
# 🖼️ Pixel Manipulation Tool

A simple Python tool to scramble and descramble pixels in an image using a key.

## 🔧 Features
- Encrypt (scramble) image pixels using a secret key
- Decrypt (descramble) back to original image
- CLI-ready and modular

## ▶️ Usage

```python
from pix_manip.core import load_image, scramble_pixels, descramble_pixels

img = load_image("your_image.jpg").convert("RGB")
key = "your_secret"

# Encrypt
scrambled = scramble_pixels(img.copy(), key)
scrambled.save("encrypted.png")

# Decrypt
decrypted = descramble_pixels(scrambled.copy(), key)
decrypted.save("decrypted.png")

