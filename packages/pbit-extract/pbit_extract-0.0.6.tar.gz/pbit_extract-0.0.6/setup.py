from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 11',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='pbit_extract',
  version='0.0.6',
  description='A model documneter for power bi files',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Ayush Jain',
  author_email='jainaayush051@outlook.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='pbit', 
  packages=find_packages(),
  install_requires=['openpyxl','openai'] 
)