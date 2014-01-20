# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from setuptools import setup

# <markdowncell>

# ##About the setup:
# 
# - name: is the name of the package
# 
# 
# - version: specify the package version
# 
# 
# - description: String with short description
# 
# 
# - long_description: String with a longer more detailed description (i guess...)
# 
# 
# - classifiers: list with certain project specific characteristics.
#     Syntax: 'Development Status :: 3 - Alpha',
#     
#     - Development Status: indicate the status of the package
#     - License: inidcate the licenuce
#     - Programming Language (eg. Python :: 2.7)
#     - Topic: give the tobpic
#     - ...
# 
# 
# - keywords: well, some keywords
# 
# 
# - inlcude_package_data: boolean to specify wheter the files specified in MANIFEST.in should be added installed along with the package or not.
# 
# 
# - url: link to the package (source?)
# 
# 
# - author: the author
# 
# 
# - author_mail: ...
# 
# 
# - licence: under which licence the package is distributed
# 
# 
# - packages: which packages the package contains (?!)
# 
# - install_requires: a lits of other packages on which this one depends. These packages are installed along.
# 
# - dependency_links: list of packages that are neede but cant be found in PyPi. Give the link.
# 
# 
# - zip_safe: dunno...
# 
# 
# - test_suite: specify what should be used for testing the package. (not sure about how this works at all)
# 
# 
# - test_require: liste with packages that are required for testing.
# 
# 
# - scripts: holds a list of scripts. The scripts need to be specified in the bin/ folder.
# 
# **NOTE** the scripts don't need to be python script, but they can be anything.
# 
# - entry_points: specify entry points of different types.
#     - console_scripts: is used to generate scripts. This is another method to include command line tools (scripts is the first one). The advantage of this metdod lies in the easy testing of a scrit. Read in the scripts part about this.

# <codecell>

def readme():
    """
        This loads the README.md file.
    """
    with open('README.md') as f:
        return f.read()

# <codecell>

setup(name = 'apipy',
      version = '0.1dev',
      description='A package to easy the interactions with the api of various websites.',
      #long_description='Long blabla',
      long_description=readme(),
      keywords='api requests',
      classifiers=[
                   'Development Status :: Under development',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Api interaction',
                   ],
      include_package_data=True,
      url='git...',
      author='j-i-l',
      author_email='simply.mail.to.j.i.l@gmail.com',
      license='MIT',
      packages=['apipy'],
      install_requires = ['requests'],
      test_suite='nose.collector',
      tests_require=['nose'],
      #scripts=['bin/some_code_script',],
      entry_points={
                    'console_scripts': [
                                         'apipy_public_request=apipy.public_request:main'
                                       ],
                    },
      #commented since the address is not valid...
      #dependency_links=[
      #                  'http://github.com/user/repo/tarball/master#egg=package-1.0',
      #                 ]
      zip_safe=False)

# <markdowncell>

# ##Usage
# 
# - python setup.py test
#     - This will run the test suite.
#     
# - python setup.py install
#     - This installs the package on the machine (need sudo on mac ... stupid mac)
#     
# - python setup.py register
#     - This registers the package on PYPI (please assure that the name is lowercase no spaces etc...)
#     
# - python setup.py sdist
#     - This creates a souce distribution
#     
# - python setup.py sdist upload
#     - This uploads the source distribution to PYPI
#     
#     
# Once the souce distribution is uploaded to PYPI the package can be installed using easy_install or better pip:
# 
# $ pip install my_first_package

# <markdowncell>

# ##Scripts:
# 
# There are two ways to create scripts.
# 
# 1. Create a scipt file in bin/ folder and include it in the setup.py by adding the path to it in scripts=[... 
# 
# 2. Use an 'entry point'. For this method we write a small python script in the root (eg. command_line_example.py) that defines a main in which it is done what the script should do, eg:
#         import my_first_package
#         def main():
#             print my_first_package.some_code()
#   Then the script is added in the setup.py like so:
#   entry_points={'console_scripts': ['some_code_console_script=my_first_package.command_line_example:main'],}
#   
#   Note that also in the tests it is tested if the main of command_line_example executes correctly (not sure how exactly this test is done though...)

# <markdowncell>

# ##Adding no .py files
# 
# This is easy, simply specify each file you would like to be installed along with the package in MANIFEST.in. Eg.
# 
#     include README.rst
#     include docs/*.txt
#     
# **NOTE** if you need some data for you package put them inside the package folder, not in the root folder, so here it should be in my_first_package/my_first_package/some_data.json
# 
# **NOTE2** If the data should be copied to the package folder, you need to include 
# 
#         include_package_data=True
#         
# in the setup.py

# <markdowncell>

# ##.gitignore file
# 
# In the source forlder there should be a this file. It contains all the files/extentions that should be ignored when installing the package.

# <codecell>


