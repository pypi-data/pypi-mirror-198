import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setuptools.setup(
    name='ApReusable',
    version='1.2.8',
    description='AP-Reusable-Package is a versatile and powerful Python package that contains many useful functions and classes for a wide range of projects.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Rafat & Billah',
    author_email='support@aamarpay.com',
    license='MIT',
    classifiers=classifiers,
    packages=setuptools.find_packages(),
    install_requires=requirements
)
