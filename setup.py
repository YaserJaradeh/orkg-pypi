from setuptools import find_packages
from distutils.core import setup
setup(
  name='orkg',
  packages=find_packages(),
  version='0.2',
  license='MIT',
  description='Python wrapper for the Open Research Knowledge Graph (ORKG) API',
  author='Mohamad Yaser Jaradeh',
  author_email='jaradeh@l3s.de',
  url='http://orkg.org/about',
  download_url='https://github.com/YaserJaradeh/orkg-pypi/archive/0.2.tar.gz',
  keywords=['ORKG', 'Scholarly communication', 'API wrapper'],
  install_requires=[
          'hammock',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
  ],
  test_suite='nose.collector',
  tests_require=['nose'],
)