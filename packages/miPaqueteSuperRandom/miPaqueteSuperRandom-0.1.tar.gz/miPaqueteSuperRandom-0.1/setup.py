from setuptools import setup, find_packages

setup(
    name='miPaqueteSuperRandom',
    version='0.1',
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
)