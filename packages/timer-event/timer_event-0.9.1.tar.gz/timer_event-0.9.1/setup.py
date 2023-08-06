from distutils.core import setup

from setuptools import find_packages


setup(
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    download_url='https://github.com/erolyesin/timer_event/archive/refs/tags/v0.9.1-rc02.tar.gz',
)
