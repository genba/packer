import os
import subprocess
from win32com.client import Dispatch
from .base import CorePlatform


class WindowsPlatform(CorePlatform):

    def create_shortcut(self, path, target):
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut('{}.lnk'.format(path))
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = target
        shortcut.IconLocation = target
        shortcut.save()

    def add_to_path(self, path):
        win_style_path = path.replace('/', '\\')
        if win_style_path not in os.environ['PATH']:
            cmd = 'SETX PATH "%%PATH%%;{}"'.format(win_style_path)
            subprocess.Popen(cmd)