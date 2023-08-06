from setuptools import setup, find_packages

setup(
    name='controme',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        # Liste der Abhängigkeiten
    ],
    author='Maximilian Bick',
    author_email='maxibick@hotmail.com',
    description='Module to read from controme API Endpoint',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/maxibick/controme',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)