from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()
    
setup(
    name='mongogettersetter',
    version='0.1.4',
    author='Sibidharan',
    author_email='sibi@selfmade.ninja',
    description='A handful set of API abstractions for MongoDB with pymongo to access MongoDB document natively over Python Object',
    packages=find_packages(),
    url='https://git.selfmade.ninja/sibidharan/pymongogettersetter',
    install_requires=['pymongo'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
