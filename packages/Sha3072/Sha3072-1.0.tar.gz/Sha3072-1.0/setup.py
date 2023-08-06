from setuptools import setup, find_packages

setup(
    name='Sha3072',
    version='1.0',
    description='SHA-3072 algorithm library',
    author='Mark Basumatary',
    author_email='markorniginal5@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pycryptodome>=3.10.1'
    ]
)
