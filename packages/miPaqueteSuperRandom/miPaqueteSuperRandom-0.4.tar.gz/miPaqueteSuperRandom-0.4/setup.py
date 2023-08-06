from setuptools import setup, find_packages
from setuptools.command.install import install

def post_install():
    """Comando personalizado para ejecutar después de la instalación"""
    print("¡Bienvenido al paquete mipackage!")

class PostInstallCommand(install):
    """Clase que define el comando personalizado"""
    def run(self):
        install.run(self)
        post_install()
setup(
    name='miPaqueteSuperRandom',
    version='0.4',
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