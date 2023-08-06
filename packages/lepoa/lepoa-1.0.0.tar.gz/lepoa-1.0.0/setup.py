from setuptools import setup, find_packages
setup(
    name='lepoa',
    version='1.0.0',
    author='Hernandez Barreto Alan Daleth',
    author_email='alandaleth.hb@gmail.com',
    description='Un generador de lenguajes de programación transpilados.',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'lepoa = src.cli:main'
        ]
    },
    install_requires=[
        'argparse',
        # lista de dependencias requeridas por el proyecto
    ]
)
