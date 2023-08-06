from setuptools import setup

setup(
    name='newsy',
    version='0.1.2',
    description='Summarize news articles on a given topic',
    author='Gowner Jones',
    packages=['newsy'],
    install_requires=[
        'newspaper3k',
        'transformers',
        'GoogleNews',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [
            'newsy=newsy.newsy:main',
        ],
    },

)
