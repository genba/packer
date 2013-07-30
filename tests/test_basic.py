import time
from .app import TestPacker

class TestBasic(object):


	def setup(self):
		self.app = TestPacker()

	def test_runs(self):
		"""Test whether app runs."""
		pass

	# def test_list(self):
	# 	"""Test whether list runs."""
	# 	self.app.list()

	# def test_initial_state(self):
	# 	"""Test initial  state."""
	# 	pkgs = self.app.list()
	# 	self.assertEqual(self.app.name, pkgs[0][0])

	# def test_search(self):
	# 	"""Test whether search runs."""
	# 	self.app.search('window package management')

	# def test_search_works(self):
	# 	resp = self.app.search('window package management')
	# 	self.assertEqual(resp.status_code, 200)

	def teardown(self):
		self.app.close()
		self.app.uninstall()
