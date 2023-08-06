from setuptools import setup, find_packages

setup(
    name='smashing',
    version='0.1',
    description='A library for hashing and encrypting data',
    author='Mark Basumatary',
    author_email='markorniginal5@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='hash encryption',
    packages=find_packages(),
    install_requires=[
        'pycryptodome'
    ],
    python_requires='>=3.6, <4',
)
