from setuptools import setup, find_packages
def post_install():
    print('¡Bienvenido a miPaquete!')

setup(
    name='miPaqueteSuperRandom',
    version='0.6',
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
        'install': lambda orig, _: orig.run_command('install') + post_install()
    }
)