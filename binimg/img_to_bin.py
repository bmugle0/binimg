#!/usr/bin/env python3

def main():
    from binimg import converter as cnvt

    args = cnvt.get_args()

    image = cnvt.Image.open(args.input_path)

    bytes = cnvt.image_to_bin(image)

    with open(args.output_name, "wb") as file:
        file.write(bytes)
