#!/usr/bin/env python3

from setuptools import setup

setup(
    name='pts_cli',
    version='0.1.1',
    packages=['pts_cli'],
    url='https://git.sr.ht/~martijnbraam/pts_cli',
    license='MIT',
    author='Martijn Braam',
    author_email='martijn@brixit.nl',
    description='End-user CLI utility for the Phone Test System',
    install_requires=[
        'pts-act',
        'requests',
        'paho-mqtt',
    ],
    entry_points={
        'console_scripts': [
            'pts-cli = pts_cli.__main__:main'
        ]
    },
)
