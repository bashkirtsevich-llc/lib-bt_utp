# /usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='lib-bt_utp',
    version=open('VERSION', 'r').read().strip(),
    description="Python 3 bittorrent micro transport protocol implementation",
    long_description=open('README.md', 'r').read().strip(),
    classifiers=["Programming Language :: Python"],
    keywords='',
    author='D.Bashkirtsevich',
    author_email='bashkirtsevich@gmail.com',
    url='https://github.com/bashkirtsevich/lib-bt_utp',
    license='GPL3 License',
    py_modules=['bt_utp'],
    include_package_data=True,
    zip_safe=True,
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
