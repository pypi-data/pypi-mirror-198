# -*- coding: utf-8 -*-
# author: 华测-长风老师
# file name：setup.py
from setuptools import setup, find_packages

setup(
    name="HCTest_WechatRobot",
    version="0.1",
    description="向你的企业微信发送消息，支持文本，富文本，markdown，图片，文件等",
    author="cf",
    author_email="dingjun_baby@yeah.net",
    url="https://github.com/pypa/sampleproject",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)
