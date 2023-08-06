from setuptools import setup, find_packages

setup(
    name='openhuman',
    version='1.1.1',
    author='OpenHuman',
    author_email='openhuman.ai@gmail.com',
    description='OpenHuman: virtual Human for virtual assistant',
    packages=find_packages('src/reader', exclude=['test'])
)
