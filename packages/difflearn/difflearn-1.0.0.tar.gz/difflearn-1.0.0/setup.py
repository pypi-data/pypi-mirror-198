from setuptools import setup, find_packages
setup(
    name='difflearn', # 包的名称
    packages=find_packages(), # 包含的模块
    version='1.0.0',
    author='Jiacheng Leng',
    author_email='amssljc@163.com',
    description='Some useful tools for differential network inference with python.',
    long_description=open('README.txt').read(),
)