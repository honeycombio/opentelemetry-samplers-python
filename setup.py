import os

from setuptools import setup, find_packages

BASE_DIR = os.path.dirname(__file__)
VERSION_FILENAME = os.path.join(
    BASE_DIR, "src", "opentelemetry", "ext", "honeycomb", "version.py"
)
PACKAGE_INFO = {}
with open(VERSION_FILENAME) as f:
    exec(f.read(), PACKAGE_INFO)

README_FILENAME = os.path.join(BASE_DIR, "README.md")
with open(README_FILENAME) as f:
    long_description = f.read()

setup(
    name='opentelemetry-ext-honeycomb-samplers',
    description='Honeycomb Samplers for OpenTelemetry',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Honeycomb Authors',
    author_email='solutions@honeycomb.io',
    url='https://github.com/honeycombio/opentelemetry-samplers-python',
    platforms='any',
    license='Apache-2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audiencee :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.4, <4',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'opentelemetry-api>=0.13b0',
        'opentelemetry-sdk>=0.13b0',
        'libhoney>=1.9.0',
    ],
    version=PACKAGE_INFO["VERSION"],
)
