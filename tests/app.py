import os
import packer


class TestPacker(packer.Packer):
	database_name='test_database.db'
	home = '{}/.packer'.format(os.path.dirname(os.path.abspath(__file__)))