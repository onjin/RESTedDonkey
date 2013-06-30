import sys
from setuptools import setup

long_description="""
What is RESTedDonkey?
==========================

For more information, docs and many examples please checkout the `home page`_:

.. _`home page`: https://github.com/onjin/RESTedDonkey
"""


def main():
    install_requires=['ZODB3', 'klein', 'BTrees', 'repoze.catalog']
    setup(
        name='RESTedDonkey',
        description='ZODB based backend with REST access',
        long_description=long_description,
        url='https://github.com/onjin/RESTedDonkey',
        version='0.0.1',
        license='GPLv2 or later',
        platforms=['unix', 'linux', 'osx', 'cygwin', 'win32'],
        author='Marek Wywial',
        author_email='onjinx@gmail.com',
        packages=['donkey', ],
        install_requires=install_requires,
        zip_safe=True,
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License (GPL)',
             'Operating System :: POSIX',
             'Operating System :: Microsoft :: Windows',
             'Operating System :: MacOS :: MacOS X',
             'Topic :: Software Development :: Testing',
             'Topic :: Software Development :: Libraries',
             'Topic :: Utilities',
             'Programming Language :: Python',
             'Programming Language :: Python :: 3'],
    )

if __name__ == '__main__':
    main()
