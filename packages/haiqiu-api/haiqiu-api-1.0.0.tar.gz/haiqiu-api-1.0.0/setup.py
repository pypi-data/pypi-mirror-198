"""
@Author: Rqk
@Date: 2021-05-22
@Description: 
"""

from setuptools import setup, find_packages

version = "1.0.0"
setup(
    name="haiqiu-api",
    version=version,
    keywords=["haiqiu", ],
    description="",
    long_description="",
    license="MIT Licence",
    url="https://gitee.com/renqiukai/haiqiu-api.git",
    author="Renqiukai",
    author_email="renqiukai@qq.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["requests", "loguru"],
)
