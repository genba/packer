import os
import subprocess
from .base import CorePlatform

class LinuxPlatform(CorePlatform):

    def create_shortcut(self, path, target):    
        os.symlink(target, path)

    def add_to_path(self, path):
        if path not in os.environ['PATH']:
            line = 'export PATH=$PATH:{}'.format(path)
            cmd = 'echo "{}" >> ~/.bashrc'.format(line)
            subprocess.call(cmd, shell=True)
