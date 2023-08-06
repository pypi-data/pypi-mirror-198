import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setuptools.setup(
    name='ApReusable',
    version='1.2.4',
    description='Core system functions',
    long_description="long_description",
    long_description_content_type='text/markdown',
    url='https://github.com/aamarpay-core/AP-Reusable-Package',
    author='Rafat & Billah',
    author_email='masumbillahsanjid@gmail.com',
    license='MIT',
    classifiers=classifiers,
    packages=setuptools.find_packages(),
    install_requires=requirements
)
