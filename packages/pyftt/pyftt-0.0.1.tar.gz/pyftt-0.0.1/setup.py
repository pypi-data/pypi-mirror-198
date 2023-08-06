from setuptools import setup, find_packages
 
classifiers = [
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='pyftt',
  version='0.0.01',
  description='sparse-array partial tracing',
  long_description=open('README.md').read(),
  url='',  
  author='Julio Candanedo',
  author_email='juliojcandanedo@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='', 
  packages=find_packages(),
  install_requires=['numpy'] 
)