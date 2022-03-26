from setuptools import setup, find_packages

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='d2-nip-eval',
    version='0.0.1',
    description='D2 nip-eval is a package aimed to help in providing an API for converting nip expressions into python eval statements',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ezro/d2_nip_to_eval",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10"
    ],
    packages=find_packages(exclude=['tests*']),
    package_data={'': ['*.png']},
    include_package_data=True
)
