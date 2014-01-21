from setuptools import setup

def readme():
    """
        This loads the README.md file.
    """
    with open('README.md') as f:
        return f.read()

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
      url='https://github.com/j-i-l/apipy',
      author='j-i-l',
      author_email='simply.mail.to.j.i.l@gmail.com',
      license='MIT',
      packages=['apipy'],
      install_requires = ['requests'],
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points={
                    'console_scripts': [
                                         'apipy_public_request=apipy.public_request:main'
                                       ],
                    },
      zip_safe=False)


