

from setuptools import setup, find_packages

setup(
    name='K07VN_Crypto',
    version='1.0.4',
    packages=find_packages(),
    install_requires=[
        'pycryptodome',
    ],
    python_requires='>=3.6',
)
