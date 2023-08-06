from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Lateo Labs fpga access module'
LONG_DESCRIPTION = 'A package that makes it easy to interface with FPGAs'

setup(
    name="llfpga",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Blayne Kettlewell",
    author_email="rbkettlewell@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='FPGA',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)