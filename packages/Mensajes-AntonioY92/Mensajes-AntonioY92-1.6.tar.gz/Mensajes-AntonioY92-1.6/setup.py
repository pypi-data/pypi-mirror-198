#Contiene la configuracion de la instalacion del distribuible
from setuptools import setup, find_packages

setup(
    name='Mensajes-AntonioY92',
    version='1.6',
    description='Un paquete para saludar',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='AntonioY92',
    author_email='correo@gmail.com',
    url='',
    licens_files=['LICENSE'],
    packages=find_packages(),
    scripts=[],
    test_suite='test',
    install_requires=[paquete.strip() 
                      for paquete in open("requirements.txt").readlines()],
    classifiers=['Environment :: Console',
                 'Intended Audience :: Developers',
                 'Topic :: Utilities']
)