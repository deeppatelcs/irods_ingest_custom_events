from setuptools import setup, find_packages
import os

# Get package version
version = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'version.py')) as file:
    exec(file.read(), version)

setup(
    name='irods_ingest_custom_events',
    version=version['__version__'],
    url='',
    license='BSD',
    author='Deep Patel',
    author_email='deeppatel.cs@gmail.com',
    description='A python module for using iRODS ingest framework with custom event handlers',
    long_description=open("README.md").read(),
    keywords=["Custom event handlers"],
    classifiers=[
        "Environment :: Console",
        "Development Status :: 3 - Alpha",
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        'Operating System :: POSIX :: Linux',
        "Environment :: Other Environment",
        "Topic :: Utilities",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Filesystems",
    ],

    packages=find_packages(),
    include_package_data=True,
    install_requires=[open("requirements.txt").read()]
)

