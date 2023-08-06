from setuptools import setup, find_packages

setup(
    name='NCBIQuery',
    version='0.1',
    license='Delt4',
    author="Leo Sun",
    author_email='zidaneandmessi@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/nachovy/NCBIQuery',
    keywords='NCBI',
    install_requires=[
          'html',
          'requests',
          'xml',
          'tokenizers',
      ],

)