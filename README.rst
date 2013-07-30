Packer
======

.. image:: https://badge.fury.io/py/packer.png
    :target: http://badge.fury.io/py/packer

.. image:: https://travis-ci.org/kalail/packer.png
	:target: https://travis-ci.org/kalail/packer

A new type of package manager

*Still under development*


Goals
-----

Package management works but it is far from ideal. There is no simple,
free, platform agnostic way to distribute software. I want to fix this.

Enter **Packer**, a package manager built from scratch to support simple
multiplatform software installation.

It should be:

* Simple
* Extendable
* Multiplatform (Starting with Windows, OSX, Ubuntu)


Installation
------------

Install using the following command .. code-block:: bash

    pip install packer


Dependencies:

* Python 2.7 (must be on PATH)
* pip
* pywin32 (Windows)