# -- coding:utf-8 --
# Time:2023-03-23 10:50
# Author:XZ
# File:setup.py
# IED:PyCharm

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="XZ_m3u8_xin_zai",
    version="0.0.1",
    author="XZ",
    author_email="345841407@qq.com",
    description="download m3u8 video",
    long_description=long_description,
    # url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
