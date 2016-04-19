"""Setup script for scarab."""
from setuptools import setup

setup(
    name='scarab',
    version='0.1.0',
    author='Esben Sonne',
    author_email='esbensonne+code@gmail.com',
    description='Static site toolkit',
    url='https://github.com/cknv/scarab',
    license='MIT',
    packages=[
        'scarab',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'Jinja2==2.8',
        'Pillow==3.0.0',
    ],
)
