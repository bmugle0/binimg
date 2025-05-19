#!/usr/bin/env python3

def main():
    from binimg import converter as cnvt

    args = cnvt.get_args()

    bytes = cnvt.get_bin(args.input_path)

    image = cnvt.bin_to_image(bytes)
    meta = cnvt.PngImagePlugin.PngInfo()
    for k, v in image.info.items():
         meta.add_text(k, v)

    image.save(args.output_name, pnginfo=meta)
