#!/usr/bin/python
import os
import sys
import imp
import shutil
import core.platforms as platforms

from core.pack import Pack
from distutils.version import StrictVersion


NAME = 'PackInstaller'
VERSION = '0.1.0'

APP_HOME = Pack.home
# Get installer path for PyInstaller
if getattr(sys, 'frozen', None):
    INSTALLER_HOME = sys._MEIPASS
else:
    INSTALLER_HOME = os.path.dirname(__file__)

ENTRYPOINT_FILE = 'main.py'
PACK_FILE = 'pack.py'
APP_CORE_DIR = 'core'
APP_PATH_DIR = 'path'
PATH = '{}/{}'.format(APP_HOME, APP_PATH_DIR)

APP_DIRS = [
    APP_PATH_DIR,
    'temp',
    'packages',
]


def check_for_install():
    if not os.path.exists(APP_HOME):
        return False
    return True

def check_for_core():
    return os.path.exists('{}/{}/__init__.py'.format(APP_HOME, APP_CORE_DIR))

def create_dir():
    [os.makedirs('{}/{}'.format(APP_HOME, d)) for d in APP_DIRS]

def copy_core():
    shutil.copytree(
        '{}/{}'.format(INSTALLER_HOME, APP_CORE_DIR),
        '{}/{}'.format(APP_HOME, APP_CORE_DIR)
    )

def install_core():
    copy_core()
    # Create shortcut to pack app
    platforms.PAL.create_shortcut(
        '{}/{}/{}'.format(APP_HOME, APP_PATH_DIR, Pack.name),
        '{}/{}/{}'.format(APP_HOME, APP_CORE_DIR, ENTRYPOINT_FILE)
    )
    # Add path dir to PATH
    platforms.PAL.add_to_path(PATH)

def standard_install():
    create_dir()
    install_core()

def remove():
    if os.path.exists(APP_HOME):
        shutil.rmtree(APP_HOME)

def remove_core():
    location = '{}/{}'.format(APP_HOME, APP_CORE_DIR)
    if os.path.exists(location):
        shutil.rmtree(location)

def replace_core():
    remove_core()
    copy_core()

if __name__ == '__main__':
    print '{} v{}'.format(NAME, VERSION)
    print 'Looking for previous installation...'
    if check_for_install():
        if check_for_core():
            imp.load_source('old_core', '/'.join((APP_HOME, APP_CORE_DIR, '__init__.py')))
            import old_core
            print 'Found v{}'.format(old_core.version)
            # if StrictVersion(old_core.version) >= StrictVersion(Pack.version):
        else:
            print 'Incomplete installation found'
            print os.getcwd()
        print 'Updating core to v{}...'.format(Pack.version)
        replace_core()
        print 'Update complete'
        sys.exit()
    print 'No previous installation found'
    print 'Installing {} v{}'.format(Pack.name, Pack.version)
    standard_install()
    print '\nNOTE: You might have to open a new terminal window'
