from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='NumberProcessing',
  version='0.0.1',
  description='Processing numbers made easy',
  long_description=open('README.txt').read(),
  url='',  
  author='Robert Jones',
  author_email='robertcwad@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='numbers', 
  packages=find_packages(),
  install_requires=[''] 
)