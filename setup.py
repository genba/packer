
import packer.Packer as Packer


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
	name = Packer.name,
    version = Packer.version,
	description = 'A new type of package manager',
	long_description = readme(),
	url = 'http://github.com/kalail/packer',
	author = 'Kashif Malik',
	author_email = 'kashif@kalail.com',
	license = 'MIT',
	packages = [
		'packer'
	],
	install_requires = [
		'requests',
	],
	zip_safe = False
)