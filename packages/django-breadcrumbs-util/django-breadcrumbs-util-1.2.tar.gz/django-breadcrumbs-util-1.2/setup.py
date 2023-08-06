from pathlib import Path

from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name='django-breadcrumbs-util',
    version='1.2',
    description='A package that provides a simple way to add breadcrumbs to your Django views',
    author='Hussein Thamer',
    author_email='hussinthamer211@gmail.com',
    url='https://github.com/hosin211/django-breadcrumbs-utils',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)