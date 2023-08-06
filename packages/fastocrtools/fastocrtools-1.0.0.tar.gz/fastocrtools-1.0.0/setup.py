import setuptools  # 导入setuptools打包工具


setuptools.setup(
    name="fastocrtools",  # 用自己的名替换其中的YOUR_USERNAME_
    version="1.0.0",  # 包版本号，便于维护版本
    author="SpeakerChen",  # 作者，可以写自己的姓名
    author_email="3390988513@qq.com",  # 作者联系方式，可写自己的邮箱地址
    description="OCR",  # 包的简述
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # 对python的最低版本要求
)