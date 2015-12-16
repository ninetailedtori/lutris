#!/usr/bin/python
import os
from distutils.core import setup
from lutris.settings import VERSION

data_files = []

for directory, _, filenames in os.walk(u'share'):
    dest = directory[6:]
    if filenames:
        files = []
        for filename in filenames:
            filename = os.path.join(directory, filename)
            files.append(filename)
        data_files.append((os.path.join('share', dest), files))


setup(
    name='lutris',
    version=VERSION,
    license='GPL-3',
    author='Mathieu Comandon',
    author_email='strider@strycore.com',
    packages=['lutris', 'lutris.gui', 'lutris.util', 'lutris.runners',
              'lutris.installer', 'lutris.migrations'],
    scripts=['bin/lutris'],
    data_files=data_files,
    # FIXME: find a way to install dependencies
    # install_requires=['PyYAML', 'PyGObject'],
    url='https://lutris.net',
    description='Install and play any video game on Linux',
    long_description="""Lutris is a gaming platform for GNU/Linux. It's goal is
    to make gaming on Linux as easy as possible by taking care of installing
    and setting up the game for the user. The only thing you have to do is play
    the game. It aims to support every game that is playable on Linux.""",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPLv3',
        'Programming Language :: Python',
        'Operating System :: Linux',
        'Topic :: Games'
    ],
)
