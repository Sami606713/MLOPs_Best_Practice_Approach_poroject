from setuptools import find_packages,setup
def get_requires(path:str)->list:
   with open(path,"r",encoding="utf-16") as f:
      requirement=f.readlines()
   
   requirement=[file.strip() for file in requirement]
   return requirement
        

setup(
    author="Samiullah",
    author_email="sami606713@gmail.com",
    description="Automating Data Science life cycle",
    packages=find_packages(),
    install_requires=get_requires('requirements.txt')
)