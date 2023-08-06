from setuptools import setup

DISTNAME = 'DEWAKSS'
VERSION = '1.0.1'
DESCRIPTION = "Denoising Expression data with a Weighted Affinity Kernel and Self-Supervision."
# with open('README.rst') as f:
#     LONG_DESCRIPTION = f.read()
MAINTAINER = 'Andreas Tjarnberg'
MAINTAINER_EMAIL = 'andreas.tjarnberg@nyu.edu'
URL = 'https://gitlab.com/Xparx/dewakss'
DOWNLOAD_URL = 'https://gitlab.com/Xparx/dewakss/-/archive/master/dewakss-master.zip'
LICENSE = 'LGPL'


setup(name=DISTNAME,
      version=VERSION,
      description=DESCRIPTION,
      url=URL,
      author=MAINTAINER,
      author_email=MAINTAINER_EMAIL,
      license=LICENSE,
      packages=['dewakss'],
      python_requires='>=3.6',
      install_requires=[
          'sparse-dot-mkl',
          'umap-learn>=0.5.0',
          'pynndescent',
          'scipy',
          'scikit-learn',
          'leidenalg',
          'pandas',
          'scanpy>=1.5.1',
          'matplotlib',
          'seaborn',
      ],
      zip_safe=False)
