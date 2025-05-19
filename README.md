# binimg

**binimg** is a simple Python tool that converts arbitrary binary data (e.g., `.bin`, `.zip`, `.py`) to PNG images and back again. It works by mapping byte values to pixel intensities, optionally storing metadata
---
Disclaimer: This README was written by ChatGPT

## 🛠 Features

- Convert any binary file to an image (`.png`)
- Recover original binary from an image
- Supports odd-sized inputs and padding
- Includes metadata for optional use
- CLI-friendly: install and run from anywhere

---

## 📦 Installation

First, clone the repo and install in development mode:

```bash
git clone https://github.com/bmugle0/binimg.git
cd binimg_tool
pip install -e .
```

---

## 🚀 Usage

### Convert binary → image

```bash
bin-to-img input.bin output.png
```

### Convert image → binary

```bash
img-to-bin input.png output.bin
```

---

## 🧪 Example

```bash
# Convert
bin-to-img example.zip out.png

# Convert back
img-to-bin out.png recovered.zip
```

---

## 📝 Project Structure

```
binimg_tool/
├── binimg/
│   ├── __init__.py
│   ├── converter.py        # Shared logic
│   ├── bin_to_img.py       # CLI entry point
│   └── img_to_bin.py       # CLI entry point
├── requirements.txt
├── setup.py
└── README.md
```

---

## 🧩 Dependencies

- `numpy`
- `Pillow`

All are installed automatically with `pip install -e .`.

---

## 📌 Notes

- Padding is used to ensure the image has square-like dimensions.
- Metadata (like original size) can be embedded in the image and recovered.

---

## ✅ License

MIT License
