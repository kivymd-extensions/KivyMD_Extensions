from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup

setup(
        name='KivyMD Components',
        version='0.1.4',
        license='MIT',
        packages=['components'],
        scripts=['bin/components', 'bin/components.bat'],
        install_requires=['requests'],
        )
