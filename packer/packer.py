#!/usr/bin/python
import os
import sys
import shutil
import sqlite3
import requests
import helpers


class Packer(object):
    """Packer
    
    Application instance that manages packages on your system.

    """

    name = 'packer'
    version = '0.1.1'
    database_name = 'database.db'
    package_index_url = 'http://www.google.com/search'
    home = '{}/.packer'.format(os.path.expanduser('~'))
    dirs = {
        'PATH': 'path',
        'TEMP': 'temp',
        'PACKAGES': 'packages',
    }

    def __str__(self):
        return '{} ({})'.format(self.name, self.version)

    @classmethod
    def get_path(cls, path):
        return '{}/{}'.format(cls.home, path)

    @classmethod
    def create_db(cls):
        db = sqlite3.connect(cls.get_path(cls.database_name))
        with db:
            db.execute('''CREATE TABLE IF NOT EXISTS packages (name text)''')
            db.execute('''INSERT OR ROLLBACK INTO packages VALUES (?)''', (cls.name,))
        return db

    @classmethod
    def remove_db(cls):
        os.remove(cls.get_path(cls.database_name))

    @classmethod
    def get_or_create_db(cls):
        if not os.path.exists(cls.get_path(cls.database_name)):
            return cls.create_db()
        return sqlite3.connect(cls.get_path(cls.database_name))

    @classmethod
    def find_install(cls):
        return os.path.exists(cls.home)

    @classmethod
    def validate_install(cls):
        if not cls.find_install():
            raise RuntimeError('Packer has not been installed')
        validators = cls.dirs.values() + [cls.database_name]
        for d in validators:
            if not os.path.exists(cls.get_path(d)):
                raise RuntimeError('Installation looks corrupt')

    @classmethod
    def install(cls):
        """Create the required directories in the home directory"""
        [os.makedirs(cls.get_path(cls.dirs[d])) for d in cls.dirs]
        cls.create_db()

    @classmethod
    def uninstall(cls):
        """Remove the package manager from the system."""
        if os.path.exists(cls.home):
            shutil.rmtree(cls.home)

    @classmethod
    def reinstall(cls):
        """Remove the package manager from the system."""
        cls.uninstall()
        cls.install()


    def __init__(self):
        self.validate_install()
        self.database = self.get_or_create_db()

    def list(self):
        packages = []
        for row in self.database.execute('SELECT * FROM packages'):
            p = helpers.Package._make(row)
            packages.append(p)
        return packages

    def search(self, name):
        # Check for if the package is installed locally
        for row in self.database.execute('SELECT * FROM packages WHERE name=?', (name,)):
            return helpers.Package._make(row)
        # Look in package index
        response = requests.get(self.package_index_url, params={'q':name})
        return response

    def close(self):
        self.database.commit()
        self.database.close()

    def __delete__(self):
        self.close()


if __name__ == '__main__':
    print 'Creating Packer instance'
    packer = Packer()
    print 'Listing Packages'
    pkgs = packer.list()
    print pkgs
    print 'Closing Packer instance'
    packer.close()
