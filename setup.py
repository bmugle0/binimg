from setuptools import setup, find_packages

setup(
    name="binimg",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
	"Pillow"
    ],
    entry_points={
	"console_scripts": [
	    "bin-to-img=binimg.bin_to_img:main",
	    "img-to-bin=binimg.img_to_bin:main"
	]
    }
)
