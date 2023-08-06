'''
Author: liuyixiong@saicmotor.com
Date: 2023-03-20 19:22:37
LastEditors: liuyixiong@saicmotor.com
Description: 
Copyright (c) 2023 by zone/${git_name_email}, All Rights Reserved. 
'''
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="query_client",
    version="0.0.1",
    author="liuyixiong",
    author_email="liuyixiong@saicmotor.com",
    description="A simple query client for pcd label dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://mirrors.sxc.sh/pypi/simple/query_client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'sql_metadata',
        'trino[sqlalchemy]',
    ],
)