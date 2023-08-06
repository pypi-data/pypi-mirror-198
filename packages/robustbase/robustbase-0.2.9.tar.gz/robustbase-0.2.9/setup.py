
from setuptools import setup, find_packages
import subprocess
import os

version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

if "-" in version:
    # when not on tag, git describe outputs: "1.3.3-22-gdf81228"
    # pip has gotten strict with version numbers
    # so change it to: "1.3.3+22.git.gdf81228"
    # See: https://peps.python.org/pep-0440/#local-version-segments
    v,i,s = version.split("-")
    version = v + "+" + i + ".git." + s

assert "-" not in version
assert "." in version

assert os.path.isfile("version.py")
with open("VERSION", "w", encoding="utf-8") as fh:
    fh.write("%s\n" % version)

  
# reading long description from file 
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

    
# some more details 
CLASSIFIERS = [ 
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers', 
    'Topic :: Scientific/Engineering :: Mathematics', 
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3',
    ] 
  
# calling the setup function  
setup(name='robustbase', 
      version=version, 
      description='A Python Based Library to Calculate Estimators (Sn, Qn, MAD, IQR)', 
      long_description=long_description, 
      long_description_content_type='text/markdown',
      url='https://github.com/deepak7376/robustbase', 
      author='Deepak Yadav', 
      author_email='dky.united@gmail.com', 
      license='MIT', 
      py_modules=["robustbase"],
      package_dir={'':'src'},
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  
      keywords='Sn Qn MAD IQR',
      python_requires='>=3'

      ) 
