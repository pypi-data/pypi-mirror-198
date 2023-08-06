#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='cryptos',
      version='2.0.2',
      description='Python Crypto Coin Tools',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      author='Paul Martin',
      author_email='greatestloginnameever@gmail.com',
      url='http://github.com/primal100/pybitcointools',
      packages=find_packages(),
      include_package_data=True,
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Topic :: Security :: Cryptography',
      ],
      entry_points='''
            [console_scripts]
            broadcast=scripts.broadcast:main
            convert_private_key=scripts.convert_private_key:main
            create_private_key=scripts.create_private_key:main
            cryptosend=scripts.cryptosend:main
            explorer=scripts.explorer:main
            get_block_sizes=scripts.get_block_sizes:main
            subscribe=scripts.subscribe:main
            view_private_key_addresses=scripts.view_private_key_addresses:main
            '''
      )
