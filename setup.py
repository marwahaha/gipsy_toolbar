#! /usr/bin/env python
from distutils.core import setup
import sys
reload(sys).setdefaultencoding('Utf-8')


setup(
    name='gipsy_toolbar',
    version='0.0.1',
    author='Guillaume Pousseo',
    author_email='guillaumepousseo@revsquare.com',
    description='Manages a toolbar for admins with shortcuts to easily navigate to most\
                 relevant admin features.',
    long_description=open('README.rst').read(),
    url='http://www.revsquare.com',
    license='BSD License',
    platforms=['OS Independent'],
    packages=['gipsy_toolbar'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 0.0.1 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Documentation',
    ],
    dependency_links=[
        'https://github.com/RevSquare/gipsy_tools#egg=gipsy_tools'
    ],
)
