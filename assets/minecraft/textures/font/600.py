from PIL import Image
import numpy as np

# 1 = foreground (visible), 0 = transparent
pixels = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Convert to a numpy array (0=transparent, 1=visible)
array = np.array(pixels, dtype=np.uint8) * 255  # 255 = visible (white), 0 = transparent

# Create an RGBA image (4 channels: Red, Green, Blue, Alpha)
img = Image.fromarray(array).convert("L")  # First convert to grayscale
img_rgba = img.convert("RGBA")  # Then add an alpha (transparency) channel

# Set transparency: where pixel=0, make alpha=0 (fully transparent)
data = img_rgba.getdata()
new_data = []
for pixel in data:
    if pixel[0] == 0:  # If grayscale value is 0 (black), make transparent
        new_data.append((0, 0, 0, 0))
    else:  # Otherwise, make it black (or any color you like)
        new_data.append((0, 0, 0, 255))  # (R, G, B, A)

img_rgba.putdata(new_data)
img_rgba.save("600.png")
