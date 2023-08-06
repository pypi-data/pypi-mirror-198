from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

class PostInstallCommand(install):
    """Comando personalizado para ejecutar después de la instalación"""
    def run(self):
        install.run(self)
        print("¡Bienvenido al paquete mipackage!")
        subprocess.call(['echo', 'El comando personalizado se ha ejecutado correctamente'])

setup(
    name='miPaqueteSuperRandom',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    author='Random guy',
    author_email='random@email.com',
    description='Random description',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='paquete ejemplo',
    cmdclass={
        'install': PostInstallCommand,
    }
)