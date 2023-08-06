from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='poofapi',
    version='1.0.2',
    description='A Python library for interacting with the Poof API',
    author='BreezDev',
    long_description=long_description,
    long_description_content_type='text/plain',
    author_email='itstheplugg@gmail.com',
    url='https://github.com/breezdev/poofapi',
    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)
