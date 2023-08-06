
from setuptools import setup, find_packages

setup(
  name = 'yotool',
  packages = find_packages(),
  version = '0.1',
  license='MIT',
  description = 'A smart tool for deep learning with Pytorch',
  author = 'Qing Yao',
  keywords = ['tool', 'Pytorch'],
  install_requires=[
     'pynvml>=11.5.0',
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ],
)
