from setuptools import setup, find_packages

from genoforge import __version__

setup(
    name='genoforge',
    version=__version__,

    url='https://github.com/Jorgelzn/Genoforge',
    author='Jorge Lizcano',
    author_email='jorgelizgo@gmail.com',

    packages=find_packages(exclude=['tests', 'tests.*']),

    install_requires=[
        'numpy',
    ],
    extras_require = {
        'dev': [
            'pytest>=4',
            'pytest-cov>=2'
        ],
    }
)