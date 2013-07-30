from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
	name = 'packer',
    version = '0.1.0',
	description = 'A new type of package manager',
	long_description=readme(),
	url = 'http://github.com/kalail/packer',
	author = 'kalail',
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