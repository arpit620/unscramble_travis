from setuptools import setup, find_packages
import os

long_description='''
Generate dictionary words by unscramblig provided word.
'''

dictionary = os.path.join('data','words_alpha.txt')

setup(
    name='Unscramble',
    version='0.2',
    description='Unscramble a word',
    author='Arpit Gupta',
    author_email='arpit.gupta@ucdconnect.ie',
    url='https://github.com/arpit625/unscramble',
    packages=find_packages(),
    license='MIT',
    # long_description=open('README.MD').read(),
    long_description='Long description goes here',
    install_requires=[
          'tqdm',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # package_data={
        # 'unscramble': ['data/*.txt']
    # },
    # include_package_data=True,
    # data_files=[dictionary],
)

