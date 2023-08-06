import setuptools
import os
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name='ccode',
    version='0.0.5',
    author='Mohammed Hamza',
    author_email='eibdhhs0@gmail.com',
    description='A library that encodes and runs any script that has been encrypted through the library in order to preserve the confidentiality of the code and preserve it from theft and preserve the programming rights of the programmer. The Lib99 library is a library that specializes in encryption and uses several offices inside it and uses a special type of encryption that was programmed in 2023 month The third on the 13th',
    long_description=read('README.md'),
    packages=setuptools.find_packages(),
    classifiers=[
        'Operating System :: OS Independent',
        'Natural Language :: Arabic',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License '
    ],
    install_requires=['pycryptodome','bs64','bs32']
)

