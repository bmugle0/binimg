#!/bin/python3

from PIL import Image, PngImagePlugin
import numpy as np

def binary_to_image(input_path, output_path, width=256):
    with open(input_path, "rb") as file:
        data = file.read()

    b_array = np.frombuffer(data, dtype=np.uint8).copy()

    original_length = len(b_array)
    height = (original_length + (width * 4) - 1) // (width * 4)

    b_array.resize((height, width, 4))

    image = Image.fromarray(b_array, mode='RGBA')
    image.show()

binary_to_image("test.txt", "")
