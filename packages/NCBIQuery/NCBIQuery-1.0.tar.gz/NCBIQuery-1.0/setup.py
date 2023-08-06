from setuptools import setup, find_packages

setup(
    name='NCBIQuery',
    version='1.0',
    license='Delt4',
    author="Leo Sun",
    author_email='zidaneandmessi@gmail.com',
    packages=find_packages(),
    url='https://github.com/nachovy/NCBIQuery',
    keywords='NCBI',
    install_requires=[
          'html',
          'requests',
          'tokenizers',
      ],

)