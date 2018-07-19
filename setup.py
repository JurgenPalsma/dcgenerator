from setuptools import setup

setup(name='dcgenerator',
      version='0.1',
      description='Generate dc events from time series',
      url='https://github.com/JurgenPalsma/dcgenerator',
      author='Flying Circus',
      author_email='jurgen.palsma@gmail.com',
      license='MIT',
      packages=['dcgenerator'],
      install_requires=[
          'pandas',
      ],
      zip_safe=False)