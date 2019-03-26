from setuptools import find_packages,setup

with open('README.md','r') as f:
    description = f.read()

setup(
        name = 'pgbackup',
        version = '0.1.0',
        author='Saketh Jakkula',
        author_email='sakethjakkula642@gmail.com',
        description='A utility for backing up PostgreSQL databases',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/saketh-linux/pgbackup',
        packages=find_packages('src')
        )
