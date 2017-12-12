from distutils.core import setup
import os

base_dir = os.path.dirname(__file__)
with open(os.path.join(base_dir, "README.rst")) as f:
    long_description = f.read()

setup(
    name='spitslurp',
    version='0.3',
    description='Write text to a file with `spit` and read from a file with `slurp`.',
    author='Matt Walker',
    author_email='walkermatt@longwayaround.org.uk',
    url='https://github.com/walkermatt/spitslurp',
    download_url='https://github.com/walkermatt/spitslurp/archive/0.3.tar.gz',
    packages=['spitslurp'],
    license='MIT',
    keywords=['io', 'file'],
    long_description=long_description
)
