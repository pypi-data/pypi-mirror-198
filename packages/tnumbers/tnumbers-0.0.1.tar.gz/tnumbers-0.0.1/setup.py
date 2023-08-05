from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='tnumbers',
  version='0.0.1',
  description='This package gives a list of evens,odds and prime numbers between two numbers(both inclusive)',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/Trimuchinni/tnumbers',  
  author='Trimurthulu Chinni',
  author_email='trimuchinni23@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='evens,even,odds,odd,numbers,number,primes,prime,between,evens between,odds between,primes between', 
  packages=find_packages(),
  install_requires=[''] 
)