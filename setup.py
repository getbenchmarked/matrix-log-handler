from setuptools import setup, find_packages

VERSION = '0.3.0'


def readme():
    with open('README.rst') as f:
        return f.read()


def deps():
    with open('requirements.txt') as f:
        return f.read().split('\n')


setup(
    name='matrix_log_handler',
    packages=find_packages('.'),
    version=VERSION,
    description='Log handler sending messages to a Matrix room',
    long_description=readme(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
    ],
    url='https://github.com/getbenchmarked/matrix-log-handler',
    author='Gergely Polonkai',
    author_email='gergely@polonkai.eu',
    keywords=['matrix', 'logging'],
    install_requires=deps(),
    include_package_data=True,
    zip_safe=False)
