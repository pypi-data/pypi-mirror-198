# This file is placed in the Public Domain.


import os


from setuptools import setup


def read():
    return open("README.rst", "r").read()


def mods():
    mod = []
    for file in os.listdir("lib"):
        if not file or 'libobj' in file or "__init__" in file or file.startswith('.'):
            continue
        if file.endswith(".pyc") or file.startswith("__pycache"):
            continue
        mod.append(file[:-3])
    return mod


setup(
    name='libobj',
    version='400',
    url='https://github.com/bthate/libobj',
    author='Bart Thate',
    author_email='bthate@dds.nl', 
    description="python3 object library",
    long_description=read(),
    long_description_content_type='text/x-rst',
    license='Public Domain',
    package_dir={
                  "": "lib",
                 },
    py_modules=mods(),
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
