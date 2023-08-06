from setuptools import setup

setup(
    name = 'csvsolar',
    version = '0.1.0',
    entry_points = {
        'console_scripts': [
            'csvsolar = csvsolar.main:main'
        ]
    })