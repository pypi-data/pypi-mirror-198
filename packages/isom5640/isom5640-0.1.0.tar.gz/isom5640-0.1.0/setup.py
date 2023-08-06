from setuptools import setup, find_packages

setup(
    name='isom5640',
    version='0.1.0',
    description='Do not distribute it without permission. ',
    author='Xuhu Wan',
    author_email='imwan@ust.hk',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'plotly'
    ],
)
