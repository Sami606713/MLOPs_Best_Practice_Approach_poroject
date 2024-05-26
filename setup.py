from setuptools import find_packages,setup
def require(path):
    with open(path,"r") as f:
        return f.read().splitlines()

setup(
    author="Samiullah",
    author_email="sami606713@gmail.com",
    description="Automating Data Science life cycle",
    packages=find_packages(),
    install_requires=require('requirements.txt')
)