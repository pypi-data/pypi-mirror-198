from setuptools import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='aws-mfa-pt',
    version='0.0.13',
    description='Manage AWS MFA Security Credentials',
    author='Shaun Lawrie',
    packages=['awsmfa'],
    scripts=['aws-mfa'],
    entry_points={
        'console_scripts': [
            'aws-mfa=awsmfa:main',
        ],
    },
    url='https://github.com/shaun-lawrie-ptml/aws-mfa',
    install_requires=['boto3']
)
