from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup

setup(
        name='KivyMD Components',
        version='0.1.4',
        license='MIT',
        author='Kivy Team',
        description='Script for installing additional components for the KivyMD library',
        packages=['components'],
        scripts=['bin/components', 'bin/components.bat'],
        install_requires=['requests'],
        )
