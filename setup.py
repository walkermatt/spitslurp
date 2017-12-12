from distutils.core import setup

setup(
    name='spitslurp',
    version='0.2',
    description='Write text to a file with `spit` and read from a file with `slurp`.',
    author='Matt Walker',
    author_email='walkermatt@longwayaround.org.uk',
    url='https://github.com/walkermatt/spitslurp',
    download_url='https://github.com/walkermatt/spitslurp/archive/0.2.tar.gz',
    packages=['spitslurp'],
    license='MIT',
    keywords=['io', 'file'],
    long_description=open('README.rst').read()
)
