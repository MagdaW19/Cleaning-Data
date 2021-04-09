from setuptools import setup, find_packages

setup(
    name='Education_Stats',
    version='1.0.0',
    packages=find_packages(include=['education', 'education.*']),
    author='Magda Wójcicka',
    install_requires=['folium>=1.19.2', 'pandas>=1.2.3', 'matplotlib>=3.3.4', 'seaborn>=0.11.1']
)