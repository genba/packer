import os
import packer


class DebugPacker(packer.Packer):
    name = 'DebugPacker'
    version = '0.1.0'
    database_name = 'debug.db'
    home = os.getcwd()


if __name__ == '__main__':
    pack = DebugPacker()
    pack.run()
    pack.close()
