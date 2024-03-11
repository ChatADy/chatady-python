from setuptools import setup, find_packages

setup(
    name='chatady',
    version='1.0.0',
    author='Jernej Pregelj',
    author_email='contact@chatady.com',
    description='A Python wrapper for the ChatADy API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ChatADy/chatady-python',
    packages=find_packages(),
    install_requires=[
        'requests>=2.31.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)