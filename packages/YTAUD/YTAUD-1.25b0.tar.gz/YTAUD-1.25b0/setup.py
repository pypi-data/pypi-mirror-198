from setuptools import setup, find_packages


setup(
    name='YTAUD',
    version='1.25b',
    license='MIT',
    author="liftium",
    author_email='email@liftium.space',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Blagdoii/YTAUD-plugin',
    keywords='YTAUD',
    install_requires=[
          'scikit-learn',
          'youtube_dl',
          'colorama',
      ],

)