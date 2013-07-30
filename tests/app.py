import os
import packer


class TestPacker(packer.Packer):
	database_name='test_database.db'
	package_index_url = 'http://127.0.0.1:8000'
	home = '{}/.packer'.format(os.path.dirname(os.path.abspath(__file__)))