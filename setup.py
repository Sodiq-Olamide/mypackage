from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_required=['numpy'],
    #url='https://github.com/Sodiq-Olamide/MyPackage'
    #author='Sodiq Ambali'
    author_email='sodiqambali@gmail.com'
)