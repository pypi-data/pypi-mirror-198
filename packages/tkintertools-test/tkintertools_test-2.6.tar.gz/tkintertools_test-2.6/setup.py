import setuptools

with open("README.md", encoding='utf-8') as readme:
    long_description = readme.read()

setuptools.setup(
    name="tkintertools_test",
    version="2.6",
    author="XiaoKang2022",
    author_email="2951256653@qq.com",
    description="An auxiliary module of the tkinder module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitcode.net/weixin_62651706/tkintertools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mulan Permissive Software License v2 (MulanPSL-2.0)",
        "Operating System :: OS Independent",
    ],
)
