from setuptools import setup, find_packages

setup(
    name='openhuman',
    version='1.1.3',
    author='OpenHuman',
    author_email='openhuman.ai@gmail.com',
    summary="Virtual human assistant",
    description='OpenHuman: Virtual human assistant',
    license_file="LICENSE",
    install_requires=[
         # List your package's dependencies here
        "numpy"
    ],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/OpenHuman-ai/python-openhuman",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    license="MIT",
    platform="linux",
    packages=find_packages('src/reader', exclude=['test'])
)
