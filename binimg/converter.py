
from PIL import Image, PngImagePlugin
import numpy as np
import argparse

def bin_to_image(input_bin, width=256):

    b_array = np.frombuffer(input_bin, dtype=np.uint8).copy()

    original_length = len(b_array)
    height = (original_length + (width * 4) - 1) // (width * 4)

    b_array.resize((height, width, 4))

    image = Image.fromarray(b_array, mode='RGBA')
    image.info["original_length"] = str(original_length)

    return image

def image_to_bin(input_image):
    array = np.array(input_image)
    original_length = int(input_image.info["original_length"])

    trimmed_array = array[:original_length].tobytes()

    return trimmed_array

def get_bin(input_path):
    with open(input_path, "rb") as file:
        data = file.read()
    return data

def get_args():

    parser = argparse.ArgumentParser(description="A file conversion CLI Program")

    parser.add_argument("input_path", help="Path to the input file")
    parser.add_argument("output_name", help="Name of the output file")

    return parser.parse_args()
