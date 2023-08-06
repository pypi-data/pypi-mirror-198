from setuptools import setup

setup(
    name='opiplayer',
    version='0.2.2',
    author='ViDat',
    author_email='tiendatopip@gmail.com',
    description='A music player package for Linux',
    py_modules=['MusicApp'],
    install_requires=[
        'pygame',
        'numpy',
        'Pillow',

    ],
)